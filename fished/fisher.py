from flask import Flask,make_response
from config import DEBUG#配置文件
# __author__ = "小夏"
# app = Flask(__name__)
#app.config.from_object('config')#导入配置文件，以这种方式导入规定读取必须都是大写如果写了小写将不读取
#不带斜杠访问，将会被重定向，加斜杠兼容用户在URL后面加斜杠
#路由注册
# @app.route('/hello/')
# def hello():
    #基于类的视图（即插视图）视图函数将会被flask解析、封装
    #封装后会返回status code、content-type、date、server
    # headers = {
    #     "content-type":"text/plain",
    #     "location":"http://www.baidu.com"#response code为301将被重定向
    # }
    # response = make_response("<html></html>",200)#404状态码并不会影像输出的内容
    # response.headers=headers
    # return response#建议写法 简易写法return "<html></html>",301,headers

    #return "hello 七月"
#第二种路由注册方法(即插视图时使用这个)
#app.add_url_rule("/hello",view_func=hello)
#debug=True自动重启 当设置debug=True不能被外网/局域网访问
#加host参数可以指定访问如果host为0.0.0.0则外网可以访问
#加port参数可以指定端口
# if __name__ == "__main__":#保证生产环境不执行flask自带的服务器 （nginx+uwsgi会加载模块启用服务）
    # app.run(debug=DEBUG,port=5000)
#以app.config.from_object('config')导入文件
# app.run(host="0.0.0.0",debug=app.config['DEBUG'],port=5001)