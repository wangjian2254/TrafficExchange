#coding=utf-8
import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.




#class SiteUser(models.Model):
#    user=models.OneToOneField(User,help_text=u'注册用户')

class Kind(models.Model):
    name=models.CharField(max_length=10,unique=True,help_text=u'内容类型')

    class Admin():
        pass
    class Meta():
        verbose_name=u'网站类型'
    def __unicode__(self):
        return self.name

class Style(models.Model):
    name=models.CharField(max_length=30,unique=True,help_text=u'展示风格，css 样式')

    class Admin():
        pass
    class Meta():
        verbose_name=u'展示样式'
    def __unicode__(self):
        return self.name

class WebSite(models.Model):
    domain=models.CharField(max_length=200,unique=True,help_text=u'网站域名，每个二级域名都算是一个')
    name=models.CharField(max_length=50,help_text=u'网站名称')
    admin=models.ForeignKey(User,help_text=u'隶属用户')
    is_action=models.BooleanField(default=True,help_text=u'是否正在使用')
    kinds=models.ManyToManyField(Kind,help_text=u'网站类型')
    is_check=models.BooleanField(default=True,help_text=u'是否通过审核')
    last_check_date=models.DateTimeField(default=datetime.datetime.now,help_text=u'最后一次审核时间')
    show_kinds=models.ManyToManyField(Kind,related_name='showkinds',blank=True,null=True,help_text=u'网站展示哪些类型的网站链接，白名单')
    not_show_kinds=models.ManyToManyField(Kind,related_name='notshowkinds',blank=True,null=True,help_text=u'网站不展示哪些类型的网站链接，黑名单')
    showed_kinds=models.ManyToManyField(Kind,related_name='beshowkinds',blank=True,null=True,help_text=u'网站被展示哪些类型的网站展示，白名单')
    not_showed_kinds=models.ManyToManyField(Kind,related_name='benotshowkinds',blank=True,null=True,help_text=u'网站不被展示哪些类型的网站展示，黑名单')

    class Admin():
        search_fields=['admin__username']
        pass
    class Meta():
        verbose_name=u'网站'
    def __unicode__(self):
        return u'%s-%s'%(self.domain,self.name)

class WebUri(models.Model):
    website=models.ForeignKey(WebSite,help_text=u'隶属网站')
    url=models.URLField(max_length=250,help_text=u'url链接')
    title=models.CharField(max_length=50,help_text=u'链接标题')
    img_url=models.URLField(max_length=250,blank=True,null=True,help_text=u'图片url')
    style=models.ForeignKey(Style,help_text=u'css样式')
    is_check=models.BooleanField(default=True,help_text=u'是否通过审核')
    last_check_date=models.DateTimeField(default=datetime.datetime.now,help_text=u'最后一次审核时间')
    is_Pub=models.BooleanField(default=False,help_text=u'是否发布')

    class Admin():
        search_fields=['website__name','website__domain']
        list_filter=['website']
        pass
    class Meta():
        verbose_name=u'链接'

    def __unicode__(self):
        return self.title

class CheckApply(models.Model):
    website=models.ForeignKey(WebSite,help_text=u'隶属网站')
    url=models.URLField(max_length=250,blank=True,null=True,help_text=u'url链接')
    create_date=models.DateTimeField(auto_created=True,help_text=u'申请创建时间')
    is_accept=models.BooleanField(default=False,help_text=u'是否受理')
    user=models.ForeignKey(User,help_text=u'申请人')

    class Admin():
        list_filter=['website']
        pass
    class Meta():
        verbose_name=u'审核申请'
    def __unicode__(self):
        return self.website.name
class CheckLog(models.Model):
    website=models.ForeignKey(WebSite,help_text=u'被审核的网站')
    weburi=models.ForeignKey(WebUri,blank=True,null=True,help_text=u'被审核的链接')
    checkapply=models.ForeignKey(CheckApply,blank=True,null=True,help_text=u'对应的审核申请')
    old_status=models.BooleanField(help_text=u'审核前状态')
    now_status=models.BooleanField(help_text=u'审核后状态')
    type=models.IntegerField(default=1,help_text=u'审核类型，1：常规审核，2：受理审核申请，3：抽查审核')
    bz=models.CharField(max_length=200,help_text=u'审核备注')
    user=models.ForeignKey(User,help_text=u'审核人')

    class Admin():
        search_fields=['website__name','website__domain']
        list_filter=['website']
        pass
    class Meta():
        verbose_name=u'审核日志'
    def __unicode__(self):
        return u'%s-%s'%(self.weburi.title,self.website.name)



