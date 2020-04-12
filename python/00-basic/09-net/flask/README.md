# Flask 

* https://github.com/greyli/flask-examples

## Hello

```
mac020:flask mac020$ pip3 install -U Flask
Requirement already up-to-date: Flask in /usr/local/lib/python3.7/site-packages (1.1.2)
Requirement already satisfied, skipping upgrade: click>=5.1 in /usr/local/lib/python3.7/site-packages (from Flask) (7.1.1)
Requirement already satisfied, skipping upgrade: Jinja2>=2.10.1 in /usr/local/lib/python3.7/site-packages (from Flask) (2.11.1)
Requirement already satisfied, skipping upgrade: itsdangerous>=0.24 in /usr/local/lib/python3.7/site-packages (from Flask) (1.1.0)
Requirement already satisfied, skipping upgrade: Werkzeug>=0.15 in /usr/local/lib/python3.7/site-packages (from Flask) (1.0.1)
Requirement already satisfied, skipping upgrade: MarkupSafe>=0.23 in /usr/local/lib/python3.7/site-packages (from Jinja2>=2.10.1->Flask) (1.1.1)
mac020:flask mac020$ env FLASK_APP=hello.py flask run
 * Serving Flask app "hello.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```