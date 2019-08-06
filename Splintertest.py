from splinter.browser import Browser
import threading

url = "http://moni.chinawhver.com/city.html"
threadNum=3

def function():
    # 账户登录
    browser = Browser('chrome')
    browser.visit(url)

    # 账户注册
    browser.choose("ctl00$plhMain$cboVisaCategory", "Beijing")  # 第一个页面 提交地点选择
    browser.find_by_xpath('//input[@type="submit"]').click()  # 第一个页面 提交

    browser.fill("ctl00$plhMain$tbxNumOfApplicants", 2)  # 第二个页面 同行人数
    browser.choose("ctl00$plhMain$cboVisaCategory", "17")   # 第二个页面 签证类型选择
    browser.find_by_xpath('//*[@id="ctl00_plhMain_ControlsTable"]/tbody/tr[8]/td/a[1]/input').click()   # 第二个页面 提交

    # 抢票
    browser.fill("name", "123@123.com")  # 第三个页面 邮箱输入
    browser.find_by_xpath('//*[@id="ctl00_plhMain_ImageButton"]').click()   # 第三个页面 提交

    browser.fill("ctl00$plhMain$txtPassword1", "Aa123123")  # 第四个页面 密码
    browser.fill('ctl00$plhMain$txtCnfPassword1', "Aa123123")  # 第四个页面 确认密码
    browser.find_by_xpath('//*[@id="ctl00_plhMain_ImageButton"]').click()   # 第四个页面 提交
    
    browser.fill("ctl00$plhMain$txtEmail","123@123.com")  # 第四个页面 邮箱输入
    browser.fill("", "Aa123123")  # 第四个页面 确认密码
    browser.find_by_xpath('//*[@id="ctl00_plhMain_ImageButton"]').click()   # 第四个页面 提交


    browser.fill("ctl00$plhMain$repAppVisaDetails$ctl01$tbxPassportNo", "G11111111")  # 第五个页面 护照
    browser.choose("ctl00$plhMain$repAppVisaDetails$ctl01$cboTitle", "MR.")   # 第五个页面 性别
    browser.fill("ctl00$plhMain$repAppVisaDetails$ctl01$tbxFName", "伟")  # 第五个页面 名
    browser.fill("ctl00$plhMain$repAppVisaDetails$ctl01$tbxLName", "阿")  # 第五个页面 性
    browser.fill("ctl00$plhMain$repAppVisaDetails$ctl01$tbxSTDCode", "+86")  # 第五个页面 区号
    browser.fill("ctl00$plhMain$repAppVisaDetails$ctl01$tbxMobileNumber", "12345678900")  # 第五个页面 电话
    browser.find_by_xpath('//*[@id="ctl00_plhMain_btnSubmit"]').click()   # 第五个页面 提交


    browser.find_by_xpath('//*[@id="ctl00_plhMain_cldAppointment"]/tbody/tr[5]/td[5]/a').click()   # 日期页面提交
    browser.find_by_xpath('//*[@id="ctl00_plhMain_gvSlot_ctl02_lnkTimeSlot"]').click()   # 时间页面提交
    browser.find_by_xpath('//*[@id="ctl00_plhMain_ImageButton1"]').click()  # 提交



for i in range(threadNum):
    thread = threading.Thread(target=function)
    thread.start()

    
