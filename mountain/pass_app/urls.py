from django.urls import path

#from .views import MountainPassViewSet
# Можно прописать эти адреса как альтернативу адресам, прописанным в роутере и ууказать их в response в тестах
#urlpatterns = [
#    path('', MountainPassViewSet.as_view({'get': 'list'}), name='mountainpass-list'),
#    path('submitData/<int:pk>/', MountainPassViewSet.as_view({'get': 'list'}), name='mountainpass-detail')
#]
# метод as_view({'get': 'list'}) связывает GET-запрос с возвратом клиенту списка записей из модели таблицы БД
