#coding=utf-8
from django.shortcuts import render_to_response
from django.template.context import RequestContext

__author__ = '王健'

RESULT='result'
MSG='msg'
SUCCESS='succeed'
WARN='warning'
def getSessionMsg(request,requestdic):
    requestdic[RESULT]=request.session.get(RESULT, '')
    requestdic[MSG]=request.session.get(MSG, '')
    if request.session.has_key(RESULT):
        del request.session[RESULT]
    if request.session.has_key(MSG):
        del request.session[MSG]
    if not requestdic[MSG]:
        del requestdic[MSG]
        del requestdic[RESULT]
    return requestdic

def custom_render_to_response(request,*args, **kwargs):
    getSessionMsg(request,args[1])
    return render_to_response(*args, **kwargs)