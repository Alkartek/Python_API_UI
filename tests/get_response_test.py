import allure
import requests
import conftest
import API.urls
import tests.result_json as resultJ




@allure.story('Тестирование АПИ по GET')
class TestApiGet:
    @allure.title('получить список пользователей')
    def test_get_list_user(self):
        response = requests.get(conftest.request(API.urls.get_list_user))
        assert resultJ.result1 == response.json()

    @allure.title('получить пользователя')
    def test_get_single_user(self):
        response = requests.get(conftest.request(API.urls.get_single_user))
        assert resultJ.result2 == response.json()

    @allure.title('пользователь не найден ')
    def test_get_single_not_found(self):
        response = requests.get(conftest.request(API.urls.get_single_not_found))
        assert resultJ.result3 == response.json()

    @allure.title('получить лист ресурсов')
    def test_get_list_resource(self):
        response = requests.get(conftest.request(API.urls.get_list_resource))
        assert resultJ.result4 == response.json()

    @allure.title('получить один ресурс')
    def test_get_single_resource(self):
        response = requests.get(conftest.request(API.urls.get_single_resource))
        assert resultJ.result5 == response.json()

    @allure.title('искомый ресурс не найден')
    def test_get_single_resource_not_found(self):
        response = requests.get(conftest.request(API.urls.get_single_resource_not_found))
        assert resultJ.result6 == response.json()

    @allure.title('получить замедленный запрос')
    def test_get_delayed_response(self):
        response = requests.get(conftest.request(API.urls.get_delayed_response))
        assert resultJ.result15 == response.json()