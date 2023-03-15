from reprlib import Repr

import allure
import pytest

import algoritm
from PageObj.mainPage import mainPage
from PageObj.secondPage import Getter
import PageObj.LOCATORS


po = PageObj.LOCATORS



@allure.story('Получение ожидаемого результата для АПИ')
class TestClass:

    def test_list_user(self, browser):
        algoritm.algoritm_to_get_json2(browser, po.LOCATOR_API1, po.locator1, 1)

    def test_single_user(self,browser):
        algoritm.algoritm_to_get_json2(browser, po.LOCATOR_API2,po.locator2, 2)

    def test_single_user_not_fount(self,browser):
        algoritm.algoritm_to_get_json2(browser,po.LOCATOR_API3, po.locator3, 3)

    def test_list_resurce(self,browser):
        algoritm.algoritm_to_get_json2(browser, po.LOCATOR_API4, po.locator4, 4)

    def test_single_resurce(self, browser):
        algoritm.algoritm_to_get_json2(browser, po.LOCATOR_API5, po.locator5, 5)

    def test_single_rec_not_found(self, browser):
        algoritm.algoritm_to_get_json2(browser, po.LOCATOR_API6, po.locator6, 6)

    def test_create(self, browser):
        algoritm.algoritm_to_get_json(browser, po.LOCATOR_API7, po.locator7, 7)

    def test_update(self, browser):
        algoritm.algoritm_to_get_json(browser, po.LOCATOR_API8, po.locator8, 8)

    def test_patch_update(self,browser):
        algoritm.algoritm_to_get_json(browser, po.LOCATOR_API9, po.locator9, 9)

    def test_delete(self, browser):
        algoritm.algoritm_to_get_jsonDelete(browser, po.LOCATOR_API10, po.locator10, 10)

    def test_register_seccessful(self, browser):
        algoritm.algoritm_to_get_json(browser, po.LOCATOR_API11, po.locator11, 11)

    def test_register_unseccessful(self,browser):
        algoritm.algoritm_to_get_json(browser, po.LOCATOR_API12, po.locator12, 12)

    def test_login_seccessful(self, browser):
        algoritm.algoritm_to_get_json(browser, po.LOCATOR_API13, po.locator13, 13)

    def test_login_unseccessful(self, browser):
        algoritm.algoritm_to_get_json(browser, po.LOCATOR_API14, po.locator14, 14)

    def test_delayed_response(self, browser):
        algoritm.algoritm_to_get_json2(browser, po.LOCATOR_API15, po.locator15, 15)


