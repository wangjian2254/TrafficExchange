#coding=utf-8
from django.http import HttpResponseRedirect, HttpResponse
from traffic.models import WebUri, WebSite

__author__ = '王健'

def getRenderUrl(request):
    if hasattr(request,'environ'):
        domain=request.environ['HTTP_REFERER']
    if hasattr(request,'META'):
        domain=request.META['HTTP_REFERER']

def toUrl(request):
    submiturl=getRenderUrl(request)
    tourl=request.GET.get('tourl','/')
    return HttpResponseRedirect(tourl)

def getLinkUrl(request):
    '''
    获取可跳转链接
    '''
    websiteid=request.GET.get('websiteid',0)
    if websiteid:
        website=WebSite.objects.get(pk=websiteid)

        webpagequery=WebUri.objects.exclude(website__in=WebSite.objects.filter(user=website.user))
        webpagequery=webpagequery.filter(is_check=True).filter(is_Pub=True)
        weburilist=[]
        for weburi in webpagequery[:5]:
            weburilist.append({'url':weburi.url,'title':weburi.title,'img_url':weburi.img_url})
    return HttpResponse()
def fromUrl(request):
    '''
    从被跳转的页面，发送数据。进行统计。
    效果不好。容易仿冒
    '''
    return HttpResponse()
    submiturl=getRenderUrl(request)
    fromurl=request.POST.get('fromurl')
    return HttpResponse()