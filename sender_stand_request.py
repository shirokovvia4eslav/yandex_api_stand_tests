# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=body,
                             headers=data.headers,
                             verify=False)

## Опредение функции get_new_user_token для подстановки в заголовок ключа "Authorization" c новым токеном "Rebely"
def get_new_user_token():
    response = post_new_user(data.user_body)
    current_headers = data.headers.copy()
    current_headers["Authorization"] = "Rebely " + response.json()["authToken"]
    return current_headers

new_user_headers = get_new_user_token()

# Определение функции get_kit_body, которая меняет значения ключа name
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Определение функции post_new_client_kit для создания нового набора нашего пользователя
def post_new_client_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.MAIN_KITS_PATH,
                        json=body,
                        headers=new_user_headers,
                        verify=False)