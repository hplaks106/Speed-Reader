from flask import Flask, redirect, url_for, render_template, request, session, flash
import file_convert as conv
from flask_wtf import FlaskForm
from wtforms import FileField, StringField
from flask_uploads import configure_uploads, UploadSet
from flask_mail import Mail, Message
from datetime import timedelta

mail = Mail()
app = Flask(__name__)
mail.init_app(app)
app.permanent_session_lifetime = timedelta(minutes=5)

app.config['SECRET_KEY'] = 'Key'
app.config['UPLOADED_FILES_DEST'] = 'uploads/files'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'speedreadercomments@gmail.com'
app.config['MAIL_PASSWORD'] = 'spam@1234'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

files = UploadSet('files', ['pdf'])
configure_uploads(app, files)

class PDFForm(FlaskForm):
    pdf  = FileField('pdf')


class EmailForm(FlaskForm):
    Name = StringField('Name')
    Email = StringField('Email')
    Message = StringField('Message')


def send_mail(name, sender, message):

    msg = Message(subject = f'About page comment, {str(name)}',
                  sender = 'speedreadercomments@gmail.com',
                  recipients = ['speedreadercomments@gmail.com'])

    msg.body = str(message) + f'Sent from {str(sender)}'
    mail.send(msg)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_files():
    form = PDFForm()
    filename = 'No file submitted...'
    if form.validate_on_submit():
        session.permanent = True
        filename = files.save(form.pdf.data)
        session['filename'] = filename
        return redirect(url_for('reader', filename=filename))
    else:
        return render_template('upload.html', form=form)



@app.route('/reader', methods=['GET', 'POST'])
def reader():
    if 'filename' in session:
        filename = session['filename']
        session['list'] = conv.readFile('uploads/files/' + filename)
    else:
        filename = 'No file selected...'

    if 'list' in session:
        list = session['list']
    else:
        list = ['Need', 'to', 'upload', 'a', 'file']

    return render_template('reader.html', list=list, filename=filename)

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    form = EmailForm()
    if form.validate_on_submit():
        name = form.Name
        email = form.Email
        message = form.Message
        send_mail(name, email, message)
        flash("Thanks!")
        return redirect(url_for('about'))
    else:
        flash("Something went wrong...")
        return render_template('about.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
