
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from rest_framework import routers

from pass_app.views import MountainPassViewSet, EmailAPIView

router = routers.DefaultRouter()
router.register(r'mountain_pass', MountainPassViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('submitData/', include(router.urls)),
    path('api/submitData/user__email=<str:email>', EmailAPIView.as_view()),
#    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
