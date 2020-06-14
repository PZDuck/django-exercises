# sf-festival

Work in progress

http://enigmatic-dawn-93404.herokuapp.com/

Admin:
* admin
* password
  
Censor user for testing purposes:
* test_censor
* fuckingpassword


### !!! EAR RAPE ALERT !!!
Be prepared when accesing the "vote" link, it has its surprises

### Deploying locally
1. Clone/download the project
2. Open a console in the base directory of the project (glukhie/)
3. Create a database ```python manage.py migrate```
4. Create a superuser ```python manage.py createsuperuser```
5. Run the server ```python manage.py runserver```
6. Test the functionality


Note: roles and permissions should be created manually, so I would recommend to test heroku version. No initial dumped data is available right now


### Things to do/improve:
* Let users choose desired timeslot directly on the schedule page by clicking on the timeslot
* Apply styling to sign out page
* Redesign the voting system for censors
* Remove/Disable the request object after is has been approved/rejected
* Create a separate Band profile object and let users create and customize their band's page
