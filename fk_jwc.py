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
import time


#####����#####
userName = '213111111'  #һ��ͨ��
passWord = '111111111'  #һ��ͨ��
semester = 2            #ѧ�ڱ�ţ���ѧ��Ϊ1����ѧ��Ϊ2
sleepTime = 1          #ÿ����ѡ��һ�Σ��ӳٵ�ʱ�䣬��λ�루0Ϊ�����ߣ�С�ı�T��
#####����#####


def postXuan(course):
    hosturl ='http://xk.urp.seu.edu.cn'
    posturl = 'http://xk.urp.seu.edu.cn/jw_css/xk/runSelectclassSelectionAction.action?select_jxbbh='+course[1]+'&select_xkkclx='+course[2]+'&select_jhkcdm='+course[0]
    headers = { 'Host' : 'xk.urp.seu.edu.cn',
            'Proxy-Connection' : 'keep-alive',
            'Content-Length' : '2',
            'Accept' : 'application/json, text/javascript, */*',
            'Origin':'http://xk.urp.seu.edu.cn',
           'X-Requested-With': 'XMLHttpRequest',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
          }
    postData = {'{}':''
        }
    postData = urllib.urlencode(postData)
    request = urllib2.Request(posturl, postData, headers)
    response = urllib2.urlopen(request)  
    text = response.read().decode('utf-8')  
 #   print text
    return text

def stateCheck(text):
    
    if (text.find(u'�ɹ�ѡ��') != -1)or(text.find(u'�����Ƽ�') != -1):
        return 0
    if text.find(u'����') != -1:
        return 1
    if text.find(u'ʧ��') != -1:
        return 2
    
    
  
#��¼����ҳ��  
hosturl = 'http://xk.urp.seu.edu.cn/' 
#post���ݽ��պʹ����ҳ�棨����Ҫ�����ҳ�淢�����ǹ����Post���ݣ�  
posturl = 'http://xk.urp.seu.edu.cn/jw_css/system/login.action' 
  
#����һ��cookie������
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener)  
  
 
h = urllib2.urlopen(hosturl)                                            #�򿪵�¼��ҳ�棬װ��cookie 
image = urllib2.urlopen('http://xk.urp.seu.edu.cn/jw_css/getCheckCode')
f = open('code.jpg', 'wb')
f.write(image.read())
f.close()

code = raw_input('���۾����ã����ҿ��������ɡ����������Ŀ¼�µ�code.jpg���������������������λ����\n')

#��¼�İ���
#����header
headers = { 'Host' : 'xk.urp.seu.edu.cn',   
            'Proxy-Connection' : 'keep-alive',
            'Origin' : 'http://xk.urp.seu.edu.cn',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
            'Referer' : 'http://xk.urp.seu.edu.cn/jw_css/system/login.action'
            
           }  
#����Post���� 
postData = {
            'userId' : userName,       #����û���  
            'userPassword' : passWord, #������룬  
            'checkCode' : code,           #��֤�� 
            'x' : '33',     #���
            'y' : '5'       #���2
  
            }

print('���ڰ����½..')
postData = urllib.urlencode(postData)  #Post���ݱ���   
request = urllib2.Request(posturl, postData, headers)#ͨ��urllib2�ṩ��request��������ָ��Url�������ǹ�������ݣ�����ɵ�¼���� 
response = urllib2.urlopen(request)  
text = response.read().decode('utf-8')  
#print text


####################################################################
#������ѧ�ڵİ���
####################################################################
print('��¼�ɹ�����ȥ���������..���jwc˵�Ҳ�������')
time.sleep(6)      #��ֹ����'��������'��ʾ
xq = str(semester)           #ѧ��
geturl = 'http://xk.urp.seu.edu.cn/jw_css/xk/runXnXqmainSelectClassAction.action?Wv3opdZQ89ghgdSSg9FsgG49koguSd2fRVsfweSUj=Q89ghgdSSg9FsgG49koguSd2fRVs&selectXn=2014&selectXq='+xq+'&selectTime=2014-05-30%2013:30~2014-06-07%2023:59'
hosturl = 'xk.urp.seu.edu.cn'
headers = { 'Host' : 'xk.urp.seu.edu.cn',
            'Proxy-Connection' : 'keep-alive',
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',        
           }
getData = {}
print('���ڸ���ѡ��ѧ��..')
getData = urllib.urlencode(getData)
request = urllib2.Request(geturl, getData, headers)
response = urllib2.urlopen(request)
text = response.read().decode('utf-8')  
#print text

#########################
#ƥ����ԡ������Ƽ���������û��ѡ�ϵĿγ�
#########################
print('�ҿ�ʼ�����Զ�ˢ����!')
courseLish = []
pattern = re.compile(r'\" onclick=\"selectThis\(\'.*\'')
#pattern = re.compile(r'selectThis')
pos=0
m=pattern.search(text,pos)
while m:
    pos=m.end()
    tempText = m.group()
    id1 = tempText[23:31]       #��һ�����
    id2 = tempText[34:51]       #�ڶ������
    id3 = tempText[54:56]       #���������
    course = [id1,id2,id3,1]
    courseLish.append(course)
    m=pattern.search(text,pos)  #Ѱ����һ��

times = 0
success = 0
while True:
    times = times+1
    print "\n��"+str(times)+"��ѡ�Σ��Ѿ��ɹ�ѡ��"+str(success)+"��"

    for course in courseLish:     
        if course[3] == 1:
            back = postXuan(course)       #����ѡ�ΰ�
            flag = stateCheck(back)
            if 0 == flag:
                course[3] = 0
                success = success+1
                print '�γ�'+str(course[0])+" ѡ��ɹ�"
            if 1 == flag:
                print '�γ�'+str(course[0])+" ��������"
            if 2 == flag:
                print '�γ�'+str(course[0])+" ѡ��ʧ�ܣ�ԭ��δ֪"
        time.sleep(sleepTime)


       



