from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Dummy data (in-memory)
users = []
projects = [
    {
        "title": "Bug Tracker",
        "description": "Track bugs in project",
        "manager": "Admin",
        "start": "2024-01-01",
        "deadline": "2024-12-31",
        "status": "NO"
    }
]

# ---------------- LOGIN ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        role = request.form.get("role")
        if role == "Admin":
            return redirect(url_for("admin"))
        else:
            return redirect(url_for("dashboard"))

    return render_template_string("""
    <h1>Bug Tracker Login</h1>
    <form method="POST">
        Username: <input type="text"><br><br>
        Password: <input type="password"><br><br>
        Role:
        <select name="role">
            <option>Admin</option>
            <option>Developer</option>
        </select><br><br>
        <button type="submit">Login</button>
    </form>
    <br>
    <a href="/signup">Sign Up</a>
    """)

# ---------------- SIGNUP ----------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        users.append({
            "username": request.form["username"],
            "email": request.form["email"]
        })
        return redirect(url_for("login"))

    return render_template_string("""
    <h1>Sign Up</h1>
    <form method="POST">
        Username: <input name="username"><br><br>
        Email: <input name="email"><br><br>
        <button type="submit">Create Account</button>
    </form>
    """)

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    return render_template_string("""
    <h1>User Dashboard</h1>
    <a href="/projects">View Projects</a><br><br>
    <a href="/">Logout</a>
    """)

# ---------------- ADMIN ----------------
@app.route("/admin")
def admin():
    return render_template_string("""
    <h1>Admin Dashboard</h1>
    <a href="/projects">Manage Projects</a><br><br>
    <a href="/">Logout</a>
    """)

# ---------------- PROJECTS ----------------
@app.route("/projects")
def project_page():
    html = "<h1>Projects</h1><ul>"
    for p in projects:
        html += f"<li>{p['title']} - {p['status']}</li>"
    html += "</ul><br><a href='/'>Logout</a>"
    return html


# ---------------- RUN ----------------
if __name__ == "_main_":
    app.run(debug=True)