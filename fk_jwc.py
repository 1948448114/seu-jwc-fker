# -*- coding: cp936 -*-
#!/usr/bin/python  
#import urllib.request
import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re  
  
#��¼����ҳ��  
hosturl = 'http://xk.urp.seu.edu.cn/' 
#post���ݽ��պʹ����ҳ�棨����Ҫ�����ҳ�淢�����ǹ����Post���ݣ�  
posturl = 'http://xk.urp.seu.edu.cn/jw_css/system/login.action' 
  
#����һ��cookie��������������ӷ���������cookie�����أ������ڷ�������ʱ���ϱ��ص�cookie  
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener)  
  
#�򿪵�¼��ҳ�棨����Ŀ���Ǵ�ҳ������cookie����������������post����ʱ����cookie�ˣ������Ͳ��ɹ���  
h = urllib2.urlopen(hosturl)
image = urllib2.urlopen('http://xk.urp.seu.edu.cn/jw_css/getCheckCode')
f = open('code.jpg', 'wb')
f.write(image.read())
f.close()

code = raw_input('��code.jpg ����������ַ�')


#����header
headers = { 'Host' : 'xk.urp.seu.edu.cn',
            'Proxy-Connection' : 'keep-alive',
            'Origin' : 'http://xk.urp.seu.edu.cn',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
            'Referer' : 'http://xk.urp.seu.edu.cn/jw_css/system/login.action'
            
           }  
#����Post���� 
postData = {
            'userId' : '213111111', #����û���  
            'userPassword' : '11111111', #������룬  
            'checkCode' : code,   #��֤�� 
            'x' : '33',  #���
            'y' : '5'       #���2
  
            }  
  
#��Ҫ��Post���ݱ���  
postData = urllib.urlencode(postData)  
  
#ͨ��urllib2�ṩ��request��������ָ��Url�������ǹ�������ݣ�����ɵ�¼����  

request = urllib2.Request(posturl, postData, headers)
print request
response = urllib2.urlopen(request)  
text = response.read().decode('utf-8')  
print text  
