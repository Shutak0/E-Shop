from django.urls import include, re_path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('categories', views.categories, name='categories'),
    re_path(r'^(?P<name>[-\w]+)/$', views.group, name='group'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.productpage, name='productpage'),
    path('accounts/profile/', views.profile, name="accounts/profile")
]
