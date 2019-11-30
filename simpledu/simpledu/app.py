# Flask App 配置，创建相关代码
from flask import Flask, render_template
from simpledu.config import configs
from simpledu.models import db, Course

# 工厂函数
def create_app(config):
    #可以根据传入的config名称，加载不同的配置"""
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    # SQLALchemy 的初始化方式改为使用init_app
    db.init_app(app)

    #路由函数暂时写在这里，
    # 路由的模块化
    @app.route('/')
    def index():
        courses = Course.query.all()
        return render_template('index.html', courses=courses)

    @app.route('/admin')
    def admin_index():
        return 'admin'

    return app


