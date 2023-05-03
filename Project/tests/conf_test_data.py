"""
Модуль содержит методы для настройки тестовых данных необходимых для прохождения тестов
"""
import requests
import json
from Project.tests.config import config



def test_create_user_api():
    '''Функция создания юзера через отправку post запроса.
    Возвращает ответ в виде списка lst[0] - код ответа, lst[1] - ответ в виде словаря со всеми значениями'''
    file = open('Project/data/user.json', "r")
    path = "api/users"
    input_data = json.loads(file.read())
    response_code = requests.post(url=config.baseUrl + path, json=input_data)
    response = json.loads(response_code.text)
    lst = [response_code, response]
    return lst


