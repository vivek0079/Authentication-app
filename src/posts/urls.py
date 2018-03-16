from django.conf.urls import url, include


from .views import (
    home,
    about,
    post_list,
)

app_name = 'post'
urlpatterns = [
   url(r'^$', home, name='home'),
   url(r'^about/$', about, name='home'),
   url(r'^list/$', post_list, name='list'),
]