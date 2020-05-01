from flask import Flask,url_for,request
from markupsafe import escape
from flask import render_template

app=Flask(__name__) # 代表目前執行的模組

@app.route("/") #函數的裝飾(Decorator)：以函式為基礎，提供附加的功能
def  home():
    return "Hello Flask"


@app.route("/test")#代表我們要處理的網站路徑
def test():
    return "This is test"


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


with app.test_request_context():
    print(url_for('home'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))



if  __name__=="__main__":#如果以主程式執行
        app.run() #立刻啟動伺服器
