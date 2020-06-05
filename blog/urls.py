from django.urls import path

from diploma_project import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path('selfManager-<slug:slug>', views.selfManagerView.as_view(), name='selfManager'),
    path('posts/<slug:slug>', views.PostView.as_view(), name='postView'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
