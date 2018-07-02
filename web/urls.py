from web import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index),
    url(r'^file$', views.FileView.as_view())
]
