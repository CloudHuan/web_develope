#coding:utf-8

from flask import Flask
from flask import request

app = Flask(__name__);

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>i am home page</h1>';

@app.route('/login',methods=['GET'])
def login():
    body = '''
    <h1>please login</h1><br/>
    <form action='/signin.html' method='POST'>
    <input name='name' /><br/>
    <input name='password'type='password'/><br/>
    <input type='Submit'>
    </form>
    '''
    return body;

'''
别人家的内容
'''
@app.route('/signin.html', methods=['GET'])
def signin_form():
    return '''<form action="/signin.html" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

'''
demo
'''
@app.route('/signin.html', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run(port=8000);