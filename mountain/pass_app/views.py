from django.http import JsonResponse
from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = LevelSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class MountainPassViewSet(viewsets.ModelViewSet):
    queryset = MountainPass.objects.all()
    serializer_class = MountainPassSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('user__email',)

    # Создаем перевал
    def create(self, request, *args, **kwargs):
        serializer = MountainPassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_200_OK,
                    'message': 'Успешно!',
                    'id': serializer.data['id'],

                }
            )
        if status.HTTP_400_BAD_REQUEST:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Сервер не разобрал запрос',
                    'id': None,
                }
            )
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response(
                {
                    'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'message': 'Ошибка сервера',
                    'id': None,
                }
            )

    # Возможность частичного редактирования данных о перевале (при статусе "new")
    def update(self, request, *args, **kwargs):
        mountain_pass = self.get_object()
        if mountain_pass.status == 'NW':
            serializer = MountainPassSerializer(
                mountain_pass,
                data=request.data,
                partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'state': '1',
                        'message': 'Изменения в записи внесены'
                    }
                )
            else:
                return Response(
                    {
                        'state': '0',
                        'message': serializer.errors
                    }
                )
        else:
            return Response(
                {
                    'state': '0',
                    'message': f'Текущий статус: {mountain_pass.get_status_display()}, изменить запись нельзя!'
                }
            )


# Список данных обо всех объектах, которые пользователь с почтой <email> отправил на сервер.
class EmailAPIView(generics.ListAPIView):
    serializer_class = MountainPassSerializer

    def get(self, request, *args, **kwargs):
        email = kwargs.get('email', None)
        if MountainPass.objects.filter(user__email=email):
            data = MountainPassSerializer(MountainPass.objects.filter(user__email=email), many=True).data
        else:
            data = {
                'message': f'Пользователя с такой почтой {email} нет'
            }
        return JsonResponse(data, safe=False)
