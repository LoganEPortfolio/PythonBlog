from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, URL, Email, EqualTo, InputRequired
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterUser(FlaskForm):
    name = StringField('Name', validators=[DataRequired('This is required.')])
    email = StringField('Email', validators=[DataRequired('This is required.'), Email('Must be an email address.')])
    password = PasswordField('Password', validators=[InputRequired(), DataRequired('This is required'), EqualTo('confirm', message='Passwords must match.')])
    confirm = PasswordField('Confirm Password', validators=[DataRequired('This is required.'), EqualTo('password', message='Passwords must match')])
    submit = SubmitField("Submit")

# TODO: Create a LoginForm to login existing users
class LoginUser(FlaskForm):
    email = StringField('Email', validators=[DataRequired('This is required.'), Email('Must be an email address.')])
    password = PasswordField('Password', validators=[DataRequired('This is required')])
    submit = SubmitField("Submit")



# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment:', validators=[DataRequired('This is required.')])
    submit = SubmitField("Add Comment")