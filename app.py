from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Dummy user data for login
USER_DATA = {
    "user@example.com": "password123"
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check credentials
        if email in USER_DATA and USER_DATA[email] == password:
            return "Login Successful!"  # Placeholder for success
        else:
            flash('Invalid email or password')  # Show error message
            return redirect(url_for('login'))

    return render_template('login.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
