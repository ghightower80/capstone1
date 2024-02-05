API selection and Schema

For this application I have decided to use the Spoonacular API. The site is https://spoonacular.com/food-api
My schema design will be as follows.

User Table:
user_id (Primary Key)
username
email
password
Other useful profile info

Food Table:
food_id (Primary Key)
food_name

UserFavoriteFoods Table:
user_id (Foreign Key referencing User Table)
food_id (Foreign Key referencing Food Table)
This table represents many-to-many relationship.

Recipe Table:
recipe_id (Primary Key)
title
instructions
source_url (url to original recipe)
Other relevant recipe info

UserLikedRecipes Table
user_id (Foreign Key referencing User Table)
recipe_id (Foreign Key referencing Recipe Table)
This table represents many-to-many relationship.

The title of this website is 'G's Recipes'. The website is hosted on Heroku. It will be deployed on a yet to be determined address.

The website gives the users a form to input a search query to search for recipes. After the form is filled out it contacts the Spoonacular API that gives the user a list of recipes based on the query. The list includes titles, likes, and pictures. The user can click on the recipe for details. The recipes give detailed information including a step by step guide of preperation. Users can 'like' the recipe by clicking the like button.

The first fearure of the site is the recipe search. It was chosen as the basis for the website. The recipe listing is the product of the search. The recipe details were also a product of the search. The 'liking' recipes was a feature to show popularity of a recipe to help the user decide between recipes. The database interaction was needed to store the 'likes' for the recipes by the user. The HTML styling was added to create a visually appealing site for the user to navigate through. API intergration was used to fetch the recipes for the user.

User FLow:

Homepage: The user starts on the homepage that gives the user a search form. The search form gives the user the ability to enter a query for the recipes. The application performs a search using thes Spoonacular API based on what the user entered. The search results are displayed on the homepage. Users can click on the desired recipe to view more information.

Recipe details page: The user is directed to this page after clicking on their desired recipe. The recipe details page shows the title, image, number of likes, ingredients, and step-by-step instructions for the selected recipe. Users are given the option to 'Like' the recipe. This page also provides a link to go back to the homepage where they can make another search query.

Users can repeat the process by entering new search queries and searching for new recipes.

The technology used for this application: Flask: Used as the framework for the application. HTML: Used to structure the content and layout. HTML files were used for the user interface. CSS: Used for styling of the application. Spoonacular API: Used to fetch information based on the users queries. Provided detailed information about the recipes. SQLAlchemy: Allows information to easily interact with PostgreSQL database and the application to interact with python objects instead of SQL queries. Jinja2: Template engine for python used in flask. Requests Library: Used to make HTML requests to the API for fetching data. FLask Migrate: Extension for flask that handles database migrations.
