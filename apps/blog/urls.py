from django.urls import path
from .views import (
    blogOverview
)

urlpatterns = [
    path('', blogOverview, name="overview"),
]