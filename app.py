from flask import Flask, render_template, request
import requests
from urllib.parse import unquote
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import redirect, url_for
from flask import current_app


# Create the flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = '42448154008950706555520308666437'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://geoffreyhightower:Vivian2023@localhost:5432/recipeApp'

API_KEY = '1e82730f8331482bb88d67a0b737ce44'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
#User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    likes = db.Column(db.Integer, default=0)  # Field for tracking likes

# Recipe model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255))
    likes = db.Column(db.Integer, default=0)  # New field for tracking recipe likes


# Define the route for the "Home" button
@app.route('/home', methods=['GET'])
def home():
    # Render the main page with empty recipe list and search query
    return render_template('index.html', recipes=[], search_query='')

# Define the main route for the app
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # If a form is submitted
        query = request.form.get('search_query', '')
        # Perform a search for recipes with the given query
        recipes = search_recipes(query)
        # Render the main page with the search results and the search query
        return render_template('index.html', recipes=recipes, search_query=query)
    
    # If it's a GET request or no form submitted
    search_query = request.args.get('search_query', '')
    decoded_search_query = unquote(search_query)
    # Perform a search for recipes with the decoded search query
    recipes = search_recipes(decoded_search_query)
    # Render the main page
    return render_template('index.html', recipes=recipes, search_query=decoded_search_query)

# Function to search for recipes based on the provided query
def search_recipes(query):
    url = f'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': API_KEY,
        'query': query,
        'number': 10,
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }

    # Send a GET request to the Spoonacular API with the query parameters
    response = requests.get(url, params=params)
    # If the API call is successful
    if response.status_code == 200:
        # Parse the API response as JSON data
        data = response.json()
        # Return the list of recipe results
        return data['results']
    # If the API call is not successful
    return []

# Route to view a specific recipe with a given recipe ID
@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    # Get the search query from the URL query parameters
    search_query = request.args.get('search_query', '')
    # Build the URL to get information about the specific recipe ID from Spoonacular API
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    params = {
        'apiKey': API_KEY,
    }

    # Send a GET request to the Spoonacular API to get the recipe information
    response = requests.get(url, params=params)
    
    # If the API call is successful
    if response.status_code == 200:
        recipe = response.json()
        return render_template('view_recipe.html', recipe=recipe, search_query=search_query)
    
    # If the API call is not successful
    return "Recipe not found", 404  # Add this line if the API call fails

# Route to like recipe with recipe ID    
@app.route('/like_recipe/<int:recipe_id>', methods=['POST'])
def like_recipe(recipe_id):
    print("Entering like_recipe route")
#Attempt to receive recipe from DB using ID   
    try:
        recipe = Recipe.query.get_or_404(recipe_id)
        print(f"Recipe ID: {recipe.id}")
        #increments likes count by 1
        recipe.likes += 1
        db.session.commit()
        #if successful print message, of not print error
        print("Recipe liked successfully")
        return redirect(url_for('index'))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "Internal Server Error", 500


    # Send a GET request to the Spoonacular API to get the recipe information
    response = requests.get(url, params=params)
    # If the API call is successful
    if response.status_code == 200:
        recipe = response.json()
        return render_template('view_recipe.html', recipe=recipe, search_query=search_query)
    return "Recipe not found", 404

# Run the app in debug mode if executed directly
if __name__ == '__main__':
    app.run(debug=True)