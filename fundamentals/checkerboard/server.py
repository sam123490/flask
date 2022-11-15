from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def part_one():
    return render_template('index.html', rows=8, columns=8, color_one='black', color_two='red')

@app.route('/<int:rows>')
def part_two(rows):
    return render_template('index.html', rows=rows, columns=8, color_one='black', color_two='red')

@app.route('/<int:rows>/<int:columns>')
def part_three(rows, columns):
    return render_template('index.html', rows=rows, columns=columns, color_one='black', color_two='red')

@app.route('/<int:rows>/<int:columns>/<color_one>')
def part_four(rows, columns, color_one):
    return render_template('index.html', rows=rows, columns=columns, color_one=color_one, color_two='red')

@app.route('/<int:rows>/<int:columns>/<color_one>/<color_two>')
def part_five(rows, columns, color_one, color_two):
    return render_template('index.html', rows=rows, columns=columns, color_one=color_one, color_two=color_two)

if __name__=="__main__":
    app.run(debug=True)