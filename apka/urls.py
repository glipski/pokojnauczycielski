from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('pokoj.urls', namespace='pokoj')),
    url(r'^pokoj/', include('pokoj.urls', namespace='pokoj')),
    url(r'^konta/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
]