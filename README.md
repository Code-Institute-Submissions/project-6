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

- Created fundamental for `listings` app (for pages such as `plants.html`, `plant.html` or `search.html`)
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


### Tests

#### pages app

- tested views
  
#### listings app

- tested views
- tested listing model
- added `max-height` to `.card-img-overlay ` as it was covering the `<a>`

#### accounts app

- tested User model

