from flask import Blueprint, Flask,render_template
import json,base64
import datetime,random,dateutil

def global_vars_templates(app:Flask):
    app.jinja_env.filters['b64encode'] = base64.b64encode
    app.jinja_env.filters['b64decode'] = base64.b64decode

    @app.context_processor
    def variaveis_globais():
        return dict(
                APP=app.config['APP'].upper(),
                LINK=app.config['LINK_COPYRIGHT'].upper(),
                now = datetime.datetime.now() ,
        )

    @app.template_filter('strftime')
    def _jinja2_filter_datetime(date, fmt=None):
        date = dateutil.parser.parse(date)
        native = date.replace(tzinfo=None)
        format='%d/%m/%Y, %H:%M:%S'
        return native.strftime(format)

    @app.template_filter('js_load')
    def _jinja2_filter_json_loads(data):
        return json.loads(data)