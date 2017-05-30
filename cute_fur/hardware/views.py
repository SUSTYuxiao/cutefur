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
#    if dict['box'] == 'ture':
#        return HttpResponse(content='true')
#    else:
#         return HttpResponse(content='false')
# return render(request, 'test_zpx.html')
    file = open('test.json', 'r')
    text = demjson.decode(file.read())
    print text['box']
#    print tttt
#    text =
#    file.close()
#    print text
    newt = str(text['box'])
    return HttpResponse(content = newt)

'''
    HOST = ''
    PORT = 8000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'socket created'

    s.bind((HOST, PORT))
    print 'socket bind complete'

    s.listen(10)
    print 'socket now listening'

    conn, addr = s.accept()
    date = 'true'
    conn.sendall(date)
    conn.close()
    s.close()
'''


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
        dict['box'] = request.GET.get('checkbox')
    elif request.POST:
        dict['name'] = request.POST.get('name')
        dict['minute'] = request.POST.get('minute')
        dict['box'] = request.POST.get('checkbox')
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

    return dict