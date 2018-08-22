from flask import Flask
from flask import render_template
from flask_script import Manager
from wechat.wechatHandler import wechat_handler_bp

app = Flask(__name__)
app.register_blueprint(wechat_handler_bp)
manager = Manager(app)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    manager.run()