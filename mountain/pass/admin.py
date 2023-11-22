from django.contrib import admin
from .models import User, Coords, Image, Level, MountainPass


admin.site.register(User)
admin.site.register(Coords)
admin.site.register(Image)
admin.site.register(Level)
admin.site.register(MountainPass)
