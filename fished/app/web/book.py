from flask import jsonify, Blueprint
from search import isbn_or_key
from yushu import YuShuBook
web = Blueprint('web',__name__)
@web.route("/book/search/<q>/<page>")
def search(q,page):
    isbnOrKey = isbn_or_key(q)
    if isbnOrKey == "isbn":
        #alt+enter自动导入
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword((q))
    # return json.dumps(result),200,{"content-type":"application/json"}
    return jsonify(result)
