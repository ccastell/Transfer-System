from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^registered-users/$', views.registered_users, name = 'registered-users'),
    url(r'^transfered-articles/$', views.transfered_articles, name = 'transfered-articles'),
    url(r'^saved-articles/$', views.saved_articles, name = 'saved-articles'),

]

