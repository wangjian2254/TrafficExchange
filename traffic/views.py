#coding=utf-8
# Create your views here.
import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.context import RequestContext
from TrafficExchange.traffic.tools import custom_render_to_response,WARN,SUCCESS,MSG,RESULT
from traffic.models import WebSite, Event

ADD_EVENT=1
CHANGE_EVENT=2
DEL_EVENT=3


def index(request):
    return custom_render_to_response(request,'index.html',{},RequestContext(request))

@login_required
def getCode(request):
    return custom_render_to_response(request,'getCode.html',{},RequestContext(request))

@login_required
def addWebSite(request):
    return custom_render_to_response(request,'WebSite.html',{},RequestContext(request))
@login_required
def saveWebSite(request):
    weburl=request.POST.get('domain','')
    weburl=weburl.replace('http://','')
    weburl=weburl.replace('/','')
    if 0==WebSite.objects.filter(domain=weburl).count():
        import hashlib
        filename=hashlib.md5(datetime.datetime.utcnow().strftime("%y-%m-%d")).hexdigest().lower()
        text=hashlib.md5(filename).hexdigest().lower()

        return custom_render_to_response(request,'checkWebSite.html',{'weburl':weburl,'filename':filename[:10],'text':text},RequestContext(request))
    else:
        request.session[RESULT]=WARN
        request.session[MSG]=u'网站已经存在。'
        return custom_render_to_response(request,'WebSite.html',{},RequestContext(request))
@login_required
def checkWebSite(request):
    import  urllib2
    weburl=request.POST.get('domain','')
    weburl=weburl.replace('http://','')
    weburl=weburl.replace('/','')
    import hashlib
    filename=hashlib.md5(datetime.datetime.utcnow().strftime("%y-%m-%d")).hexdigest().lower()
    text=hashlib.md5(filename).hexdigest().lower()
    try:
        u=urllib2.urlopen(weburl+filename[:10]+'.txt')
        html=u.read()
    except Exception,e:
        html=''
    if text==html:
        if 0==WebSite.objects.filter(domain=weburl).count():
            website=WebSite()
            website.domain=weburl
            website.user=request.user
            website.save()
            event=Event()
            event.user=website.user
            event.website=website
            event.object_repr=str(website)
            event.action_flag=ADD_EVENT
            event.old_status=website.is_check
            event.change_message=u'新添加的网站'
            event.event_object=website
            event.save()
            return custom_render_to_response(request,'addWebSiteSuccess.html',{'weburl':weburl},RequestContext(request))
        else:
            request.session[RESULT]=WARN
            request.session[MSG]=u'网站已经存在。'
            return custom_render_to_response(request,'checkWebSite.html',{'weburl':weburl,'filename':filename[:10],'text':text},RequestContext(request))
        #        request.session[RESULT]=SUCCESS
        #        request.session[MSG]=u'验证成功！请重继续操作。'
    request.session[RESULT]=WARN
    request.session[MSG]=u'验证失败！请重新再来。'
    return custom_render_to_response(request,'checkWebSite.html',{'weburl':weburl,'filename':filename[:10],'text':text},RequestContext(request))
@login_required
def dataAnalytics(request):
    return custom_render_to_response(request,'dataAnalytics.html',{},RequestContext(request))
@login_required
def trafficSettings(request):
    return custom_render_to_response(request,'trafficSettings.html',{},RequestContext(request))