from flask import Flask ,render_template ,request
import sqlite3
app=Flask(__name__)

def get_db():
    conn =sqlite3.connect("cafe.db")
    conn.row_factory=sqlite3.Row
    return conn



users = [
    {'id': 1, 'username': 'Mohamed', 'age': 21, 'email': 'test@test.com', 'password': 'pass1'},
    {'id': 2, 'username': 'Ammar', 'age': 15, 'email': 'test2@test.com', 'password': 'pass2'},
    {'id': 3, 'username': 'Hamza', 'age': 14, 'email': 'test3@test.com', 'password': 'pass3'},
]


@app.route("/")
def index():
    database=get_db()
    cursor=database.cursor()
    cursor.execute("SELECT * FROM food_menu")
    foodmenu=cursor.fetchall()
    database.close()
    return render_template("cafe.html", users=users, foodmenu=foodmenu)

@app.route("/admin/addfood")
def admin ():
    return render_template("adminfood.html")




@app.route("/admin/addFood", methods=["GET", "POST"])
def addFood():
    print(request.method)

    if request.method == "GET":
        return render_template("adminFood.html")
    
    elif request.method == "POST":
        name = request.form['name'] 
        price = request.form['price']
        description = request.form['description']
        image_url = request.form['image_url']

        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'INSERT INTO food_menu (name, price, description, image_url) VALUES (?, ?, ?, ?)',
            (name, price, description, image_url)
        )

        db.commit()
        db.close()
        return "Food added successfully!"
@app.route("/admin/foodlist")
def foodlist ():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM food_menu")
        foodmenu=cursor.fetchall()
        db.close()
        return render_template ("Foodlist.html", foodmenu=foodmenu)

@app.route("/admin/deletefood/<int:foodid>")
def delete (foodid):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM food_menu WHERE id = ? ",[foodid])
        db.commit()
        db.close()
        return ("delete is maked sussfully")
if __name__=="__main__":
    app.run(debug=True,port=5000)