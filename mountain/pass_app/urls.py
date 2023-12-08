from django.urls import path

from .views import MountainPassViewSet

urlpatterns = [
    path('', MountainPassViewSet.as_view({'get': 'list'}), name='mountain_pass-list'),
    # метод as_view({'get': 'list'}) связывает GET-запрос с возвратом клиенту списка записей из модели таблицы БД
    path('submitData/<int:pk>/', MountainPassViewSet.as_view({'get': 'list'}), name='mountain_detail')
]
