from flask import Flask, render_template
import os
app = Flask(__name__)


@app.route('/')
def home_page():
    return app.send_static_file('yeet.html')

@app.route('/yeeting')
def yeet_page():
    return app.send_static_file('yeeting.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=int(os.environ.get('PORT', 8080)))
