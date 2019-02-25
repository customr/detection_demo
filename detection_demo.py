from app import app


app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=True)
