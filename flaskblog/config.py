class Config:
    SECRET_KEY = '90ce5a417f49cf1c6c1a052e8604b233'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_USERNAME = '18801095270@163.com'
    MAIL_PASSWORD = 'ACLUTATAGPUINPHV'
    # 连接mysql
    HOST_NAME = 'localhost'
    PORT = '3306'
    DATA_BASE = 'flaskblog'
    DATA_BASE_USER_NAME = 'root'
    DATA_BASE_USER_PASSWORD = '123456'
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DATA_BASE_USER_NAME, DATA_BASE_USER_PASSWORD, HOST_NAME, PORT,DATA_BASE)
    SQLALCHEMY_DATABASE_URI = DB_URI