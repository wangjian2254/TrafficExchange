#coding=utf-8
from traffic.models import Kind,Style, WebSite, WebUri, CheckApply, CheckLog

__author__ = '王健'

from django.contrib import admin
admin.site.register(Kind)
admin.site.register(Style)
admin.site.register(WebSite)
admin.site.register(WebUri)
admin.site.register(CheckApply)
admin.site.register(CheckLog)
