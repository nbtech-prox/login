from os import name
from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Email

# Criando a aplicação Flask
app = Flask(__name__)
app.config['SECRET_KEY']='abc123abc'

class RegisterForm(FlaskForm):
    first_name = StringField('Primeiro nome', validators=[DataRequired()])
    second_name = StringField('Apelido', validators=[DataRequired()])
    email = StringField('E-mail', validators=[Email(message='E-mail inválido!')])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm', message='A password devem ser iguais.')])
    confirm = PasswordField('Corfime a Password')
    submit = SubmitField('REGISTRAR')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegisterForm()

    if form.validate_on_submit():
       return redirect('/registrado')

    return render_template('index.html', form=form)
@app.route('/registrado')
def registrado():
    return render_template('registrado.html', name='Nuno Batista')

# Executando o servidor
if __name__ == '__main__':
    app.run(debug=True, port=5152)
