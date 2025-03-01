from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
import openai
# Create your views here.


class GenerateStoryView(APIView):
    permission_classes = [IsAuthenticated]

    def __generate_journey(self, data: dict):
        initial_msg = f"""Write a story based on a perfume's details. The story shoould be creative and really stir some emotional connection with the reader. The perfume's details are as follows:"""

        client = openai.OpenAI()

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" for higher-quality responses
            messages=[
                {"role": "system", "content": initial_msg},
                {"role": "user", "content": data}
            ],
            max_tokens=600,
            temperature=0.7,
        )

        # print(response.choices[0].message.content)
        try:
            result_json = json.loads(
                response.choices[0].message.content.strip())
            print(f"{result_json=}")
            for result in result_json:
                result["maps_link"] = self.__get_google_maps_link(
                    result["name_of_location"], "Cluj-Napoca")

        except json.JSONDecodeError:
            result_json = {"error": "Invalid JSON format returned by AI."}

        return result_json

    def post(self, request):
        ...
