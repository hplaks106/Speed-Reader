from flask import Flask, redirect, url_for, render_template, request, session
import file_convert as conv
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, UploadSet

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ThisKeyCanBeAnyString'
app.config['UPLOADED_FILES_DEST'] = 'uploads/files'

files = UploadSet('files', ['pdf'])
configure_uploads(app, files)

class MyForm(FlaskForm):
    pdf  = FileField('pdf')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_files():

    form = MyForm()
    list = []
    filename = 'No file submitted...'
    if form.validate_on_submit():
        filename = files.save(form.pdf.data)
        list = conv.convert_pdf('uploads/files/' + filename)

    return render_template('upload.html', form=form, list=list, filename=filename)

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == "__main__":
    app.run(debug=True)
