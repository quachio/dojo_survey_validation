from flask import Flask, render_template, redirect, session
import re

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

