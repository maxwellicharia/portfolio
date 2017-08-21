from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
from portfolio.forms import ContactForm

# Instantiating a class from Flask called app
app = Flask(__name__)
app.secret_key = 'MySecreteKey'

# configuring the mail server
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'maxwellicharia@gmail.com'
app.config['MAIL_PASSWORD'] = 'Marx 11an0 3830'

# initialising the Mail class to be used in app
mail = Mail(app)


@app.route('/', methods = ['GET', 'POST'])
def main():
	"""
	Main function to carry out all the backend communication
	"""
	form = ContactForm(request.form)
	if request.method == 'GET':
		return render_template('index.html', form = form)
	else:
		# if not form.validate_on_submit():
		# 	flash('Valid data required to submit')
		# 	return render_template('index.html', form = form)
		# else:
		try:
			f = request.files['file']
			f.save(secure_filename(f.filename))
			msg = Message("Message from your potential client: " + form.name.data,
			              sender = 'maxwellicharia@gmail.com',
			              recipients = ['maxwellicharia@gmail.com'])  # ,
			# 'fatmahilal2016.fh@gmail.com'])
			msg.body = """
			            From: %s <%s>,
			            %s %s %s
			        """ % (form.name.data, form.email.data, form.message.data,
			               form.subject.data, form.proposal.data)
			mail.send(msg)
			flash('Successfully sent message')
			return render_template('index.html', form = form)
		except:
			flash('An error occurred, try again')
			return render_template('index.html', form = form)
