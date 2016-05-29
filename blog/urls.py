from django.conf.urls import urls

urlpatterns = [
    url(r'^$','blog.views.index', name='index')

]
