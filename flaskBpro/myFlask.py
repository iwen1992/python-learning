from flask import Flask,render_template,request
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')#render_template会自动找templates文件夹里面的
@app.route("/pic")
def pic():
    picName = "这是一个flask变量"
    lst = ['李元芳','刘备','刘婵','赵云']
    return render_template('pictrue.html',name=picName,lst=lst)
@app.route("/login",methods=['post'])
def login():
    username = request.form.get('username')
    pwd = request.form.get('pwd')
    if(username=='iwen' and pwd=='123456'):
        return render_template("index.html")
    else:
        return render_template("pictrue.html")
if __name__ == '__main__':#固定写法 程序入口
    app.run(debug=True)