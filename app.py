# импортируем все необходимые модули
from flask import Flask, render_template, redirect, request, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import os

from data import db_session
from data.users import User
from forms.user import RegisterForm, LoginForm

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


# создаем функцию для добавления ползователя в БД
@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


# создаем функцию для выхода из аккаунта
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


# создаем функцию для запуска приложения
def main():
    port = int(os.environ.get("PORT", 5000))
    db_session.global_init("blogs.db")
    app.run(host='0.0.0.0', port=port)


# создаем функцию для главной страницы приложения
@app.route("/")
def index():
    return render_template("index.html")


# создаем функцию для страницы регистрации приложения
@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


# создаем функцию для страницы входа приложения
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template('login.html', title='Авторизация', form=form)


# создаем функцию для страницы профиля приложения
@app.route('/profile')
def profile():
    return render_template("profile.html")


# создаем функции для страниц разделов приложения
@app.route('/Bird')
def bird():
    return render_template("design/Bird.html")


@app.route('/Meet')
def meet():
    return render_template("design/Meet.html")


@app.route('/Fish')
def fish():
    return render_template("design/Fish.html")


@app.route('/Soups')
def soups():
    return render_template("design/Soups.html")


@app.route('/Salads')
def salads():
    return render_template("design/Salats.html")


@app.route('/Desserts')
def desserts():
    return render_template("design/Desserts.html")


@app.route('/Cocktail')
def cocktails():
    return render_template("design/Cocktails.html")


# создаем функции для страниц рецептов приложения
@app.route('/meet1')
def meet1():
    return render_template("meet/meet_res_1.html")


@app.route('/meet2')
def meet2():
    return render_template("meet/meet_res_2.html")


@app.route('/meet3')
def meet3():
    return render_template("meet/meet_res_3.html")


@app.route('/meet4')
def meet4():
    return render_template("meet/meet_res_4.html")


@app.route('/meet5')
def meet5():
    return render_template("meet/meet_res_5.html")


@app.route('/meet6')
def meet6():
    return render_template("meet/meet_res_6.html")


@app.route('/bird1')
def Bird1():
    return render_template("bird/bird_res_1.html")


@app.route('/bird2')
def Bird2():
    return render_template("bird/bird_res_2.html")


@app.route('/bird3')
def bird3():
    return render_template("bird/bird_res_3.html")


@app.route('/bird4')
def bird4():
    return render_template("bird/bird_res_4.html")


@app.route('/bird5')
def bird5():
    return render_template("bird/bird_res_5.html")


@app.route('/bird6')
def bird6():
    return render_template("bird/bird_res_6.html")


@app.route('/fish1')
def fish1():
    return render_template("fish/fish_res_1.html")


@app.route('/fish2')
def fish2():
    return render_template("fish/fish_res_2.html")


@app.route('/fish3')
def Fish3():
    return render_template("fish/fish_res_3.html")


@app.route('/fish4')
def fish4():
    return render_template("fish/fish_res_4.html")


@app.route('/fish5')
def fish5():
    return render_template("fish/fish_res_5.html")


@app.route('/fish6')
def fish6():
    return render_template("fish/fish_res_6.html")


@app.route('/soup1')
def soup1():
    return render_template("soup/soup_res_1.html")


@app.route('/soup2')
def soup2():
    return render_template("soup/soup_res_2.html")


@app.route('/soup3')
def soup3():
    return render_template("soup/soup_res_3.html")


@app.route('/soup4')
def soup4():
    return render_template("soup/soup_res_4.html")


@app.route('/soup5')
def soup5():
    return render_template("soup/soup_res_5.html")


@app.route('/soup6')
def soup6():
    return render_template("soup/soup_res_6.html")


@app.route('/salad1')
def salad1():
    return render_template("salad/salad_res_1.html")


@app.route('/salad2')
def salad2():
    return render_template("salad/salad_res_2.html")


@app.route('/salad3')
def salad3():
    return render_template("salad/salad_res_3.html")


@app.route('/salad4')
def salad4():
    return render_template("salad/salad_res_4.html")


@app.route('/salad5')
def salad5():
    return render_template("salad/salad_res_5.html")


@app.route('/salad6')
def salad6():
    return render_template("salad/salad_res_6.html")


@app.route('/dessert1')
def dessert1():
    return render_template("dessert/dessert_res_1.html")


@app.route('/dessert2')
def dessert2():
    return render_template("dessert/dessert_res_2.html")


@app.route('/dessert3')
def dessert3():
    return render_template("dessert/dessert_res_3.html")


@app.route('/dessert4')
def dessert4():
    return render_template("dessert/dessert_res_4.html")


@app.route('/dessert5')
def dessert5():
    return render_template("dessert/dessert_res_5.html")


@app.route('/dessert6')
def dessert6():
    return render_template("dessert/dessert_res_6.html")


@app.route('/cocktail1')
def cocktail1():
    return render_template("cocktail/cocktail_res_1.html")


@app.route('/cocktail2')
def cocktail2():
    return render_template("cocktail/cocktail_res_2.html")


@app.route('/cocktail3')
def cocktail3():
    return render_template("cocktail/cocktail_res_3.html")


@app.route('/cocktail4')
def cocktail4():
    return render_template("cocktail/cocktail_res_4.html")


@app.route('/cocktail5')
def cocktail5():
    return render_template("cocktail/cocktail_res_5.html")


@app.route('/cocktail6')
def cocktail6():
    return render_template("cocktail/cocktail_res_6.html")


if __name__ == '__main__':
    main()
