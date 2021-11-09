# Pug Pitch
## Author
* [Dhyder](https://github.com/Dhyder)

## Description
Platform where users submit one minute pitches and other users will vote on them and leave comments to give their feedback on them.

## Screenshot
![cipher](https://user-images.githubusercontent.com/86789832/140872778-b27646e9-703a-4f32-91eb-0e74985a2650.png)

## Live Link
You can view the site at: [Pug Pitch](https://pugpitch.herokuapp.com/)

## User Stories

### As a user I would like to:
* See the pitches other people have posted.
* Vote on the pitch they liked and give it a downvote or upvote.
* Be signed in for me to leave a comment
* Receive a welcoming email once I sign up.
* View the pitches I have created in my profile page.
* Comment on the different pitches and leave feedback.
* Submit a pitch in any category.
* View different pitch categories.

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load The Page | **On page load** | Get all posts, Select between signup and login |
| Select Sign Up | **Email,Username,Password** | Redirect to login |
| Select Login from a news source | **Username and Password** | Redirected to a page with pitches from different categories and commenting section on read button click |
| Select comment button | **Comment** | Form for comment input |
| To Read more on an entire pitch  | **Click read on pitch** | Redirected to the pitch viewing page where user can upvote or downvote a pitch |


## SetUp / Installation Requirements
### Prerequisites
* python3.6.15
* pip
* virtualenv

### Cloning
* In your terminal:

        $ git clone https://github.com/Dhyder/pitched.git
        $ cd pitched

## Running the Application
* Creating the virtual environment

        $ virtualvenv
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ python3.8 -m pip install Flask
        $ python3.8 -m pip install Flask-bootstrap
        $ python3.8 -m pip install Flask-Script

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.6.15 manage.py tests

## Technologies Used
* Python3.8.10
* Flask

## Known Bugs
* No known bugs at the moment
## Author's Contact Information
* For any queries, you can reach out at [desastrecaliente@gmail.com]

### MIT License:
Copyright (c) 2021 **Dhyder**
