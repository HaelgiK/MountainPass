from django.urls import path

from .views import MountainPassViewSet

urlpatterns = [
    path('', MountainPassViewSet.as_view({'get': 'list'}), name='mountain_pass-list'),
    path('<int:id/', MountainPassViewSet.as_view({'get': 'list'}), name='mountain_detail')
]
