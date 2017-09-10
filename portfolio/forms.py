from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, \
	validators, FileField


class ContactForm(FlaskForm):
    """
    class with the blueprint in which the contact form will be derived from
    """
    name = StringField('First & Last Name:', [validators.DataRequired(message =
                                                                      "What is "
                                                                      "your "
                                                                      "First "
                                                                      "and Last "
                                                                      "name?"
                                                                      "")])
    phone = IntegerField('Phone Number:', [validators.DataRequired(message =
                                                                   "Kindly "
                                                                   "leave your "
                                                                   "phone number"
                                                                   "")])
    email = StringField('Email Address:', [validators.DataRequired(message =
                                                                   "Leave your "
                                                                   "email to "
                                                                   "contact you"),
                                            validators.Email("your@email.com")])
    message = TextAreaField('Your message:', [validators.DataRequired("How can "
                                                                      "we "
                                                                      "assist "
                                                                      "you?"
                                                                      "")])
    proposal = FileField('Proposal')
    submit = SubmitField('Send Message')
