from django.urls import path

from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("", views.add_content, name="add_content"),
    path('delete/<int:item_id>/', views.delete_link, name='delete_link'),
    path('signup/', views.signing, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='add_content'), name='logout'),
]
