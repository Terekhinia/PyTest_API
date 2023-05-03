import json
import requests
from Project.base.base_page import BasePage
from Project.tests.config import config

class Requests():

    def get_requests_user(self, id_user):
        '''Возвращает ответ в виде списка lst[0] - код ответа, lst[1] - ответ в виде словаря со всеми значениями'''
        path = f'api/users/{id_user}'
        response_code = requests.get(url=config.baseUrl + path)
        response = json.loads(response_code.text)
        lst = [response_code, response]
        return lst

    def delete_requests_user(self, id_user):
        '''Удаляет юзера по id. Возвращает ответ в виде списка lst[0] - код ответа'''
        path = f'api/users/{id_user}'
        response_code = requests.get(url=config.baseUrl + path)
        return response_code


