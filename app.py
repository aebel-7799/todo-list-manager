from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET'])
def home():
    search = request.args.get('search', '')
    if search:
        filtered = [t for t in tasks if search.lower() in t.lower()]
    else:
        filtered = tasks
    return render_template('home.html', tasks=filtered, search=search)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    if task:
        tasks.append(task)
    return redirect(url_for('home'))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        tasks[id] = request.form['task']
        return redirect(url_for('home'))
    return render_template('update.html', task=tasks[id], id=id)

@app.route('/delete/<int:id>')
def delete(id):
    tasks.pop(id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
