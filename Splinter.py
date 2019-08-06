from splinter.browser import Browser

urlAppSite = ''
urlAppAdd = ''
urlAppData = ''

def function():
    b = Browser("chrome")
    b.visit(AppSite)
    dictAppSite = {
        '': '澳大利亚',  # 选择访问国
        '': '中国',  # 选择居住国
        '': '澳大利亚签证中心-成都',  # 地点
        '': 'Work and Holiday Visa',  # 选择签证；类别
    }
    b.fill_form(dictAppSite)
    button = b.find_by_value(u"继续")
    button.click()
    
    b.visit(AppAdd)
    dictAppAdd = {
        '': 'G11111111',  # 护照号码
        '': '1/1/1999',  # 出生日期
        '': '1/1/2025',  # 护照失效期
        '': 'CHINA',  # 选择国籍
        '': '阿',  # 名
        '': '伟',  # 姓
        '': '男性',  # 性别
        '': '+8612345678900',  # 电话号码
        '': '123123@163.com'  # 电子邮箱
        # 验证码
    }
    b.fill_form(dictAppSite)
    button = b.find_by_value(u"提交")
    button.click()

    b.visit(AppData)
    dictAppData = {
        '': '7/15/2019',  # 日期槽
        '': '8:30-8:45'  # 时间槽
        # 验证码
    }
    b.fill_form(dictAppAdata)
    button = b.find_by_value(u"提交")
    button.click()

threads = 5
for i in range(threads):
    thread = threading.Thread(target=function)
    thread.start()


