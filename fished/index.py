from flask import Flask
app = Flask(__name__)
app.config.from_object("config")
@app.route("/book/search")
def search(q,page):
    isbn_or_key = "key"
    if len(q) == 13 and q.isdigit():
        isbn_or_key="isbn"
    short_q = q.replace("-","");
    if "-" in q and len(short_q) and short_q.isdigit:#多个and条件，把最可能为假的放在前面
        isbn_or_key='isbn'
    pass
