from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint("auth", __name__)

# 🚧 Temporary in-memory user (replace with Supabase later)
USERS = {
    "admin@example.com": {"password": "pass123", "name": "Admin"}
}

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        # Basic validation
        if not email or not password:
            flash("Email and password are required.", "error")
            return render_template("login.html", email=email)

        user = USERS.get(email)
        if not user or user["password"] != password:
            flash("Invalid email or password.", "error")
            return render_template("login.html", email=email)

        # Success: store minimal user info in session
        session["user"] = {"email": email, "name": user["name"]}
        flash(f"Welcome back, {user['name']}!", "success")
        return redirect(url_for("home"))

    # GET
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("home"))
