from flask import Flask , render_template, url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class UserDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname= db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return '<UserDetails %r>' % self.id






@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        message = request.form.get('message')
        new_contact = UserDetails(email=email,firstname=firstname,lastname=lastname,message=message)
        
        db.session.add(new_contact)
        db.session.commit()
        
        return redirect(url_for('home'))



    return render_template('contact.html')






if __name__ == "__main__":
    app.run(debug=True)