from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^posts', views.posts, name='posts'),
	url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
]