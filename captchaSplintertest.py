from splinter.browser import Browser
import threading
import urllib.request
import urllib.parse
import json
import random
import http.cookiejar
import tkinter
from PIL import Image,ImageTk

url = "http://moni.chinawhver.com/city.html"
threadNum=1

cookie = http.cookiejar.CookieJar() # 管理存储HTTP的cookie值
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie)) #支持验证、cookie、其它HTTP高级功能
headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/75.0.3770.100 Safari/537.36'
}
    
def get_captcha(): # 获取注册验证码
    req_auth = urllib.request.Request(url='http://moni.chinawhver.com/Australia%20Visa_files/MyCaptchaImage.jpg')
    # req_auth = urllib.request.Request(url='http://moni.chinawhver.com/Australia%20Visa_files/MyCaptchaImage.jpg'+str(random.random()))
    filename = r"captcha.jpg"
    f = open(filename,"wb")
    f.write(opener.open(req_auth).read())
    f.close()
    
def show_captcha(captcha_shower): # 显示注册验证码
    get_captcha()
    im=Image.open("captcha.jpg")
    img=ImageTk.PhotoImage(im)
    captcha_shower.configure(image=img)
    captcha_shower.image=img





def function():
    # 账户登录
    browser = Browser('chrome')
    browser.visit(url)

    # 账户注册
    captcha=input()

    browser.fill("ctl00$plhMain$MyCaptchaControl1", captcha)  # 第二个页面 同行人数
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
        
    root = tkinter.Tk() # 界面编辑
    get_captcha()

    captcha_shower=tkinter.Label(root)
    captcha_shower.grid(column=2,row=0,sticky=tkinter.W+tkinter.N+tkinter.S+tkinter.E)
    show_captcha(captcha_shower)

    
