# Virtual internship
## MountainPass REST API
Development of a mobile application for Android and IOS that would simplify the task of tourists sending data about mountain passes.

Tourists will use the mobile application. In the mountains, they will enter data about the pass into the application and send it to the FSTR (Sports Tourism Federation [pereval.online](https://pereval.online/)) as soon as Internet access becomes available.

A moderator from the federation will verify and enter information received from users into the database, and they, in turn, will be able to see the moderation status in the mobile application and view the database with objects contributed by others.

The following actions will be available to the user in the mobile application:
* Entering information about a new object (pass) into the object card
* Editing in the application data about objects that have not been sent to the FSTR server. The Internet does not always work at the pass
* Filling out your full name and contact information (phone and email) and then auto-filling them when entering data about new objects
* Sending data to the FSTR server
* Receive notification of submission status (successful/unsuccessful)
* The user agrees with the personal data processing policy if he clicks on the “Submit” button when sending data to the server

Using the mobile application, the user will transmit the following data about the pass to the FSTR:
* coordinates of the pass and its height;
* username;
* user's email and phone number;
* name of the pass;
* photos of the pass.

After this, the tourist presses the “Submit” button in the mobile application.

The mobile application will call the method
***submitData***:

***
GET /submitData/ - receives and displays information about all records (passes).
***
POST /submitData/ - application for entering information about one mountain pass

**Example JSON with information about the pass**

> {
> 
            "id": 5,
            "beauty_title": "pass.",
            "title": "Riffltor",
            "other_titles": "433.Alps",
            "connect": "glacier. Karlingerkees - glacier. Pasterzenboden",
            "add_time": "2023-11-30T15:26:32.837387Z",
            "user": {
                "email": "user@example.com",
                "phone": "89998887766",
                "fam": "Konukhov",
                "name": "Fedor",
                "otc": "Fedorovich"
            },
            "coords": {
                "latitude": 47.12173,
                "longitude": 12.68298,
                "height": 3100
            },
            "level": {
                "winter": "1b",
                "summer": "2b",
                "autumn": "1b",
                "spring": "1b"
            },
            "images": [
                {
                    "image": "https://pereval.online/imagecache/original/object/images/2019/11/27/9bf9a5-94493.jpg",
                    "title": "title"
                }
            ],
            "status": "NW"
        }
        
Method Result: JSON
* status — HTTP code, integer:
    * 500 — error during operation;
    * 400 — Bad Request (if there are not enough fields);
    * 200 - success.
* message — строка:
    * Reason for the error (if there was one);
    * Sent successfully;
    * If the sending is successful, the id of the inserted record is additionally returned.
* id is the identifier that was assigned to the object when it was added to the database.

***
GET /submitData/{id} - получение данных о конкретном горном перевале с выводом всей информации
***

PATCH /submitData/{id} - allows you to edit an existing entry (replacement). If the entry is in the "new" status.

You can edit all fields except those containing your full name, email address and phone number.

***
GET /api/submitData/user_id__email=<str:email> - allows you to obtain data of all objects sent to the server by the user with mail <***str:email***>.
Filtering by email address is implemented using the package ***django-filter***.

The list of external dependencies is given in the file ***requirements.txt***

***
The project is hosted ***pythonanywhere.com***:

https://haelgik.pythonanywhere.com/submitData/

(the project uses the db.sqlite3 database)
 ***
 Documentation ***Swagger***:

 https://haelgik.pythonanywhere.com/api/docs/

 ***
Documentation ***Redoc***
https://haelgik.pythonanywhere.com/api/schema/redoc/
***


  

# Виртуальная стажировка
## MountainPass REST API
Разработка мобильного приложения для Android и IOS, которое упростило бы туристам задачу по отправке данных о горных перевалах.

Пользоваться мобильным приложением будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять их в ФСТР (Федерации спортивного туризма России [pereval.online](https://pereval.online/ )), как только появится доступ в Интернет.

Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.
>для пользователя в мобильном приложении будут доступны следующие действия:

    Внесение информации о новом объекте (перевале) в карточку объекта.
    Редактирование в приложении неотправленных на сервер ФСТР данных об объектах. На перевале не всегда работает Интернет.
    Заполнение ФИО и контактных данных (телефон и электронная почта) с последующим их автозаполнением при внесении данных о новых объектах.
    Отправка данных на сервер ФСТР.
    Получение уведомления о статусе отправки (успешно/неуспешно).
    Согласие пользователя с политикой обработки персональных данных в случае нажатия на кнопку «Отправить» при отправке данных на сервер.

   > C помощью мобильного приложения пользователь будет передавать в ФСТР следующие данные о перевале:

    координаты перевала и его высота;
    имя пользователя;
    почта и телефон пользователя;
    название перевала;
    Фотографии перевала.

  После этого турист нажимает кнопку «Отправить» в мобильном приложении.
  Мобильное приложение вызовет метод
  ***submitData***:
  ***
  GET /submitData/ - получает и выводит информацию о всех записях (перевалах).
  ***
  POST /submitData/ - заявка на внесение информации об одном горном перевале
  
  Пример JSON с информацией о перевале

  > {
            "id": 5,
            "beauty_title": "пер.",
            "title": "Riffltor",
            "other_titles": "433.Альпы",
            "connect": "ледн. Karlingerkees - ледн. Pasterzenboden",
            "add_time": "2023-11-30T15:26:32.837387Z",
            "user": {
                "email": "user@example.com",
                "phone": "89998887766",
                "fam": "Конюхов",
                "name": "Федор",
                "otc": "Федорович"
            },
            "coords": {
                "latitude": 47.12173,
                "longitude": 12.68298,
                "height": 3100
            },
            "level": {
                "winter": "1b",
                "summer": "2b",
                "autumn": "1b",
                "spring": "1b"
            },
            "images": [
                {
                    "image": "https://pereval.online/imagecache/original/object/images/2019/11/27/9bf9a5-94493.jpg",
                    "title": "title"
                }
            ],
            "status": "NW"
        }


  > Результат метода: JSON

* status — код HTTP, целое число:
    * 500 — ошибка при выполнении операции;
    * 400 — Bad Request (при нехватке полей);
    * 200 — успех.
* message — строка:
    * Причина ошибки (если она была);
    * Отправлено успешно;
    * Если отправка успешна, дополнительно возвращается id вставленной записи.
* id — идентификатор, который был присвоен объекту при добавлении в базу данных.
  ***
  GET /submitData/{id} - получение данных о конкретном горном перевале с выводом всей информации
  ***
  PATCH /submitData/{id} - позволяет отредактировать существующую запись (замена), при условии, что она в статусе "new".
  Редактировать можно все поля, кроме тех, что содержат ФИО, адрес почты и номер телефона.
  ***
  GET /api/submitData/user_id__email=<str:email> - позволяет получить данные всех объектов, отправленных на сервер пользователем с почтой <***str:email***>.
  Фильтрация по адресу электронной почты реализуется с помощью пакета ***django-filter***.
  
  Список внешних зависимостей приведен в файле ***requirements.txt***
***
Проект размещен на хостинге ***pythonanywhere.com***:
https://haelgik.pythonanywhere.com/submitData/
 (в проекте используется база данных db.sqlite3)
 ***
 Документация ***Swagger***:
 https://haelgik.pythonanywhere.com/api/docs/
***
Документация ***Redoc***
https://haelgik.pythonanywhere.com/api/schema/redoc/

    
