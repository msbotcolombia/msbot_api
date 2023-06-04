from django.urls import path
from .views import *

urlpatterns = [
    path('v1/signin', CreateUserView.as_view()),
    path('v1/UserList', UserListView.as_view()),
    path('v1/token', MyTokenObtainPairView.as_view(), name='token_obtain_pair')
]