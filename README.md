
# **Table of Contents**

- [**Table of Contents**](#table-of-contents)
	- [**Key Keepers**](#key-keepers)
	- [**CI Guidelines**](#ci-guidelines)
	- [**UX**](#ux)
		- [**Requirements**](#requirements)
			- [Users](#users)
			- [Pages](#pages)
		- [**General Design**](#general-design)
	- [**Features**](#features)
		- [Existing features](#existing-features)
			- [Database existing features](#database-existing-features)
			- [Existing apps](#existing-apps)
		- [Features left to implement](#features-left-to-implement)
	- [**Technologies used**](#technologies-used)
		- [Front End](#front-end)
		- [Back End](#back-end)
	- [**Changelog and Fixes**](#changelog-and-fixes)
		- [Before version 1](#before-version-1)
		- [Version 1 and later](#version-1-and-later)
			- [1.0](#10)
	- [**Testing**](#testing)
		- [Tools used for testing](#tools-used-for-testing)
		- [Testing before version 1](#testing-before-version-1)
	- [**Deployment**](#deployment)
	- [**How to run the project locally?**](#how-to-run-the-project-locally)
	- [**What could be done better?**](#what-could-be-done-better)
	- [**Credits**](#credits)
		- [Special thanks to](#special-thanks-to)
		- [Need to add](#need-to-add)

<hr />

## **Key Keepers**

Hello there,  
and welcome to my final [Code Institute (CI)](https://courses.codeinstitute.net/) school project.

In this project I should be able to show that I can create a web application using [Python 3](https://www.python.org/downloads/) and [Django](https://docs.djangoproject.com/en/2.1/).

I decided to create my own project.

<hr />

## **CI Guidelines**

- **Use the following guidelines when developing your project:**
  - Build a web app that fulfils some actual (or imagined) real-world need. This can be of your choosing and may be domain specific.
  - Write a README file for your project that explains what the project does and the need that it fulfils. It should also describe the functionality of the project, as well as the technologies used. Detail how the project was deployed and tested and if some of the work was based on other code, explain what was kept and how it was changed to fit your need. A project submitted without a README file will FAIL.
  - The project must be a brand-new Django project, composed of multiple apps (an app for each reusable component in your project).
  - The project should include an authentication mechanism, allowing a user to register and log in, and there should be a good reason as to why the users would need to do so. e.g., a user would have to register to persist their shopping cart between sessions (otherwise it would be lost).
  - At least one of your Django apps should contain some e-commerce functionality using Stripe. This may be a shopping cart checkout, subscription-based payments or single payments, etc.
  - Include at least one form with validation that will allow users to create and edit models in the backend (in addition to the authentication mechanism).
  - The project will need to connect to a database (e.g., sqlite or Postgres) using Django’s ORM
  - The UI should be responsive, use either media queries or a responsive framework such as Bootstrap to make sure that the site looks well on all commonly-used devices.
  - As well as having a responsive UI, the app should have a great user experience.
  - The frontend should contain some JavaScript logic to enhance the user experience.
  - Whenever relevant, the backend should integrate with third-party Python/Django packages, such as Django Rest Framework, etc. Strive to choose the best tool for each purpose and avoid reinventing the wheel, unless your version of the wheel is shinier (and if so, consider also releasing your wheel as a standalone open source project).
  - Make sure to test your project extensively. In particular, make sure that no unhandled exceptions are visible to the users, under any circumstances. Use automated Django tests wherever possible. For your JavaScript code, consider using Jasmine tests.
  - Use Git & GitHub for version control. Each new piece of functionality should be in a separate commit.
  - Deploy the final version of your code to a hosting platform such as Heroku.

<hr />

## **UX**


### **Requirements**

#### Users

***The general idea is that only registered users can add / edit / delete property in the database. Also only registered users should be able to contact other users.***

Role | View Property | Add / Edit / Delete Property | Access admin area
--- | --- | --- | ---
Anonymous | Yes | No | No |
Logged in | Yes | Yes* | No |
Logged in as Admin | Yes | Yes** | Yes |

**User should be able to edit / delete only his own property.*

***Admin and CI should be able to delete any property.*

#### Pages

Create 6 - 7 pages for the project.

- **Any page**
  - **Navigation**
    - Logo should lead the user to "home" page
    - Create functionality for user to access **All properties**
    - Create functionality for user to search for existing properties
    - **Anonymous**
      - Create functionality for user to be able to create new account.
      - Create functionality for user to be able to log-in to existing account.
    - **Logged in**
      - Create functionality for user to be able log out from current session
      - Create functionality for user to access **Add new property**
      - Create functionality for user to access **Profile page**
  - **Footer**
    - Show general information about the company (e.g social links, address and contact details)
- **Landing page (index.html)**
  - Welcome new or existing user
  - Show user few examples of properties (up to 5) with short information’s (newest properties)
  - Add section for recent feedbacks
  - Add contact form for user to be able to send messages (e.g "General message", "Property enquiry"(registered users only) and "Feedback")  
- **All properties**
  - Create functionality for user to be able to search for properties.
  - Show user available properties (if any)
    - Show base information about each of them
  - Add pagination (if too many properties to display)
- **Single property**
  - Show user detail information’s about targeted property
    - Title
    - Price
    - Owner
    - Picture
    - More pictures (if any)
    - Address
    - Map
    - Date posted
  - **Logged in**
    - Create functionality for user to be able log out from current session
- **Add property**
  - Allow logged in user to add new property to database
  - Create functionality for user to pay small fee via **Stripe**  
  *The idea is to let user to pay small (£5-£10) onetime fee for posting*
- **Edit property**
  - Allow logged in user to edit his own property
- **Profile page**
  - Show user avatar (if any)
  - Show properties added by user
  - Let user to edit his profile
  - Let user to be able to change his password
- **Django admin**
  - Show registered users and they information
  - Show properties by users
  - Show all messages
  
### **General Design**

Design | Importance
--- | ---
Functionality | 7 |
User experiences | 6 |
HTML / CSS | 5 |

[**To top**](#Table-of-Contents)

<hr />

## **Features**

### Existing features

*For more detail information please visit [**Changelog and Fixes**](#changelog-and-fixes)*

#### Database existing features

*I decided to use Postgres database.*

- **Models**
  - [Property](/listings/models.py)
  - [Enquiries (user messages)](/enquiries/models.py)
  - [User profile](/accounts/models.py) (extend `User` model from Django `auth`)
  
#### Existing apps

[**To top**](#Table-of-Contents)

### Features left to implement

[**To top**](#Table-of-Contents)

<hr />

## **Technologies used**

### Front End

### Back End

[**To top**](#Table-of-Contents)

<hr />

## **Changelog and Fixes**

*[Git](https://git-scm.com/) has been used for version control.*

- There are xxxxxxxxx different branches:

  - [master branch](https://github.com/MiroslavSvec/project-5/tree/master) used in production.  
    - *The application is built from this branch on **Heroku***

  - *xxxxxxxx other branches has been created for development purpose only. Where each branch represent different version of the application.*

### Before version 1

*Before version 1 I did not use separated branches.*

- **0.0**
  - Created basic file structure, installed minimum requirements, started the project "APH"
  - Added setting for `static` files and folders

- **0.1**
  - Created fundamental for `pages` app (for pages such as `index.html` or `about.html`)
  - Added fundamentals for `base.html`

- **0.2**
  - Created fundamental for `listings` app (for pages such as `houses.html`, `house.html` or `search.html`)
  - separated `templates` and `static` for each of the app
  - Added testing via Django build in tests

- **0.3**  
  *As I did not have enough data as well as I thought that this project will be too similar to my 4th project I decided to change the project slightly.*
  - Changed `plants.html` and `plant.html` to match the project definition
  - Added env variables to hide keys
  - Added `if` statement to swap between testing and production database
  - Created single listing model
  - Added fundamental for `accounts` app
  - Create `User` model
  - Created small up to fake users and listing using `django faker`

- **0.4**
  - Added img to db
  - Created fundamentals for `houses.html`
  - Customized the Admin dashboard
  - Added Showcase section to `index.html`
  - Added More Information section to `index.html`
  - Added fundamentals Contact us section to `index.html`
  - Added `_page-header.html`

- **0.5**
  - Extended the `User` model
  - Added section for Bootstrap messages
  - Added user registration and creating profile
  - Added Log in functionality for user
  - Added Log out functionality for user
  - Added functionality for user to be able to change his password
  - Added fundamentals for user to be able to reset his password

- **0.6**
  - Added `enquiries` app for user to be able to contact the company

- **0.7**
  - Finished `house.html` for single house listing
  - Added Light Box for secondary images in single house listing
  - Added fundamentals for `edit_house` view

- **0.8**
  - Removed Whitenoise as no longer required
  - Deployed the project to Digital Ocean for testing
  - Connected the `fake_data_gen` app to the project
  - Added more styles to `index.html` and `house.html`
  - Separated settings for production and development
  - Removed `/media` from `.gitignore` as used on **Digital Ocean** and for local testing (**CI**)  
  *Please note that I will normally store the images elsewhere or upload to the images directly to **Digital Ocean**.*  
  *I only storing them in GitHUb for easy local testing.*

- **0.9**
  - Added first step to add new listing

### Version 1 and later

#### 1.0

*At this point I got back to the project.*

- **Changelog**
  - Created proper `README` template and adjusted it to fit the project
  - Tidied up static files  
  - Added [favicon](/media/img/favicon.ico)
  - [index.html](/pages/templates/index.html)
    - Added more **CSS** styles to `nav`
    - Added **CSS** transitions to `#listings` section
- **Fixes**
  - [index.html](/pages/templates/index.html)
    - fixed `overflow` issues (on small screens) in `#more-info` section

[**To top**](#Table-of-Contents)

<hr />

## **Testing**

### Tools used for testing

- **Front End**
  - [W3C Markup Validation Service](https://validator.w3.org/)

  - [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

  - [JSHint](https://jshint.com/) (Report of all custom JS functions)
    - **Metrics**
      - 
- **Back End**
  - [Jupyter Notebook](https://jupyter.org/index.html)
    - *Most of the functions has been pre-written and tested in **Jupyter Notebook**.*

  - [Visual Studio Python debugger](https://code.visualstudio.com/docs/python/debugging)
    - *Mostly used after **Jupyter Notebook** testing.*

### Testing before version 1

- Fixed issue where alerts prevent user to click on nav links

- **pages app**
  - tested views
  - **index**
    - Fixed issue with `alert` to only shows on top of the page

- **listings app**
  - tested views
  - tested listing model
  - added `max-height` to `.card-img-overlay` as it was covering the `<a>`

- **accounts app**
  - tested User model
  - tested UserProfile model
  - tested views
    - Fixed `clean_email()` now properly check if user already exist
    - Fixed issue when user was not redirected to last page visited
  - Fixed issue where alerts prevent user to click on nav links

- **pages app**
  - tested views
  - **index**
    - Fixed issue with `alert` to only shows on top of the page

- **listings app**
  - tested views
  - tested listing model
  - added `max-height` to `.card-img-overlay` as it was covering the `<a>`

- **accounts app**
  - tested User model
  - tested UserProfile model
  - tested views
  - Fixed `clean_email()` now properly check if user already exist
  - Fixed issue when user was not redirected to last page visited

[**To top**](#Table-of-Contents)

<hr />

## **Deployment**

*I decided to deploy the project to **Digital Ocean** as I wanted to learn something new in process.*

- [Python 3.6.3](https://www.python.org/downloads/release/python-363/) and [Django](https://docs.djangoproject.com/en/2.1/)
- created [requirements.txt]

- **Pre-requirements**
  - pushed the latest changes to **GitHub**
  - created new Ubuntu 18.04 x64 droplet
  - generated new ssh key to connect to the server
- **Users**
  - created new user and gave him root privileges
  - added the new ssh key to the created user
  - disabled the default root user for security reasons
- **Security**
  - added simple firewall for better security
- **Software and packages installation**
  - updated the packages on the server
  - installed **Python 3**
  - installed python3-venv
- **Postgres Database**
  - installed Postgres
  - created new Postgres database
  - created new user in the database and gave him all privilages
- **Folders set up**
  - created new dir
  - cloned the repository to the created dir
- **Virtual Environment**
  - created new venv and active it
  - installed requirements to the venv from **requirements.txt**
- **Cloud (production) setting**
  - created .bash_profile and added all necessary variables to it
  - added try block to seettings.py to look for the cloud setting first
- **Server set up**
  - migrated to new created database
  - add superuser
  - collected static files
  - allowed port 8000 (default for Django) to the firewall
- **Gunicorn**
  - deactivated the venv
  - installed **Gunicorn** via pip
  - added gunicorn.socket and gunicorn.service configuration as per **Digital Ocean** documentation
  - enabled **Gunicorn** socket and checked for existence of it
- **NGINX**
  - installed NGINX
  - created new folder in the project to hold the setting
  - added NGINX setting as per documentation and adjust it to the project
  - added 10Mb max rule to **NGINX** config to allow users to upload large imgs
  - tested NGINX config
  - removed port 8000 from firewall and add new port 80 (*NGINX*)
- restarted **Gunicorn** and **NGINX**
- **Custom Domain**

[**To top**](#Table-of-Contents)

<hr />

## **How to run the project locally?**

*Please note that the project can not be run locally without database user name and password.*

*Due to the security reasons I do not publish any of those and therefore the project can not be really run locally.*

1. Download and install [Python 3](https://www.python.org/downloads/)
2. Clone or download the project
*Please note that if you downloaded the project manually you must unpack it after*
3. Open your **Command line (CLI)** inside the project root or navigate to it
4. [Create virtual environment (venv)](https://docs.python.org/3/tutorial/venv.html) (optional)
   - Activate venv `source venv/bin/activate` where "venv" is the name of your virtual environment
5. Install required packages via **CLI**
   - `pip install -r requirements.txt`
6. Set **venv** variables
   - IP `0.0.0.0`
   - PORT `5000`
   - 
   - SECRET_KEY `my_secret_key`
   - DEVELOPMENT `True`
7. Database
   - 
8. Run the application
   - 
9.  The application should now run on your `localhost:8000`

[**To top**](#Table-of-Contents)

<hr />

## **What could be done better?**

[**To top**](#Table-of-Contents)

<hr />

## **Credits**

### Special thanks to

- **everyone for finding few minutes to test the project!**

  *All of you gave me constructive feedback which made the project better* 😊


### Need to add

- email verification on register / add Terms as required before saving the profile
- add more fields to listing form (first line of address and so on)
- much more JS and less Python for better user experiences

