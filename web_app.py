from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template.html')


@app.route('/js_test')
def js_test():
    return render_template('js_test.html')

if __name__ == '__main__':
    app.run()
