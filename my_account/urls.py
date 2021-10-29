from django.urls import path

from . import views

urlpatterns = [
    path('', views.AccountPageView.as_view(), name='my_account'),
    path('upload/', views.image_upload_view),
]