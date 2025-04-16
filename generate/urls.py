from django.urls import path
from .views import GenerateStoryView, StoryDeleteView

urlpatterns = [
    path('story', GenerateStoryView.as_view(), name='generate_story'),
    path('story/<int:pk>', StoryDeleteView.as_view(), name='delete_story'),
]
