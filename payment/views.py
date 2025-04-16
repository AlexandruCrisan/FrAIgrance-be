from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
import stripe
import os
from dotenv import load_dotenv
from user.models import User
# Create your views here.

load_dotenv()


class CheckoutSessionView(APIView):
    permission_classes = [IsAuthenticated]
    stripe.api_key = os.getenv("STRIPE_API_SECRET_KEY")

    def post(self, request):
        user = request.user

        price_options = [
            {
                "price": os.getenv("PRICE_ID0"),
                "quantity": 3,
                "adjustable_quantity": {
                    "enabled": True,
                    "minimum": 3,
                },
            }
        ]

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="payment",
            allow_promotion_codes=True,  # Optional: Allow discount codes
            line_items=price_options,
            success_url=os.getenv("CLIENT_URL"),
            metadata={"email": user.email},
            customer_email=user.email,
        )

        return Response({"url": session.url}, status=200)


class StripeWebhook(APIView):
    # Allow unauthenticated users to sign up
    permission_classes = [AllowAny]

    def post(self, request):
        payload = request.body
        sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
        endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret)
        except ValueError:
            return JsonResponse({"error": "Invalid payload"}, status=400)
        except stripe.error.SignatureVerificationError:
            return JsonResponse({"error": "Invalid signature"}, status=400)

        if event["type"] == "checkout.session.completed":
            session = event["data"]["object"]
            user_email = session["metadata"]["email"]

            # Determine how many credits the user bought
            total_credits = session.get('amount_total') / 100 / 0.5
            # print(session)
            # print(f"User {user_email} bought {total_credits} credits!")
            # Update user's credit balance
            user = User.objects.get(email=user_email)
            user.credits += total_credits
            user.save()

        return JsonResponse({"status": "success"})
