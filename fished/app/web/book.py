from flask import jsonify, Blueprint,request
from search import isbn_or_key
from yushu import YuShuBook
# from . import web
web = Blueprint('web',__name__)
@web.route("/book/search/<q>/<page>")
def search(q,page):
    q = request.args['q']#args是dict字典子类
    page = request.args['page']
    isbnOrKey = isbn_or_key(q)
    if isbnOrKey == "isbn":
        #alt+enter自动导入
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    # return json.dumps(result),200,{"content-type":"application/json"}
    return jsonify(result)
