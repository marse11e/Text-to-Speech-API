# Django проект для текст в речь

Этот Django проект позволяет конвертировать текст в аудиофайлы и сохранять их.

## Возможности

- Преобразование текста в речь на нескольких языках.
- Сохранение сгенерированных аудиофайлов с уникальными именами.
- Основные административные функции через Django Admin.

## Установка

1. **Клонировать репозиторий:**

    ```bash
    git clone git@github.com:marse11e/Text-to-Speech-API.git
    cd Text-to-Speech-API
    ```

2. **Создать виртуальное окружение:**

    ```bash
    python -m venv venv
    ```

3. **Активировать виртуальное окружение:**

    - На Windows:

        ```bash
        venv\Scripts\activate
        ```

    - На macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Установить зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Применить миграции:**

    ```bash
    python manage.py migrate
    ```

6. **Запустить сервер разработки:**

    ```bash
    python manage.py runserver
    ```

7. **Открыть браузер и перейти по адресу [http://localhost:8000/admin](http://localhost:8000/admin) для доступа к Django Admin.**

8. **Войти, используя административные учетные данные, и начать использовать функционал текст в речь.**

## Использование

1. Войти в Django Admin и перейти в раздел "Text to Speech".

2. Создать новую запись, предоставив текст и уникальное имя файла. По желанию можно выбрать язык речи.

3. Сохранить запись, и соответствующий аудиофайл будет сгенерирован и сохранен в каталоге `voice/`.

4. Чтобы прослушать или скачать сгенерированное аудио, перейти на страницу деталей записи в Django Admin и кликнуть по предоставленной ссылке.

## Вклад

Приветствуются вклады! Если у вас есть идеи для улучшений или новых функций, не стесняйтесь создавать issue или отправлять pull request.

## Лицензия

Этот проект лицензирован по лицензии MIT - подробности см. в файле [LICENSE](LICENSE).