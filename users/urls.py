from django.urls import path, include
from users import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('auth/', obtain_jwt_token),
    path('', views.UserList.as_view(), name='user-list'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]
