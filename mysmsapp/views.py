from django.http import HttpResponse# Create your views here.
from django.shortcuts import render
from django.contrib.auth import *
from django.contrib.auth.models import *
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from mysmsapp.models import *
import json,urllib2,cookielib,os
from traceback import format_exc

@csrf_exempt
def send_msg_from_user(request):
    print 'hii',eval(request.body)
    data = json.loads(request.body)
    print 'data',data
    try:
        if User.objects.filter(username=data['username']):
            user = User.objects.get(username=data['username'])
            push_user_msg = User_details.objects.create(uname=user,message=data['message'],send_to=data['to'])
            alert = send_messsage(data['username'],data['password'],data['to'],data['message']) 
        else:
            user = User.objects.create(username=data['username'],password=data['password'])
            push_user_msg = User_details.objects.create(uname=user,message=data['message'],send_to=data['to'])
            alert = send_messsage(data['username'],data[' password'],data[' to'],data[' message']) 
    except:
        print 'eoor',repr(format_exc())
    return HttpResponse(content = json.dumps(alert), content_type='Application/json')   


def send_messsage(username, passwd, number, message):
    url = 'http://site24.way2sms.com/Login1.action?'
    data = 'username=%s&password=%s&Submit=Sign+in' % (username, passwd)
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
    
    try:
        usock = opener.open(url, data)
    except IOError:
        msg = "Error while logging in."

    jession_id = str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token=%s&mobile=%s&message=%s&msgLen=136' % (jession_id, number, message)
    opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token=%s' % jession_id)]
    
    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
        msg = "success"
    except IOError:
        msg = "Error while sending message"
    return HttpResponse("msg")    

