
# функция получения пути для сохранения фотографий
# фото относятся к конкретному перевалу
def get_image_path(instance, file):
    return f'photos/mountain_pass-{instance.mountain_pass.id}/{file}'
