from urllib import request, parse
import threading
import urllib.request
import urllib.parse
import json
import random
import http.cookiejar
import tkinter
from PIL import Image,ImageTk

urlLogin = ''
urlAppSite = ''
urlAppAdd = ''
urlAppData = ''

cookie = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

headers1 = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/75.0.3770.100 Safari/537.36'
}

headers2 = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/75.0.3770.100 Safari/537.36',
    'Cookie': ''
}


dictLogin = {
    '': '伟',  # 名
    '': '阿',  # 姓
    '': '17635366177@163.com',  # 电子邮箱
    '': '17635366177',  # 电话
    '': 'Aa123123',  # 密码
    '': 'Aa123123'  # 确认密码
    # 验证码
}

dictAppSite = {
    '': '澳大利亚',  # 选择访问国
    '': '中国',  # 选择居住国
    '': '澳大利亚签证中心-成都',  # 地点
    '': 'Work and Holiday Visa',  # 选择签证；类别
}

# 点击添加申请人
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

dictAppData = {
    '': '7/15/2019',  # 日期槽
    '': '8:30-8:45'  # 时间槽
    # 验证码
}


def register():

