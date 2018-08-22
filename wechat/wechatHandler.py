from . import *

wechat_handler_bp = Blueprint('wechat_handler_bp',
                              __name__,
                              url_prefix='/wechat',
                              static_folder='../static',
                              template_folder='../templates'
                              )
@wechat_handler_bp.route('/')
def index():
    return render_template('wechat_index.html')