import allure
import requests
import conftest
import API.urls
import tests.result_json as resultJ
import API.body
import API.algoritmForDict

value = API.algoritmForDict.dict_value
key = API.algoritmForDict.dicte_key
body = API.body
urls = API.urls

@allure.story('Тестирование API по POST, PUT, PATCH, DELETE')
class TestPutResponses:

    @allure.title('PUT Обновление')
    def test_put_update(self):
        responses = requests.put(conftest.request(urls.put_update), json=body.body_put_update)
        result = resultJ.result8
        assert value(responses.json()) == value(result)
        assert key(responses.json()) == key(result)
        assert responses.status_code == 200

    @allure.title('POST CREATE')
    def test_post_create(self):
        responses = requests.post(conftest.request(urls.post_create), json=body.body_post_create)
        assert responses.status_code == 201
        result = resultJ.result7
        assert key(responses.json())[:-1] == key(result)[:-1]
        assert value(responses.json())[:-1] == value(result)[:-1]

    @allure.title('PATCH UPDATE')
    def test_patch_update(self):
        response = requests.patch(conftest.request(urls.patch_update), json=body.body_patch_update)
        assert response.status_code == 200
        result = resultJ.result9
        assert value(response.json()) == value(result)
        assert key(response.json()) == key(result)

    @allure.title('POST регистрация успешна')
    def test_post_register_successful(self):
        response = requests.post(conftest.request(urls.post_register_successful), json=body.body_post_register_successful)
        assert response.status_code == 200
        result = resultJ.result11
        assert result == response.json()

    @allure.title('POST регистрация не прошла')
    def test_post_register_unsuccessful(self):
        response = requests.post(conftest.request(urls.post_register_unsuccessful), json=body.body_post_register_unsuccessful)
        assert response.status_code == 400
        result = resultJ.result12
        assert response.json() == result

    @allure.title('POST Вход успешный')
    def test_post_login_successful(self):
        response = requests.post(conftest.request(urls.post_login_successful), json=body.body_post_login_successful)
        assert response.status_code == 200
        result = resultJ.result13
        assert response.json() == result

    @allure.title('POST Вход не удался')
    def test_post_login_unsuccessful(self):
        response = requests.post(conftest.request(urls.post_login_unsuccessful), json=body.body_post_register_unsuccessful)
        assert response.status_code == 400
        result = resultJ.result14
        assert response.json() == result

    @allure.title("DELETE")
    def test_delete_delete(self):
        response = requests.delete(conftest.request(urls.delete_delete))
        result = resultJ.result10
        assert response.status_code == 204
        assert response.text == result






