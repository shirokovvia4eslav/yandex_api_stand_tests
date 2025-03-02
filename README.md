# Тесты на проверку создания наборов в Яндекс.Прилавок с помощью API Яндекс.Прилавок.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполняется командой pytest
- В проекте шесть файлов: configuration.py, data.py, sender_stand_request.py, create_kit_name_kit_test.py, README.md, .gitignore.
# Чек-лист проверок
1. Допустимое количество символов (1): kit_body = { "name": "a" }
- ОР: Код ответа — 201. В ответе поле name совпадает с полем name в запросе
2. Допустимое количество символов (511): kit_body = { "name":"Тестовое значение для этой проверки будет ниже" }
- ОР: Код ответа — 201. В ответе поле name совпадает с полем name в запросе
3. Количество символов меньше допустимого (0): kit_body = { "name": "" }
- ОР: Код ответа — 400
4. Количество символов больше допустимого (512): kit_body = { "name":"Тестовое значение для этой проверки будет ниже"
- ОР: Код ответа — 400
5. Разрешены английские буквы: kit_body = { "name": "QWErty" }
- ОР: Код ответа — 201. В ответе поле name совпадает с полем name в запросе
6. Разрешены русские буквы: kit_body = { "name": "Мария" }
- ОР: Код ответа — 201. В ответе поле name совпадает с полем name в запросе
7. Разрешены спецсимволы: kit_body = { "name": ""№%@"," }
- ОР: Код ответа — 201. В ответе поле name совпадает с полем name в запросе
8. Разрешены пробелы: kit_body = { "name": " Человек и КО " }
- ОР: Код ответа — 201. В ответе поле name совпадает с полем name в запросе
9. Разрешены цифры: kit_body = { "name": "123" }
- ОР: Код ответа — 201. В ответе поле name совпадает с полем name в запросе
10. Параметр не передан в запросе: kit_body = { }
- ОР: Код ответа — 400
11. Передан другой тип параметра (число): kit_body = { "name": 123 }
- ОР: Код ответа — 400

# Тестовые значения для проверок №2 и №4

- Test2 Допустимое количество символов (511):
kit_body = {    "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
- Test4 Количество символов больше допустимого (512):
kit_body = {  "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}


