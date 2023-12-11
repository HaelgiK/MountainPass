import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *
from django.urls import reverse

from .serializers import MountainPassSerializer


class MountainPassTestCase(APITestCase):
    # Метод setUp запускается перед каждым тестовым примером
    # (для настройки объектов, которые могут изменяться во время тестов)
    def setUp(self):
        # Объекты первого перевала
        self.mountain_pass_1 = MountainPass.objects.create(
            user = User.objects.create(
                email='cruzen@example.com',
                phone='89991234567',
                fam='Иван',
                name='Крузенштерн',
                otc='Федорович'
            ),
            beauty_title='пер.',
            title='Riffltor',
            other_titles='433.Альпы',
            connect='ледн. Karlingerkees - ледн. Pasterzenboden',
            coords=Coords.objects.create(
                latitude=47.12173,
                longitude=12.68298,
                height=3100
            ),
            level=Level.objects.create(
                winter='1b',
                summer='1a',
                autumn='1a',
                spring='1a'
            )
        )
        # Изображеение первого перевала
        self.image_1 = Image.objects.create(
            image="https://altaitg.ru/upload/iblock/c80/c80fb8d75505232e59812ad2f20f8684.jpg",
            title="title",
            mountain_pass=self.mountain_pass_1
        )

        # Объекты второго перевала
        self.mountain_pass_2 = MountainPass.objects.create(
            user=User.objects.create(
                email='mail@example.com',
                phone='9991234567',
                fam='Боб',
                name='Билли',
                otc='Торнтон'
            ),
            beauty_title='пер.',
            title='Brizio',
            other_titles='433.Альпы',
            connect='ледн. Karlingerkees - ледн. Pasterzenboden',
            coords=Coords.objects.create(
                latitude=43.6148,
                longitude=41.10383,
                height=2892
            ),
            level=Level.objects.create(
                winter='1a',
                summer='1a',
                autumn='1a',
                spring='1a'
            )
        )
        # Изображеение второго перевала
        self.image_2 = Image.objects.create(
            image="https://altaitg.ru/upload/iblock/75d/75df2c2bda5111bb4c19c646e9ca7fc6.jpg",
            title="title",
            mountain_pass=self.mountain_pass_2
        )

    # Проверка получения всех записей о перевале
    def test_mountain_list(self):
#        url = reverse('mountainpass-list')
        response = self.client.get(reverse('mountainpass-list'))
        serializer_data = MountainPassSerializer(
            [
                self.mountain_pass_1,
                self.mountain_pass_2
            ],
            many=True
        ).data
        # Функции проверки утверждений
        # (позволяют проверять различные условия и ожидаемые результаты)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data['results'])

    # Проверка получение записи о первом перевале
    def test_mountain_detail(self):
#        url = reverse('mountainpass-detail', kwargs={'pk': self.mountain_pass_1.pk})
        response = self.client.get(reverse('mountainpass-detail', kwargs={'pk': self.mountain_pass_1.id}))
#        response = self.client.get(reverse('mountain_detail', args=(self.mountain_pass_1.id)))
        serializer_data = MountainPassSerializer(self.mountain_pass_1).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Проверяем создание записи обо всех объектах,
    # добавленных пользователем с почтой user.email
    def test_by_mail(self):
        url = reverse('email-mountain_pass', args=(self.mountain_pass_1.user.email,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MountainPassSerializerTestCase(TestCase):
    def setUp(self):
        self.mountain_pass_1 = MountainPass.objects.create(
            id=2,
            beauty_title="пер.",
            title="Riffltor",
            other_titles="433.Альпы",
            connect="ледн. Karlingerkees - ледн. Pasterzenboden",
            add_time="2023-11-24T14:33:19.590646Z",
            user=User.objects.create(
                email="cruzen@example.com",
                phone="89991234567",
                fam="Иван",
                name="Крузенштерн",
                otc="Федорович"
            ),
            coords=Coords.objects.create(
                latitude=47.12173,
                longitude=12.68298,
                height=3100
            ),
            level=Level.objects.create(
                winter="1b",
                summer="1a",
                autumn="1a",
                spring="1a"
            )
        )

        self.image_1 = Image.objects.create(
            image="https://altaitg.ru/upload/iblock/c80/c80fb8d75505232e59812ad2f20f8684.jpg",
            title="title",
            mountain_pass=self.mountain_pass_1
        )

        self.mountain_pass_2 = MountainPass.objects.create(
            id=3,
            beauty_title="пер.",
            title="Brizio",
            other_titles="433.Альпы",
            connect="ледн. Karlingerkees - ледн. Pasterzenboden",
            add_time="2023-11-24T14:46:17.390528Z",
            user=User.objects.create(
                email="mail@example.com",
                phone="9991234567",
                fam="Боб",
                name="Билли",
                otc="Торнтон"
            ),
            coords=Coords.objects.create(
                latitude=43.6148,
                longitude=41.10383,
                height=2892
            ),
            level=Level.objects.create(
                winter="1a",
                summer="1a",
                autumn="1a",
                spring="1a"
            )
        )

        self.image_2 = Image.objects.create(
            image="https://altaitg.ru/upload/iblock/75d/75df2c2bda5111bb4c19c646e9ca7fc6.jpg",
            title="title",
            mountain_pass=self.mountain_pass_2
        )
