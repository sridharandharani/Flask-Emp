from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def add_emp():
    return render_template("add_emp.html")

@app.route('/search')
def search():
    return render_template("search.html")

@app.route('/update')
def update():
    return render_template("update.html")

@app.route('/delete')
def delete():
    return render_template("delete.html")

if __name__ == "__main__":
    app.run()