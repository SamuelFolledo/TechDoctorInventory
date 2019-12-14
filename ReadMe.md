# TechDoctor Inventory
Website for TechDoctor to keep track of inventories and repair requests and schedules using Django as its backend, as a final project for my BackEndWeb 1.2 course in Make School

## Tools User
- [Django RESTful Framework](https://www.djangoproject.com/)
- Heroku - deployment

## Screenshots
### Device Lists - without User
- Home page without a user logged in, with a login and signup button on the nav bar
<img src="https://github.com/SamuelFolledo/TechDoctorInventory/blob/master/static/screenshots/device_list.png" width="465" height="828">

### Device Lists - with User
- With user logged in and have their username displayed and a logout button on the nav bar
<img src="https://github.com/SamuelFolledo/TechDoctorInventory/blob/master/static/screenshots/user-devices_list.png" width="465" height="828">

### Device Detail / Parts List
- When user clicks a device's See Repairable Parts button, then it will show a list of available parts specifically for that device
<img src="https://github.com/SamuelFolledo/TechDoctorInventory/blob/master/static/screenshots/user-parts_list.png" width="465" height="828">

### Login Screen
- Page for user to login and receive its token
<img src="https://github.com/SamuelFolledo/TechDoctorInventory/blob/master/static/screenshots/login_screen.png" width="465" height="828">

### Signup Screen
- Page for user to sign up and create an account with some security and simple password detector
<img src="https://github.com/SamuelFolledo/TechDoctorInventory/blob/master/static/screenshots/signup.png" width="465" height="828">

## Admin Page
### Admin Parts
- Admin page which displays the list of parts which can be sorted, search by title, filtered, and removed, and edited
<img src="https://github.com/SamuelFolledo/TechDoctorInventory/blob/master/static/screenshots/admin_parts.png" width="465" height="828">

### Admin Devices
- Admin page which displays the list of devices as well as create, read, update, or delete
<img src="https://github.com/SamuelFolledo/TechDoctorInventory/blob/master/static/screenshots/admin_device.png" width="465" height="828">


## Challenges
- __Deploying to Heroku__
    - OperationalError - no such table: inventories_device
        - When inventories_device exist nowhere in the file
        - Restarted the db.sqlite3 multiple times and still did not work
        - Ran migrate and makemigrations and still did not work

## Important Links
- [Proposal](https://github.com/SamuelFolledo/TechDoctorInventory/blob/master/proposal.md)
- [Contractor Requirements and Instructions](https://make-school-courses.github.io/BEW-1.2-Authentication-and-Associations/#/Projects/requirements)
- [Contractor Rubric](https://make-school-courses.github.io/BEW-1.2-Authentication-and-Associations/#/Projects/rubric)
- [Django Authentication Checklist](https://github.com/Make-School-Labs/makewiki-starter/blob/master/CHALLENGES.md#login--logout)
- [Playlistr Tutorial](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/start-a-flask-project)

## Deployed websites in Heroku backed by Django
- [Polling Website](https://polls-v2.herokuapp.com/)
- [Make Wiki Website](https://sf-makewiki-v2.herokuapp.com/)