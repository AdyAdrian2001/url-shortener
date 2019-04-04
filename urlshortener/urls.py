from django.urls import path
from . import views
from django.conf.urls import include, url
from urlshortener.views import HomeView, ShortUrlView

urlpatterns = [
    # for our home/index page
    path('', HomeView.as_view()),
    # when short URL is requested it redirects to original URL
    path('<shortcode>', ShortUrlView.as_view()),
]
