#coding:utf-8

from wsgiref.simple_server import make_server
from hello_WSGI import application
from hello_WSGI import application02
from time import sleep

from simple_WSGI.hello_WSGI import mApplication

httpd = make_server('',8000,mApplication);
httpd.serve_forever();
sleep(60)
httpd.server_close();