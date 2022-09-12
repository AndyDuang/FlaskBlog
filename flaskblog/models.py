from datetime import datetime, timedelta
from flaskblog import db, login_manager, app
from flask_login import UserMixin
from jose import jwt


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # 设置作者与博客之间的关联关系，lazy代表何时加载
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        expires_sec = datetime.utcnow() + timedelta(seconds=expires_sec)
        # exp: expire_time, iss: issuer(who generated the token)
        # aud: token receiver(target receiver)(once set, decode method must set an arg:audience=xxx)
        # iat: issue at (specific time)
        payload = {
            'exp': expires_sec,
            'iss': 'tjn',
            # 'aud': self.username,
            'iat': datetime.utcnow(),
            'user_id': self.id
        }
        return jwt.encode(claims=payload, key=app.config['SECRET_KEY'])

    @staticmethod
    def verify_reset_token(token):
        payload = jwt.decode(token, app.config['SECRET_KEY'])
        try:
            user_id = payload['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # 用户的id，外键关联
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"
