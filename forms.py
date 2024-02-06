from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField,PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterForms(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    email = EmailField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit_register = SubmitField(label="Register")


# TODO: Create a LoginForm to login existing users
class LoginForms(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit_register = SubmitField(label="Login")


# TODO: Create a CommentForm so users can leave comments below posts
class CommentForms(FlaskForm):
    comment_body = CKEditorField("Comment", validators=[DataRequired()])
    submit_comment = SubmitField(label="Submit")


class ContactForms(FlaskForm):
    name = StringField(label="Name:", validators=[DataRequired()])
    email = EmailField(label="Your email:", validators=[DataRequired()])
    subject = StringField(label="Subject:", validators=[DataRequired()])
    message = CKEditorField(label="Message:", validators=[DataRequired()])
    to = StringField(label="To:", render_kw={"read_only": True})
    submit_Contact = SubmitField(label="Submit")
