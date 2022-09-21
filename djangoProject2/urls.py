from django.contrib import admin
from django.urls import path
from .views import PublisherListView

from .views import home_page, contact_page, register_page
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_page, name='home'),

    path('register/', register_page, name='register'),
    path('contact/', contact_page, name='contact'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
    path('publishers/', PublisherListView),
]
