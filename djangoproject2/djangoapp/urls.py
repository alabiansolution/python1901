from django.conf.urls import url
from djangoapp import views

urlpatterns = [
    url(r'^$', views.about, name='about'),
]
