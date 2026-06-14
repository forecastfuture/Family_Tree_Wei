from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 改成你的实际 chromedriver.exe 路径
chromedriver_path = r'E:\6-ticket_purchase\chromedriver.exe'

service = Service(chromedriver_path)
options = webdriver.ChromeOptions()
# 不要添加任何额外参数，测试最简启动
# options.add_argument('--headless')  # 确保没有无头模式

driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.baidu.com')
print("浏览器成功打开百度！")
driver.quit()