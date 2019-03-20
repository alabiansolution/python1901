from django.conf.urls import url
from djangoapp1 import views


urlpatterns = [
    url(r'^$', views.about, name="about"),
    url(r'^$', views.contact, name="contact")
]
