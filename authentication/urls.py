from django.urls import path
from django.conf.urls.static import static
from student import settings
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("feed", views.feed, name="feed"),
    path("home", views.home, name="home"),
    path("signup", views.sign_up, name="signup"),
    path("createpost/", views.create_post, name="createpost"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
