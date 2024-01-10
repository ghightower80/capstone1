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
