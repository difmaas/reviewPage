from flask import Flask,render_template,request,flash,redirect,url_for
from models import db,Review
import os

app = Flask(__name__)
app.secret_key = "rahasia"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///review.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
    
        nama   = request.form.get("nama")
        rating = request.form.get("rating")
        ulasan = request.form.get("ulasan")
        if not rating:
            return render_template("index.html", form=request.form, error="Belum ada ulasan.")
        review_baru = Review(nama=nama, rating=rating, ulasan=ulasan)
        db.session.add(review_baru)
        db.session.commit()

        flash("Ulasan berhasil dikirim!", "success")
        return redirect(url_for("index"))  
    
    return render_template("index.html", form={}, success=False)

@app.route('/admin/')
def admin():
    reviews = Review.query.all()
    return render_template("admin.html", reviews=reviews)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
