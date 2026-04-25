from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Message-te lo in-save-na tur list
messages = []

@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        name = request.form.get('name')
        msg = request.form.get('message')
        if name and msg:
            messages.append({'name': name, 'message': msg})
        return redirect(url_for('message'))
    return render_template('message.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
