from django.conf.urls import url, include


from .views import (
    home,
    about,
    post_list,
    post_detail,
)

app_name = 'posts'
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^posts/$', post_list, name='list'),
    url(r'^posts/(?P<title>[\w-]+)/$', post_detail, name='detail'),
   
]