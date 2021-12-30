from django.urls import path
from apis.v1 import UserCreateView

urlpatterns = [
    path('v1/users/create/', UserCreateView.as_view(), name='apis_v1_user')
]

