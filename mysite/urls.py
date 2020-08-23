
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]