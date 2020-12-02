# Hackbright Academy Capstone Project
Hackbright Academy Full-Stack Software Engineering Program

This web app creates song snippets from Taylor Swift albums using a Markov chain. The user will be able to save and view their favorite snippets and create snippet mash-ups with their own uploaded albums. Taylor Swift album details are retrieved from the Audio DB API.

## Technologies:
* Python
* Flask
* Jinja
* PostgreSQL
* SQLAlchemy
* HTML
* CSS
* Bootstrap
* jQuery
* Javascript (AJAX)

## Features:

### MVP
* User can register and log in
* User can view all details for each Taylor Swift studio album
* User can create song snippet and save it
* User can view all saved song snippets

### 2.0
* User can view saved song snippets by album
* User can upload their own album lyrics to create a Taylor Swift mash-up
* Album details page contains a chart displaying the most common words in an album
* Added log-in and registration security

### Future Implementations
* User can share snippets view text and/or email

## Installation:

### Requirements:

* PostgreSQL
* Python 3.7.3

You are welcome to run this app locally on your own computer. To do so, first clone this repository:

```
$ git clone https://github.com/dianasch/snippets.git
```

Create and activate a virtual environment:

```
$ pip3 install virtualenv
$ virtualenv env
$ source env/bin/activate
```

Install dependencies:

```
(env) $ pip3 install -r requirements.txt
```

Create a secrets.sh file and save your secret key for this app using the following syntax:

```
export SECRET_KEY="your_secret_key"
```

Activate the secrets.sh file in your terminal:

```
source secrets.sh
```

Create the database:

```
(env) $ createdb snippets
```

Seed the database:

```
(env) $python3 seed.py
```

Start the backend server:

```
(env) $ python3 server.py
```

Open a new window and visit this address: http://0.0.0.0:5000/ to view the Snippets app.