from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField
from wtforms import validators


class UserForm(Form):

   user_id = HiddenField()

   user_name = StringField("Name: ",[
                                    validators.DataRequired("Please enter your name."),
                                    validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])


   user_email = StringField("Email: ",[
                                 validators.DataRequired("Please enter your name."),
                                 validators.Email("Wrong email format")
                                 ])

   user_birthday = DateField("Birthday: ", [ validators.DataRequired("Please enter your birthday.")])

   user_studybook = StringField("Study Book: ",[
                                             validators.DataRequired("Please enter your study book."),
                                             validators.Length(6,6,"6 symbols allowed")
                                          ])

   user_year = DateField("Study year: ", [ validators.DataRequired("Please enter your study year.")])


   submit = SubmitField("Save")


