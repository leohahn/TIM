from django.conf.urls import url

from . import views

app_name = 'tim_app'
urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^ranking$', views.ranking, name='ranking'),
    url(r'^request$', views.request, name='request'),
    url(r'^offer$', views.offer, name='offer'),
	url(r'^list$', views.list, name='list'),
]