#coding:utf-8

from flask import Flask,render_template
from flask import Request
'''
步骤：
新建app.py，用flask框架处理WSCI接口请求
安装jinja2，使用模板完成web app编写
'''

app = Flask(__name__);

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html');

@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('signin.html')

@app.route('/signin',methods=['POST'])
def signin():
    #name = Request.form("user");
    #psw = Request.form('psw');
    #print 'ok'
    #if name == "admin" and psw == "admin":
    return render_template('signin_ok.html',user="test");
    #return render_template('signin_ok.html',Msg='bad user or passworld!!!');

if __name__ == '__main__':
    app.run();