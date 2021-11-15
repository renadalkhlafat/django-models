from .views import SnackListView ,DetailView
from django.urls import path


urlpatterns =[
    path('',SnackListView.as_view(),name='snacks'),
    path("<int:pk>/", DetailView.as_view(), name="snack_detail"),
]