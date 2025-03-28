from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import home,deletevideo

urlpatterns = [
    path('',home,name='home'),
    path('delete-video/<int:video_id>',deletevideo,name='delete'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]