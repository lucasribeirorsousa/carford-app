from flask import Flask,jsonify,url_for,redirect,session,request,render_template,session
from ext.db import db
from flask_wtf.csrf import CSRFError
from flask_login import user_logged_in,user_logged_out,user_unauthorized,logout_user

def init_app(app:Flask):

    @app.errorhandler(CSRFError)
    def csrf_token(e):
        return redirect(url_for('security.login'))
    
    @app.errorhandler(404)
    @app.errorhandler(401)
    @app.errorhandler(403)
    def error(e):
        return render_template('errors/generic.html',error = e)

    @app.errorhandler(401)
    def error(e):
        return jsonify({'error':"401"}), 401

    @user_logged_in.connect_via(app)
    def on_user_logged_in(sender, user):

        pass

    @user_logged_out.connect_via(app)
    def on_user_logged_out(sender, user):
        session.pop('_id', None)