from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def index():
    return render_template('index.html')

@app.route("/k<book>")
def show_book(book):
    return render_template(f"k{book}.html")

if __name__ == "__main__":
    app.run(debug=True)