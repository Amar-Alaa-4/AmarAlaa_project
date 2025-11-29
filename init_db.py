import sqlite3
conn =sqlite3.connect("cafe.db")
cursor =conn.cursor()
#Conn =Connection
#Cursor =معناها موشر بالعربي  اسمها مش بيدل علي معناها 
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS food_menu (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT,
        image_url TEXT
    )
    """
)
foodMenu = [


    {
        'id': 1,
        'name': 'Strawberry Tarts',
        'price': 10.99,
        'description': 'Delicious strawberry tarts with a buttery crust and fresh strawberries on top.',
        'image_url': 'static/images/Strawberry-Tarts.png'
    },
    {
        'id': 2,
        'name': 'Cookies',
        'price': 5.99,
        'description': 'Classic chocolate chip cookies, crispy on the outside and chewy on the inside.',
        'image_url': 'static/images/Cookies.png'
    },
    {
        'id': 3,
        'name': 'Hot Chocolate',
        'price': 12.99,
        'description': 'Rich and creamy hot chocolate made with real cocoa and topped with whipped cream.',
        'image_url': 'static/images/Cup-of-Hot-Chocolate.png'
    },
    {
        'id': 4,
        'name': 'Strawberry & Blueberry Tarts',
        'price': 8.99,
        'description': 'Creamy vanilla ice cream with a smooth texture and a rich flavor.',
        'image_url': 'static/images/Strawberry-&-Blueberry-Tarts.png'
    },
    {
        'id': 5,
        'name': 'Coffee & Pastries',
        'price': 15.99,
        'description': 'Freshly brewed coffee served with a selection of assorted pastries.',
        'image_url': 'static/images/Coffee-and-Pastries.png'
    }
    ]
food_data = [(food["id"], food["name"], food["price"], food["description"], food["image_url"])
           for food in foodMenu
           #طريقه مختصره عشان تعمل loop  وتحول الي tuple
]
#ta اسم ال 
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """
)



users = [
    {'id': 1, 'username': 'Mohamed', 'age': 21, 'email': 'test@test.com', 'password': 'pass1'},
    {'id': 2, 'username': 'Ammar', 'age': 15, 'email': 'test2@test.com', 'password': 'pass2'},
    {'id': 3, 'username': 'Hamza', 'age': 14, 'email': 'test3@test.com', 'password': 'pass3'},
]
user_data=[(user["id"], user ["username"] ,user ["age"] ,user ["email"],user ["password"],  )
           for user  in users
           #طريقه مختصره عشان تعمل loop  وتحول الي tuple
]

cursor.executemany("INSERT INTO user VALUES  (?,?,?,?,?)",user_data)
print("Data base is  Created")

cursor.executemany("INSERT INTO food_menu VALUES (?,?,?,?,?)", food_data)
print("Data base Created")
















conn.commit()
conn.close()

