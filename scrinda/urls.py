from django.conf.urls import url
from examsdb import views

urlpatterns = [
	url(r'^$', views.home_page, name='home'),
	url(r'search/$', views.search_page, name='search'),
]
