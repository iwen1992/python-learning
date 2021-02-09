from flask import Flask
from app import create_app
app = create_app()
def index():
    return "this is indexPage"
if __name__ == '__main__':
    app.run(host="127.0.0.1",debug=app.config['DEBUG'])

