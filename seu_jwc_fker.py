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


def loginIn(userName,passWord):
    print "��¼��"
    #����cookie������
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
    urllib2.install_opener(opener)  
    #��ѡ��ҳ��
    h = urllib2.urlopen('http://xk.urp.seu.edu.cn/') 
    #��ȡ��֤��
    image = urllib2.urlopen('http://xk.urp.seu.edu.cn/jw_css/getCheckCode')
    f = open('code.jpg','wb')
    f.write(image.read())
    f.close()
    #��ȡ��֤��
    code = raw_input('���������Ŀ¼�µ�code.jpg���������������������λ����\n')
    #����post����
    posturl = 'http://xk.urp.seu.edu.cn/jw_css/system/login.action' 
    header ={   
                'Host' : 'xk.urp.seu.edu.cn',   
                'Proxy-Connection' : 'keep-alive',
                'Origin' : 'http://xk.urp.seu.edu.cn',
                'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
                'Referer' : 'http://xk.urp.seu.edu.cn/jw_css/system/login.action'
                }
    data = {
            'userId' : userName,
            'userPassword' : passWord, #������룬  
            'checkCode' : code,           #��֤�� 
            'x' : '33',     #���
            'y' : '5'       #���2
            }
            
    #post��¼����
    text = postData(posturl,header,data)
    print "��¼�ɹ�"
    return text

def selectSemester(semesterNum):
    print "�������\"��������\"��ʾ����˯���룬Ȼ��ѡ��ѧ��"
    time.sleep(6)
    #����ѡ��ѧ�ڵİ�
    geturl ='http://xk.urp.seu.edu.cn/jw_css/xk/runXnXqmainSelectClassAction.action?Wv3opdZQ89ghgdSSg9FsgG49koguSd2fRVsfweSUj=Q89ghgdSSg9FsgG49koguSd2fRVs&selectXn=2014&selectXq='+str(semesterNum)+'&selectTime=2014-05-30%2013:30~2014-06-07%2023:59'
    header = {  'Host' : 'xk.urp.seu.edu.cn',
                'Proxy-Connection' : 'keep-alive',
                'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',        
    }
    data = {}
    #get��ȡѧ�ڿγ�
    text = getData(geturl,header,data)
    return text

def postData(posturl,headers,postData):
    postData = urllib.urlencode(postData)  #Post���ݱ���   
    request = urllib2.Request(posturl, postData, headers)#ͨ��urllib2�ṩ��request��������ָ��Url�������ǹ�������ݣ�����ɵ�¼���� 
    response = urllib2.urlopen(request)  
    text = response.read().decode('utf-8')
    return text

def getData(geturl,header,getData):
    getData = urllib.urlencode(getData)
    request = urllib2.Request(geturl, getData, header)
    response = urllib2.urlopen(request)
    text = response.read().decode('utf-8') 
    return text

def stateCheck(text):    
    if (text.find(u'�ɹ�ѡ��') != -1)or(text.find(u'�����Ƽ�') != -1):
        return 0
    if text.find(u'����') != -1:
        return 1
    if text.find(u'ʧ��') != -1:
        return 2

def Mode1(semesterNum):
    s =  semesterNum
    text = selectSemester(s)
    #Ѱ�ҿ��ԡ������Ƽ����Ŀγ�
    print "==============\nģʽ1����ʼѡ��\n=============="
    courseList = []
    pattern = re.compile(r'\" onclick=\"selectThis\(\'.*\'')
    pos = 0
    m = pattern.search(text,pos)
    while m:
        pos = m.end()
        tempText = m.group()
        course = [tempText[23:31],tempText[34:51],tempText[54:56],1]
        courseList.append(course)
        m=pattern.search(text,pos)  #Ѱ����һ��
    times = 0
    success = 0
    total = len(courseList)
    while True:
        if total == 0:
            break
        time.sleep(1)
        times = times +1
        print "\n��"+str(times)+"��ѡ�Σ��Ѿ��ɹ�ѡ��"+str(success)+"��"
        for course in courseList:
            if 1 == course[3]:
            #����ѡ��post
                posturl = 'http://xk.urp.seu.edu.cn/jw_css/xk/runSelectclassSelectionAction.action?select_jxbbh='+course[1]+'&select_xkkclx='+course[2]+'&select_jhkcdm='+course[0]
                headers = { 'Host' : 'xk.urp.seu.edu.cn',
                        'Proxy-Connection' : 'keep-alive',
                        'Content-Length' : '2',
                        'Accept' : 'application/json, text/javascript, */*',
                        'Origin':'http://xk.urp.seu.edu.cn',
                        'X-Requested-With': 'XMLHttpRequest',
                        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
                        }
                data = {'{}':''
                }
                #postѡ�ΰ�������ȡ����״̬
                flag = stateCheck(postData(posturl,headers,data))
                #����ѡ��״̬������Ϣ
                if 0 == flag:
                    course[3] = 0
                    success = success + 1
                    total = total - 1
                    print '�γ�'+str(course[0])+" ѡ��ɹ�"
                if 1 == flag:
                    print '�γ�'+str(course[0])+" ��������"
                if 2 == flag:
                    print '�γ�'+str(course[0])+" ѡ��ʧ�ܣ�ԭ��δ֪"
       

if __name__ == "__main__":
    print "��ѡ��ģʽ��"
    print "1. ֵֻ������������С������Ƽ����γ�"
    print "2. ֵֻ���ӽ��桰���ġ��͡���Ȼ���зֱ�����һ�ſγ�"
    print "3. ����ָ�������ſγ̵����ֲ�ֵ�أ��γ����Ͳ��ޣ�"
    mode = input('\n������ģʽ���(��:1)\n')
    userId = raw_input('������һ��ͨ��(��:213111111)\n')
    passWord = raw_input('����������(��:65535)\n')
    semester = input('������ѧ�ڱ��(��ѧ��Ϊ1����ѧ��Ϊ2)\n')
    if 1 == mode:
        loginIn(userId,passWord)
        Mode1(semester)