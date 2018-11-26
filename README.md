# project-5

## 5th project for CI

### Changelog

#### 0.0

- Created basic file structure, installed minimum requirements, started the poroject "APH"
- Added setting for `static` files and folders

#### 0.1

- Created fundamental for `pages` app (for pages such as `index.html` or `about.html`)
- Added fundamentals for `base.html`

#### 0.2

- Created fundamental for `listings` app (for pages such as `houses.html`, `house.html` or `search.html`)
- separated `templates` and `static` for each of the app
- Added testing via Django build in tests

#### 0.3

As I did not have enough data as well as I thought that this project will be too similar to my 4th project I decided to change the project slightly.

- Changed `plants.html` and `plant.html` to match the project defination
- Added env variables to hide keys
- Added `if` statment to swap between testing and production database
- Created single listing model
- Added fundamental for `accounts` app
- Create `User` model
- Created small up to fake users and listing using `django faker`

#### 0.4

- Added img to db
- Created fundamentals for `houses.html`
- Customized the Admin dashboard
- Added Showcase section to `index.html`
- Added More Information section to `index.html`
- Added fundamentals Contact us section to `index.html`
- Added `_page-header.html`

#### 0.5

- Extended the `User` model
- Added section for Boostrap messages
- Added user registration and creating profile
- Added Log in functionality for user
- Added Log out functionality for user
- Added functionality for user to be able to change his password
- Added fundamenatls for user to be able to reset his password

#### 0.6

- Added `enquiries` app for user to be able to contact the company

#### 0.7

- Finished `house.html` for single house listing
- Added Light Box for secondary images in single house listing
- Added fundamentals for `edit_house` view

#### 0.8

- Removed Whitenoise as no longer required
- Deployed the project to Digital Ocean for testing
- Connected the `fake_data_gen` app to the project
- Added more styles to `index.html` and `house.html`
- Separated settings for production and development
- Removed `/media` from `.gitignore` as used on Digital Ocean

### Deployment

I decided to deploy the project to Digital Ocean as I wanted to learn something new in process.

- Pre-requirements
  - pushed the latest changes to GitHub
  - created new `Ubuntu 18.04 x64` droplet
  - generated new ssh key to connect to the server
- Users
  - created new user and gave him root privileges
  - added the new ssh key to the created user
  - disabled the default root user for security reasons
- Security
  - added simple firewall for better security
- Software and packedges installation
  - updated the packedges on the server
  - installed `Python 3`
  - installed `python3-venv`
- Postgres Database
  - installed `Postgres`
  - created new postgres database
  - created new user in the database and gave him all privilages
- Git
  - created new dir
  - cloned the repository to the created dir
- Virtual Enviroment
  - created new venv and actived it
  - installed requirements to the venv from `requirements.txt`
- Cloud (production) setting
  - created `.bash_profile` and added all neccessary variables to it
  - added try block to `seettings.py` to look for the cloud setting first
- Server start
  - migrated to new created database
  - add superuser
  - collected static files
  - allowed port 8000 (default for Django) to the firewall
- Gunicorn
  - deactivated the venv
  - installed Gunicorn via pip
  - added `gunicorn.socket` and `gunicorn.service` configuration as per Digital Ocean documentation
  - enabled Gunicorn socket and chceked for existence of it
- NGINX
  - installed `NGINX`
  - created new folder in the project to hold the setting
  - added `NGINX` seeting as per documenation and adjust it to the project
  - added 10Mb max rulle to `NGINX` config to allow users to upload large imgs
  - tested `NGINX` config
  - removed port `8000` from firewall and add new port `80` (`NGINX`)
- Custom Domain
  

### Tests

- Fixed issue where alerts prevent user to click on nav links

#### pages app

- tested views

  - index
  - Fixed issue with `alert` to only shows on top of the page

#### listings app

- tested views
- tested listing model
- added `max-height` to `.card-img-overlay` as it was covering the `<a>`

#### accounts app

- tested User model
- tested UserProfile model
- tested views
  - Fixed `clean_email()` now properly check if user already exist
  - Fixed issue when user was not redirected to last page visited

#### enquiries app
