from django.urls import path
from .views import SignupView, LoginView, LogoutView

app_name = 'accounts'
urlpatterns = [
    path('signup/', SignupView, name="signup"),
    path('login/', LoginView, name="login"),
    path('logout/', LogoutView, name="logout"),
]
