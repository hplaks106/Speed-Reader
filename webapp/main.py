from flask import Flask, redirect, url_for, render_template, request, session
import file_convert as conv
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, UploadSet

app = Flask(__name__)

app.config['SECRET_KEY'] = 'key'
app.config['UPLOADED_FILES_DEST'] = 'uploads/files'

files = UploadSet('files', ['pdf'])
configure_uploads(app, files)

class MyForm(FlaskForm):
    pdf  = FileField('pdf')

@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    form = MyForm()
    list = []
    if form.validate_on_submit():
        filename = files.save(form.pdf.data)
        list = conv.convert_pdf('uploads/files/' + filename)
    # else:
    #     return redirect('/')
    return render_template('home.html', form=form, list=list)

@app.route('/upload', methods=['POST', 'GET'])
def upload_files():

    return render_template('upload.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == "__main__":
    app.run(debug=True)
