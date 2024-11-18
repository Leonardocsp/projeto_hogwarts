from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import db, User
from views import bp as views_bp 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name') 
        email = request.form.get('email')
        password = request.form.get('password')

        new_user = User(name=name, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        flash('Registro realizado com sucesso!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')  
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()  

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        
        flash('Login inválido!', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
@login_required
def index():
    return render_template('index.html')

app.register_blueprint(views_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
