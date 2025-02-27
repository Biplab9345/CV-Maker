from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for categories page
@app.route('/categories')
def categories():
    return render_template('categories.html')

# Route for template selection
@app.route('/templates/<category>')
def templates(category):
    return render_template('templates.html', category=category)

# Route for customization page
@app.route('/customize')
def customize():
    return render_template('customize.html')

if __name__ == '__main__':
    app.run(debug=True)
