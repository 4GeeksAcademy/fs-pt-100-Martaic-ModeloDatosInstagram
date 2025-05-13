import os
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, User, Post, Comment, Media, Follower

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'super-secret')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

    admin = Admin(app, name='Instagram Clone Admin', template_mode='bootstrap3')

    # Registrar modelos en el panel de administración
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Post, db.session))
    admin.add_view(ModelView(Comment, db.session))
    admin.add_view(ModelView(Media, db.session))
    admin.add_view(ModelView(Follower, db.session))