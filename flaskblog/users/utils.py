import os
import secrets

from PIL import Image
from flask import url_for,current_app
from flask_mail import Message

from flaskblog import  mail


def save_picture(form_picture):
    # genarate random hex key as new file name
    random_hex = secrets.token_hex(8)
    # get uploaded file name and file extensions
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    # message sender must be authorized, so keep it the same as mail user
    msg = Message('Password Reset Requeset', sender=current_app.config['MAIL_USERNAME'], recipients=[user.email])
    msg.body = f'''
        To reset your password, visit the following link:{url_for('users.reset_token', token=token, _external=True)}
        If you did not make this request then simply ignore this email and no change has set.
    '''
    mail.send(msg)
