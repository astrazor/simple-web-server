from flask import Flask, render_template

app = Flask(__name__)

# Route for home page
@app.route('/')
def index():
     return render_template('index.html', page_title='Home page')

# Route for the "About Us" page
@app.route('/about')
def about():
     return render_template('about.html', page_title='About us')

# Route for the "Contacts" page
@app.route('/contact')
def contact():
     return render_template('contact.html', page_title='Contacts')

if __name__ == '__main__':
     app.run(debug=True)
