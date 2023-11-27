
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from pass_app.views import MountainPassViewSet

router = routers.DefaultRouter()
router.register(r'mountain_pass', MountainPassViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('submitData/', include(router.urls)),
]
