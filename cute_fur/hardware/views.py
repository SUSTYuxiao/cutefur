# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import loader,context
from django.http import HttpResponse
from hardware.models import Hardware
import socket

# Create your views here.
import demjson

def test(request):
	html = loader.get_template('test.html')
	hd = Hardware.objects.get(name_id = 'test')
	if hd.state == True:
		c = context({'id' : 'true'})
	else:
		c = context({'id' : 'false'})
	html = html.render(c)
	return HttpResponse(html)

def test_zpx(request):
    # return render(request, 'test_zpx.html')
    HOST = ''
    POST = 8000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'socket created'

    s.bind((HOST, POST))
    print 'socket bind complete'

    s.listen(10)
    print 'socket now listening'

    conn, addr = s.accept()

    print 111

def index(request):
	# html = loader.get_template('index.html')
	# c = context({'name' : '智能家电-1'})
	# html = html.render(c)
	# return HttpResponse(html)
    return render(request, 'index.html', {'name': '智能家电中心'})

def calendar(request):
	# html = loader.get_template('calendar.html')
	# c = context({})
	# html = html.render(c)
	#return HttpResponse(html)
    return render(request, 'calendar.html')

def media(request):
	# html = loader.get_template('media.html')
	# c = context({})
	# html = html.render(c)
	# return HttpResponse(html)
    return render(request, 'midia.html', {})

def post_test(request):

    dict = {}
    if request.GET:
        dict['name'] = request.GET.get('name')
        dict['minute'] = request.GET.get('minute')
    elif request.POST:
        dict['name'] = request.POST.get('name')
        dict['minute'] = request.POST.get('minute')
    file = open('test.json', 'w')
    json = demjson.encode(dict)
    file.write(str(json))
    file.close()

	# html = loader.get_template('index.html')
	# c = context({'name' : '智能家电-1'})
	# html = html.render(c)
	# return HttpResponse(html)
    return render(request, 'index.html', dict)


def test(request):

    return dict