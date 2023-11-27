from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import User, Coords, Level, MountainPass, Image


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'phone',
            'fam',
            'name',
            'otc',
        ]
        verbose_name = 'Турист'

    def save(self, **kwargs):
        self.is_valid()
        user = User.objects.filter(email=self.validated_data.get('email'))
        if user.exists():
            return user.first()
        else:
            return User.objects.create(
                email=self.validated_data.get('email'),
                phone=self.validated_data.get('phone'),
                fam=self.validated_data.get('fam'),
                name=self.validated_data.get('name'),
                otc=self.validated_data.get('otc'),
            )


class CoordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coords
        fields = [
            'latitude',
            'longitude',
            'height'
        ]
        verbose_name = 'Координаты'


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ['winter',
                  'summer',
                  'autumn',
                  'spring'
                  ]
        verbose_name = 'Уровень сложности'


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.URLField()
#    image = serializers.CharField()

    class Meta:
        model = Image
        fields = [
            'image',
            'title',
        ]
        verbose_name = 'Фото'


class MountainPassSerializer(WritableNestedModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = MountainPass
        fields = [
            'id',
            'beauty_title',
            'title',
            'other_titles',
            'connect',
            'add_time',
            'user',
            'coords',
            'level',
            'images',
        ]
