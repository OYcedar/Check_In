from util import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码

@retry(stop_max_attempt_number=5)
def muacloud():
    try:
        driver = get_web_driver()
        driver.get("https://12o.ooo/auth/login")
        
        # 等待页面加载完成
        wait = WebDriverWait(driver, 10)
        
        # 修改1：等待邮箱输入框出现，然后输入
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        email_input.clear()
        email_input.send_keys(username)
        
        # 修改2：等待密码输入框出现，然后输入
        password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
        password_input.clear()
        password_input.send_keys(password)
        
        # 修改3：等待登录按钮可点击，然后点击
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'n-button') and contains(., '登入')]")))
        login_button.click()
        
        # 等待签到按钮出现
        try:
            checkin_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='xboard-checkin-button']")))
            driver.execute_script("arguments[0].click();", checkin_button)
            print('muacloud签到成功')
        except:
            print('muacloud未找到签到按钮，可能已经签到过了')
            
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    muacloud()
