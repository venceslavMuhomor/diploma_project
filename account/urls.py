from django.contrib.auth import views as auth_views
from django.urls import path
from diploma_project import settings
from . import views
from django.conf.urls.static import static
urlpatterns = [
path('login/', auth_views.LoginView.as_view(), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('', views.dashboard.as_view(), name='dashboard'),
path('post_edit-/<int:pk>', views.editPost, name='post_edit'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
