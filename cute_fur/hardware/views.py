# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import loader,context
from django.http import HttpResponse
from hardware.models import Hardware
from hardware.models import tjsj
import socket

# Create your views here.
import demjson
'''
def test(request):
	html = loader.get_template('test.html')
	hd = Hardware.objects.get(name_id = 'test')
	if hd.state == True:
		c = context({'id' : 'true'})
	else:
		c = context({'id' : 'false'})
	html = html.render(c)
	return HttpResponse(html)
'''
def test_zpx(request):
    file = open('test.json', 'r')
    text = demjson.decode(file.read())
    file.close()
    newt = str(text['box'])
    return HttpResponse(content = newt)


def dbcreate(request):
    temp = tjsj(name='zxtjsj')
    temp.save()
    return HttpResponse("<p>successful1</p>")

def dbset(request):
    ndata =tjsj.objects.get(pk='zxtjsj')
    ndata.ydl_data = request.GET.get('ydl')
    print ndata.ydl_data
    ndata.snwd_data = request.GET.get('snwd')
    ndata.snsd_data = request.GET.get('snsd')
    ndata.ysl_data = request.GET.get('ysl')
    ndata.save()
    return HttpResponse("successful1")

def index(request):
	# html = loader.get_template('index.html')
	# c = context({'name' : '智能家电-1'})
	# html = html.render(c)
    tj = tjsj.objects.get(pk='zxtjsj')
    print tj.ydl_data
    return render(request, 'index.html', {'name': '智能家电中心','tj': tj})

def calendar(request):
	# html = loader.get_template('calendar.html')
	# c = context({})
	# html = html.render(c)
    return render(request, 'calendar.html')

def media(request):
	# html = loader.get_template('media.html')
	# c = context({})
	# html = html.render(c)
    return render(request, 'media.html', {})

def post_test(request):

    dict = {}
    if request.GET:
        dict['name'] = request.GET.get('name')
        dict['minute'] = request.GET.get('minute')
        dict['hour'] = request.GET.get('hour')
        dict['box'] = request.GET.get('checkbox')
    elif request.POST:
        dict['name'] = request.POST.get('name')
        dict['minute'] = request.POST.get('minute')
        dict['hour'] = request.POST.get('hour')
        dict['box'] = request.POST.get('checkbox')
    # seconds=(int(str(dict['hour'])) * 60 + int((str(dict['minute']))))*60

    print dict['hour']
    print dict['minute']

    file = open('test.json', 'w')
    json = demjson.encode(dict)
    file.write(json)
    file.close()
    print 'text in jeso has been changed'

	# html = loader.get_template('index.html')
	# c = context({'name' : '智能家电-1'})
	# html = html.render(c)
	# return HttpResponse(html)
    return render(request, 'index.html', dict)


def test(request):
    tj = tjsj.objects.get(pk='zxtjsj')
    return render(request, 'test.html', {'tj': tj})