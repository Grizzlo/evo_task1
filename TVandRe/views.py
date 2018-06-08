from django.shortcuts import render,redirect
from TVandRe.models import TV,Refrigerator
from django.http import HttpResponse,HttpResponseRedirect


def index(request):
    return render(request,'index.html')

def tv_clicked(request, tv_id):
    tv = TV.objects.get(id=tv_id)
    tv.count_of_views += 1
    tv.save()
    tv_list = TV.objects.all()
    return render(request,'TV_page.html',{'TV':tv_list,'redirect':True,'tv_clicked':tv})

def tv(request):
    tv_list = TV.objects.all()
    return render(request,'TV_page.html',{'TV':tv_list,'redirect':False})

def tv_sorted(request):
    tv_list = TV.objects.order_by('count_of_views')
    return render(request,'TV_page.html',{'TV':tv_list,'redirect':False})

def re_clicked(request, re_id):
    re = Refrigerator.objects.get(id=re_id)
    re.count_of_views += 1
    re.save()
    refr_list = Refrigerator.objects.all()
    return render(request,'Re_page.html',{'refrigerator':refr_list,'redirect':True,'re_clicked':re})


def re_sorted(request):
    refr_list = Refrigerator.objects.order_by('count_of_views')
    return render(request,'Re_page.html',{'refrigerator':refr_list,'redirect':False})

def refrigirator(request,redirected=False):
    refr_list = Refrigerator.objects.all()
    return render(request,'Re_page.html',{'refrigerator':refr_list,'redirect':False})
