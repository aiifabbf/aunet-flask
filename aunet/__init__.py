#-*-coding:utf-8-*-
# 导入各扩展
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_restful import Api,Resource
import pymysql


app=Flask(__name__)#创建应用
app.config.from_object('config')#导入配置

# 实例化各扩展
db=SQLAlchemy(app)
api=Api(app)



lm=LoginManager()
lm.init_app(app)
lm.login_view='login'

mail=Mail(app)

#注册蓝图
from .Admin import admin
app.register_blueprint(admin,url_prefix='/admin')

from . import models,views

