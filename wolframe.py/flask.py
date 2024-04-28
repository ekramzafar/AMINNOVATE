from flask import Flask

app = Flask(index.html)

@app.route('/')  # Defines the route for the main page
def index():
    # Python code that generates dynamic content
    data = {'message': 'Hello from Flask!'}
    return render_template('index.html', data=data)  # Pass data to the template

if _/index.html== '_main_':
    app.run(debug=True)  # Runs the development server
