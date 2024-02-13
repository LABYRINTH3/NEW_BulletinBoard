# My Bulletin Board Project README

## Project Overview
This project is a simple bulletin board created using Django. Users can register and login to write posts, and the written posts can be viewed on detail pages.

## Project Structure
1. **Accounts App**: Responsible for user account functionalities.
   - Model: Defines a CustomUser class to store username and password.
   - Login and Registration: Validates input username and password for login, and saves input data to the database for registration.

2. **Pages App**: Manages post-related functionalities.
   - Model: Defines a Post class to store title, content, author, and creation time.
   - Post Creation: Allows users to create posts by inputting title and content, and assigns the current logged-in user as the author.
   - Post Detail Page: Displays the content of a specific post when clicked.
   - Post List: Displays all posts stored in the database in a table format.

## User Management Customization
Initially, Django's default user model was used, but I opted to create a custom user model. By adding `AUTH_USER_MODEL = 'accounts.CustomUser'` in settings, I changed the default user model to my custom user model.

## Data Validation Enhancement
To ensure data consistency, an error message is displayed to the user if the password and confirmation password do not match. This is achieved by utilizing the `clean` method to validate the data and raise an error.

## How to Run the Project
1. Install Django and necessary libraries: `pip install django`
2. Perform database migration by navigating to the project folder and running: `python manage.py makemigrations` followed by `python manage.py migrate`
3. Run the server: `python manage.py runserver`
4. Access the bulletin board by opening a web browser and visiting `http://127.0.0.1:8000/`

## Additional Notes
- For more detailed information about the project, please refer to the code comments and source code.
- The project may be updated continuously, and feedback or feature suggestions are always welcome.
