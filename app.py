from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --------------------
# Routes
# --------------------

@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    message = None

    if request.method == "POST":
        username = request.form.get("username")

        # مؤقتًا (لاحقًا نربطه بـ Supabase)
        if username == "Anis":
            return redirect(url_for("categories"))
        else:
            message = "Access denied"

    return render_template("login.html", message=message)


@app.route("/categories")
def categories():
    categories_list = [
        {
            "name": "خضروات",
            "icon": "https://cdn-icons-png.flaticon.com/512/415/415733.png"
        },
        {
            "name": "إلكترونيات",
            "icon": "https://cdn-icons-png.flaticon.com/512/3659/3659899.png"
        },
        {
            "name": "مواد غذائية",
            "icon": "https://cdn-icons-png.flaticon.com/512/3075/3075977.png"
        },
        {
            "name": "ملابس",
            "icon": "https://cdn-icons-png.flaticon.com/512/892/892458.png"
        }
    ]

    return render_template("categories.html", categories=categories_list)


@app.route("/products/<category>")
def products(category):
    products_list = [
        {
            "name": "Tomato",
            "price": "2$",
            "category": "خضروات"
        },
        {
            "name": "Laptop",
            "price": "800$",
            "category": "إلكترونيات"
        }
    ]

    filtered = [p for p in products_list if p["category"] == category]
    return render_template("products.html", products=filtered, category=category)


# --------------------
# Run App (Render needs this)
# --------------------
if __name__ == "__main__":
    app.run()
