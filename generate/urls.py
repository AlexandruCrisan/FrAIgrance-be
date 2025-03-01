from django.urls import path
from .views import GenerateStoryView

urlpatterns = [
    path('story', GenerateStoryView.as_view(), name='generate_story'),
]
