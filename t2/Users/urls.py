from django.urls import path
from .views import user_login_view, user_registration_view, user_logout_view, UserUpdateView

app_name = 'Users'

urlpatterns = [
    path('login/', user_login_view, name='user-login-view'),
    path('register/', user_registration_view, name='user-registration-form'),
    path('logout/', user_logout_view, name='user-logout-view'),
    path('update/<int:id>', UserUpdateView.as_view(), name='user-update-view'),
]
