from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, \
	validators, FileField


class ContactForm(FlaskForm):
    """
    class with the blueprint in which the contact form will be derived from
    """
    name = StringField('First & Last Name:', [validators.DataRequired()])
    phone = IntegerField('Phone Number:', [validators.DataRequired(message =
                                                                   "Kindly "
                                                                   "leave your "
                                                                   "phone number"
                                                                   "")])
    email = StringField('Email Address:', [validators.DataRequired(),
                                            validators.Email("your@email.com")])
    subject = StringField('Subject:', [validators.DataRequired()])
    message = TextAreaField('Your message:', [validators.DataRequired("Message "
                                                                      "required")])
    proposal = FileField('Proposal')
    submit = SubmitField('Send Message')
