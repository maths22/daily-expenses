from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^expenses/', include('expenses.urls',  namespace="expenses")),
    url(r'^admin/', include(admin.site.urls)),
]
