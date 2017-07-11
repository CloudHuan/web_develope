#coding:utf-8

u'''
environ是一个dict，用例接收http的请求信息
start_response是一个函数，用来发送http响应
'''
def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')]);
    return ['<h1>hello world!!!</h1>'];

#这里学到了：or竟然可以设置默认值，厉害了
def application02(environ,start_response):
    start_response('200 OK',[('ContentType','text/html')]);
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:])
    return [body.encode('utf-8')]