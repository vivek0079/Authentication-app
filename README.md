# Authentication-app

__Description:__

  This is a custom user authentication app mainly focused on following functionalities
    1.Register/Creating user
    2.Login/Logout user
    3.Two step Email verification 
    4.Forgot password option
  
  **This app is mainly for the reference of django authentication system**
  
__Technology Stack:__

_Front-end:_ &nbsp;&nbsp;Bootstrap 4(HTML & CSS)

_Back-end:_ &nbsp;&nbsp;Django1.11 (Python 3.5)

_Database:_ &nbsp;&nbsp;dbsqlite3

__Instructions:__

 
  1.Make a directory in your local machine and create a virtual environment by `python3 -p virtualenv .`

  2.Clone this repo in that directory and ensure to install the requirements by `pip install -r requirments.txt` 
  
  3.Make the migrations to create the database by `python3 manage.py makemigrations` followed by `python3 manage.py migrate`
  
  4.Create superuser by using the command `python3 manage.py createsuperuser`

  5.To run the application open terminal and change directory to the manage.py in the Blog-app/mysite folder.Now run the command `python3 mange.py runserver` and the app goes live in your machine.
  
__Note:__

  This is just a prototype and is not indented for deployment.
  
  This app uses smtp.gmail backend to send mails.However gmail is not recommended for a production project (live web application) because gmail is not a transactional email service; gmail is not made web application use and, if abused, could cause you to be banned from gmail. In any case, it's still very useful to test on gmail until you move to a production-ready email service like Sendgrid or Postmark.  
