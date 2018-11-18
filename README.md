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

- Changed `plants.html` and  `plant.html` to match the project defination
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

- Deployed the project to Heroku for testing
- Connected the `fake_data_gen` app to the project
- Added more styles to `index.html` and `house.html`


### Tests

- Fixed issue where alerts prevent user to click on nav links
 
#### pages app

- tested views
- - index
- - - Fixed issue with `alert` to only shows on top of the page
  
#### listings app

- tested views
- tested listing model
- added `max-height` to `.card-img-overlay` as it was covering the `<a>`

#### accounts app

- tested User model
- tested UserProfile model
- tested views
- - registration
- - - Fixed `clean_email()` will now properly check if user already exist 
- - log in
- - - Fixed issue whe user was not redirected to last page visited

#### enquiries app