"""Модуль содержит тестовые данные для тестов"""
import json

class UserAshish:
    file = open('Project/data/user.json', "r")
    input_data = json.loads(file.read())
    NAME = input_data["name"]

class User_2:
    ID = 2
    FIRST_NAME = 'Janet'
    LAST_NAME = 'Weaver'
