from PageObj.mainPage import mainPage
from PageObj.secondPage import Getter


def algoritm_to_get_json(browser,LOCATOR_1,LOCATOR_2,NUMBER):
    mainpage = mainPage(browser)
    mainpage.to_go()
    mainpage.responseGet1(LOCATOR_1=LOCATOR_1,LOCATOR_2=LOCATOR_2)
    get_res = Getter(browser)
    result = get_res.getText()
    f = open(f'result_json.py', 'a+')
    f.write(f'result{NUMBER} = {result}'+'\n')
    f.close()

def algoritm_to_get_json2(browser,LOCATOR_1,LOCATOR_2,NUMBER):
    mainpage = mainPage(browser)
    mainpage.to_go()
    mainpage.responseGet2(LOCATOR_1=LOCATOR_1,LOCATOR_2=LOCATOR_2)
    get_res = Getter(browser)
    result = get_res.getText2()
    f = open(f'result_json.py', 'a+')
    f.write(f"result{NUMBER} = {result}\n")
    f.close()

def algoritm_to_get_jsonDelete(browser,LOCATOR_1,LOCATOR_2,NUMBER):
    mainpage = mainPage(browser)
    mainpage.to_go()
    mainpage.responseGet1(LOCATOR_1=LOCATOR_1,LOCATOR_2=LOCATOR_2)
    get_res = Getter(browser)
    result = get_res.getText()
    f = open('result_json.py', 'a+')
    f.write(f"result{NUMBER} = '{result}'\n")
    f.close()



