#coding=utf-8
# Create your views here.
from TrafficExchange.traffic.tools import custom_render_to_response


def index(request):
    return custom_render_to_response(request,'index.html',{})


def getCode(request):
    return custom_render_to_response(request,'getCode.html',{})

def addWebSite(request):
    return custom_render_to_response(request,'WebSite.html',{})

def saveWebSite(request):
    return custom_render_to_response(request,'checkWebSite.html',{})

def checkWebSite(request):
    return custom_render_to_response(request,'addWebSiteSuccess.html',{})

def dataAnalytics(request):
    return custom_render_to_response(request,'addWebSite.html',{})

def trafficSettings(request):
    return custom_render_to_response(request,'addWebSite.html',{})