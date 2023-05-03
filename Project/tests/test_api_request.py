import jsonpath
from Project.tests.requests import Requests
from Project.base.base_page import BasePage
from Project.data.data_page import *
from Project.tests.conf_test_data import *


def test_fetch_user():
    page_requests = Requests()
    response_text = page_requests.get_requests_user(User_2.ID)[1]
    response_code = page_requests.get_requests_user(User_2.ID)[0]
    page_base = BasePage()
    page_base.check_api_code_response(response_code.status_code, 200)
    page_base.check_api_response(jsonpath.jsonpath(response_text, '$.data.first_name')[0], User_2.FIRST_NAME)
    page_base.check_api_response(jsonpath.jsonpath(response_text, '$.data.id')[0], User_2.ID)


def test_check_create_user():
    page_base = BasePage()
    response = test_create_user_api()
    response_code = response[0]
    response_text = response[1]
    page_base.check_api_code_response(response_code.status_code, 201)
    page_base.check_api_response(jsonpath.jsonpath(response_text, '$.name')[0], UserAshish.NAME)


def test_check_delete_user():
    page_base = BasePage()
    page_requests = Requests()
    response = test_create_user_api()
    response_text = response[1]
    id = jsonpath.jsonpath(response_text, '$.id')[0]
    response_code = page_requests.delete_requests_user(id)
    page_base.check_api_code_response(response_code.status_code, 404)




