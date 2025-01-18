import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
ICON_FOLDER = os.path.join(os.getcwd(), 'icons')
@app.route('/icons/<path:filename>')
def show_icon(filename):
    return send_from_directory(ICON_FOLDER, filename)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def page2():
    return render_template('dashboard.html')

@app.route('/clone')
def page3():
    return render_template('clone.html')

if __name__ == '__main__':
    app.run(debug=True, port=413)
