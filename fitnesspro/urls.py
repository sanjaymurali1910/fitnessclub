"""fitnesspro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path
from fitnessproapp import views

urlpatterns = [
    re_path('admin/', admin.site.urls),

    re_path(r'^$', views.index, name='index'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^classes/$', views.classes, name='classes'),
    re_path(r'^train/$', views.train, name='train'),
    re_path(r'^selecttrainer/$', views.selecttrainer, name='selecttrainer'),
    re_path(r'^startnow/$', views.startnow, name='startnow'),
    re_path(r'^shedule/$', views.shedule, name='shedule'),
    re_path(r'^contact/$', views.contact, name='contact'),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^join/$', views.join, name='join'),
    re_path(r'^userpaymentpage/$', views.userpaymentpage, name='userpaymentpage'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^online_training/$', views.online_training, name='online_training'),
    re_path(r'^offline_training/$', views.offline_training, name='offline_training'),
    re_path(r'^traindex/$', views.traindex, name='traindex'),
    # re_path(r'^addbutonline/$', views.addbutonline, name='addbutonline'),
    re_path(r'^onlin/$', views.onlin, name='onlin'),
    re_path(r'^onedit/(?P<i_id>[0-9]+)/$', views.onedit, name='onedit'),
    re_path(r'^onlineedit/(?P<oned_id>[0-9]+)/$', views.onlineedit, name='onlineedit'),
    re_path(r'^offlin/$', views.offlin, name='offlin'),
    re_path(r'^offedit/(?P<i_id>[0-9]+)/$', views.offedit, name='offedit'),
    re_path(r'^staffd/$', views.staffd, name='staffd'),
    re_path(r'^maint/$', views.maint, name='maint'),
    re_path(r'^admhome/$', views.admhome, name='admhome'),
    re_path(r'^admreg/$', views.admreg, name='admreg'),
    re_path(r'^admregedit/(?P<i_id>[0-9]+)/$', views.admregedit, name='admregedit'),
    re_path(r'^admregistration/(?P<reg_id>[0-9]+)/$', views.admregistration, name='admregistration'),
    re_path(r'^admintrainee/$', views.admintrainee, name='admintrainee'),
    re_path(r'^admintrainer/$', views.admintrainer, name='admintrainer'),
    re_path(r'^admintimetable/$', views.admintimetable, name='admintimetable'),
    re_path(r'^admin_view_timetable/$', views.admin_view_timetable, name='admin_view_timetable'),
    re_path(r'^admin_edit_timetable/(?P<i_id>[0-9]+)/$', views.admin_edit_timetable, name='admin_edit_timetable'),
    re_path(r'^admin_editpage/(?P<timet_id>[0-9]+)/$', views.admin_editpage, name='admin_editpage'),
    re_path(r'^delete_batch/(?P<p_id>[0-9]+)/$', views.delete_batch, name='delete_batch'),
    re_path(r'^admin_userpayment/$', views.admin_userpayment, name='admin_userpayment'),
    re_path(r'^admin_view_userpay/$', views.admin_view_userpay, name='admin_view_userpay'),
    re_path(r'^admin_payment/$', views.admin_payment, name='admin_payment'),
    re_path(r'^admin_pay_page/$', views.admin_pay_page, name='admin_pay_page'),
    


    


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

