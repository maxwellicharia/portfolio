from flask import Flask, render_template, request
from flask_mail import Mail  # , Message
from portfolio.forms import ContactForm

# Instantiating a class from Flask called app
app = Flask(__name__)
app.secret_key = 'MySecreteKey'

# configuring the mail server
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'award.me@gmail.com'
app.config['MAIL_PASSWORD'] = 'maxwellaward?'

# config the file upload
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = {'txt', 'pdf'}

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
	elif request.method == 'POST':
		if not form.validate_on_submit():
			return render_template('index.html', form = form, not_valid = True)
		else:
			# msg = Message("Message from your potential client: " + form.name.data,
			# 	              sender = 'award.me001@gmail.com',
			# 	              recipients = ['maxwellicharia@gmail.com',
			# 	                            'fatmahilal2016.fh@gmail.com'])
			# msg.body = """
			# 			From: %s <%s>,
			#             %s
			#             %s
			#             %s
			#             %s
			#             """ \
			#            % (form.name.data, form.name.data, form.email.data,
			#               form.message.data, form.subject.data,
			#               form.proposal.data)
			# mail.send(msg)
			return render_template('index.html', form = form, good = True)
	else:
		return render_template('index.html', form = form, error = True)
