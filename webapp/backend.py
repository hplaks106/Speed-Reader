from flask import Flask, redirect, url_for, render_template
import file_convert as conv

app = Flask(__name__)


@app.route('/')
def home():
    # list = conv.convert_pdf_to_txt('Group_Assignment_4.pdf')
    return render_template('home.html', list=conv.readFile('Group_Assignment_4.pdf'))


@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == "__main__":
    app.run(debug=True)
