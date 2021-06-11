from django.urls import path
from .views import (
    blogOverview,
    articleView
)

urlpatterns = [
    path('', blogOverview, name="overview"),
    path('<slug:slug>/', articleView, name='article'),
]