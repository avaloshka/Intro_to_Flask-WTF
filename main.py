from flask import Flask, render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, AnyOf

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
app.config['RECAPTCHA_PUBLIC_KEY'] = "6LcSx7kcAAAAAE-Fwfi4pL_A2yZX-CEmdBZpC6u0"
app.config['RECAPTCHA_PRIVATE_KEY'] = "6LcSx7kcAAAAAD0U9YhIYRFXwZV6cbiEbsmV54IL"
app.config['TESTING'] = True


class LoginForm(FlaskForm):
    username = StringField("username", [InputRequired(message="A username is required"), Length(min=5, max=10, message="Must be between 5 and 10 characters")])
    password = PasswordField("password", [InputRequired(message="A password is required"), AnyOf(values=['mypassword', 'myanotherpassword'])])
    recaptcha = RecaptchaField()


@app.route("/", methods=['GET', 'POST'])
def form():
    form = LoginForm()

    if form.validate_on_submit():
        return '<h1>The username is {}. the password is {}.'.format(form.username.data, form.password.data)
    return render_template("form.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
