from util import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码

@retry(stop_max_attempt_number=5)
def muacloud():
    try:
        driver = get_web_driver()
        driver.get("https://12o.ooo/auth/login")
        
        # 修改1：邮箱输入框 - 使用 placeholder 属性定位
        driver.find_element_by_xpath("//input[@placeholder='邮箱']").send_keys(username)
        
        # 修改2：密码输入框 - 使用 placeholder 属性定位
        driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys(password)
        
        # 修改3：登录按钮 - 使用按钮文本内容定位
        driver.find_element_by_xpath("//button[contains(@class, 'n-button') and contains(., '登入')]").click()
        
        # 签到按钮的 class 保持不变，这部分不需要修改
        if driver.find_elements_by_xpath("//*[@class='xboard-checkin-button']") != []:
            button = driver.find_element_by_xpath("//*[@class='xboard-checkin-button']")
            driver.execute_script("arguments[0].click();", button)
            print('muacloud签到成功')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    muacloud()
