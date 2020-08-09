from flask import Flask, render_template, request, redirect, url_for, make_response, session

app = Flask(__name__)


@app.route('/')
def home():
    return "Home Page!"


@app.route('/login')
def login():
    return "Login Page!"


@app.route('/signup')
def signup():
    return "Signup Page!"


@app.route('/resetpassword')
def passwordreset():
    return "Password Reset page!"


@app.route('/profile')
def profile():
    return "My Profile Page!"


@app.route('/myprojects')
def myprojects():
    return "My Projects Page!"


@app.route('/upload')
def upload():
    return "Upload New Project Page!"


if __name__ == '__main__':
    app.run(debug=True)