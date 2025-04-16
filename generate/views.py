from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import openai
from rest_framework.response import Response
import json
from user.services.user_service import UserService
from .models import Story
from django.shortcuts import get_object_or_404
# Create your views here.


class GenerateStoryView(APIView):
    permission_classes = [IsAuthenticated]

    def __generate_journey(self, data: dict):
        # initial_msg = "You are a master storyteller who crafts immersive, emotionally rich short stories. "
        # "Each story should evoke a deep emotional response—whether nostalgia, passion, longing, or mystery—"
        # "without ever referencing perfume, scents, or fragrance notes. Instead, describe vivid scenes, emotions, and experiences "
        # "that naturally induce the intended feeling. Your writing should be poetic, atmospheric, and cinematic."

        client = openai.OpenAI()

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": (
                    "You are a master storyteller who crafts immersive, emotionally rich short stories. "
                    "Each story should evoke a deep emotional response"
                    "without ever referencing perfume, scents, or fragrance notes. Instead, describe vivid scenes, emotions, and experiences "
                    "that naturally induce the intended feeling. Your writing should be poetic, atmospheric, and cinematic."
                )},
                {"role": "user", "content": (
                    f"Write a short story that captures the essence of the feelings induces by the perfume: {data}. "
                    f"The story should immerse the reader in a vivid experience that conveys this feeling without mentioning scent or perfume."
                    f"\n\nReturn only a JSON object with 2 keys: 'title' and 'story'."
                )}
            ],
            response_format={"type": "json_object"},
            max_tokens=325,
            temperature=1.3,
            top_p=0.9,
            presence_penalty=0.6,  # Encourages introducing new ideas
            frequency_penalty=0.4,
        )

        # print(response.choices[0].message.content)
        try:
            result_json = json.loads(
                response.choices[0].message.content.strip())
            print(f"{result_json=}")

        except json.JSONDecodeError:
            result_json = {"error": "Invalid JSON format returned by AI."}

        return result_json

    def post(self, request):
        data = request.data
        story = self.__generate_journey(data)

        Story.objects.create(user=request.user, content=story["story"], title=story["title"])

        user = request.user

        user.credits -= 4
        user.save()

        return Response(story, status=200)


class StoryDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Story, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
