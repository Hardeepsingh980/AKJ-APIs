from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from kirtan.views import KirtanViewSet


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/kirtan/', KirtanViewSet.as_view()),
    path('admin/', admin.site.urls),
    path('kirtan/',include('kirtan.urls'))
]
