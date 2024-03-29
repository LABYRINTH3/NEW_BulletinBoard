# Bulletin Board Project README

## Project Overview
This project is a simple bulletin board created using Django. Users can register and login to write posts, and the written posts can be viewed on detail pages.
Edit & delete function is added.

## Project Structure
1. **Accounts App**: Responsible for user account functionalities.
   - Model: Defines a CustomUser class to store username and password.
   - Login and Registration: Validates input username and password for login, and saves input data to the database for registration.

2. **Pages App**: Manages post-related functionalities.
   - Model: Defines a Post class to store title, content, author, and creation time.
   - Post Creation: Allows users to create posts by inputting title and content, and assigns the current logged-in user as the author.
   - Post Detail Page: Displays the content of a specific post when clicked.
   - Post List: Displays all posts stored in the database in a table format.
   - Post Edit and Delete: Recently added functionalities to edit and delete posts. However, there is currently an issue where these functions are accessible without requiring users to log in.

## User Management Customization
Initially, Django's default user model was used, but I opted to create a custom user model. By adding `AUTH_USER_MODEL = 'accounts.CustomUser'` in settings, I changed the default user model to my custom user model.

## Data Validation Enhancement
To ensure data consistency, an error message is displayed to the user if the password and confirmation password do not match. This is achieved by utilizing the `clean` method to validate the data and raise an error.

## Authorization Issue (FIXED)
~~There is a current issue where the edit and delete functionalities are accessible without requiring users to log in.~~

## Update (14th February 2024)
- Reset the screen size for mobile compatibility.
- Modified the edit and delete functions to be available only when logged in.
- Implemented a security fix for the delete functionality. Now, users can only delete posts if the ID of the logged-in user matches the ID of the post author. If they don't match, users are redirected to another page.

## Update (15th February 2024)
- Implemented a safeguard against unintended data loss: when adding a blank title or body, a pop-up window now appears or the page reloads to prevent accidental loss of written content. This is achieved by utilizing the `required` attribute in HTML forms.
- Enhanced password security: Previously, passwords were stored as strings. Now, all passwords, including existing ones, are encrypted and securely saved.

## How to Run the Project
1. Install Django and necessary libraries: `pip install django`
2. Perform database migration by navigating to the project folder and running: `python manage.py makemigrations` followed by `python manage.py migrate`
3. Run the server: `python manage.py runserver`
4. Access the bulletin board by opening a web browser and visiting `http://127.0.0.1:8000/`

### Additional Steps:
- **Using a Virtual Environment (Recommended)**
  
- **Creating a Superuser**:
  Django superuser account to access the admin interface.
  ```
  python manage.py createsuperuser
  ```
  Go to `http://127.0.0.1:8000/admin/` and login with the superuser id.
  
  Please ensure that you have Python installed on your system before proceeding with the installation steps.

## Additional Notes
- For more detailed information about the project, please refer to the code comments and source code.
- Feedback or feature suggestions are welcome.
