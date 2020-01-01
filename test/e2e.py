

def main_test() :
    if scorse_service("http://192.168.99.100:8777") == True :
        print("0")
    else: print("-1")


def scorse_service(app_url) :
    from selenium import webdriver
    wd=webdriver.Chrome(executable_path="c:\chromedriver.exe")
    wd.get(app_url)
    score=wd.find_element_by_id("score")
    s=int(score.text)
    if s >= 0 and s <=1000 :
        return True
    else: return False, wd.close()


main_test()
