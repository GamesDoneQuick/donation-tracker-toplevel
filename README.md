# donation-tracker-toplevel
Contains the settings and configuration for creating a simple deploy of the tracker

In order to deploy the tracker, some boilerplate code is neccessary for configuration and management. 

The goal of this repository is to make doing so as simple as possible for any given user to get 
started developing on the tracker. It does not go into any details about doing a full production deployment,
as this would be better handled by a full installer.

## Getting a Working Copy of the Tracker

1. Install git (http://www.git-scm.com/download). 
   I'm assuming if you're here, you know enough about git and version control to get started.
2. Install python (https://www.python.org/downloads/).
   Currently, the tracker only supports version 2.6+ for now. Thus, getting whatever the latest 2.7 version is ideal.
   Python version 3.x is not supported by our code at this time. If someone wants that to change, they will have to 
   do the legwork themselves, we are not in a position to support both versions at this time.
3. Install pip (Follow the directions here: https://pip.pypa.io/en/stable/installing/) This is the package management system
   we use with the tracker, and its generally the best option for getting python packages.
4. Clone this repository, typically I put it in a folder called `donations` (and will call it that for the rest of this list). 
   ```> git clone https://github.com/GamesDoneQuick/donation-tracker-toplevel.git donations```
5. Make an empty directory under `donations` called `db`. This is where you can keep the working copy of your sqlite database. 
   By default, the settings are such that one called `db/testdb` will be created, but of course you can modify that to suit 
   your needs
6. Make a copy of `example_local.py` under `donations`, and call it `local.py`. 
   This is where you will enter any deployment-specific settings for your instance of the website.
 1. (optional) Change the `NAME` field under the `DATABASES` variable to point at a different location if you wish.
 2. There are some other config variables related to timezone, e-mail, google docs, and giantbomb's API. None of these are
    neccessary to get started, and mostly can be ignored unless you are interested in that specific feature. Documentation
    on these fields are lacking, but it shouldn't be too diffficult to figure out how they work if you take a look at
    `settings.py`
7. Clone the main repository. The easiest way to do this is as a submodule of this top-level repository. The only restriction 
   is that the module _must_ be called `tracker`: 
   ```> git submodule add https://github.com/GamesDoneQuick/donation-tracker.git tracker```
8. Download the requirements in `tracker/requirements.txt` using pip:
   (Note that you'll need to be root/administrator in order to install it on most systems).
   ```> [sudo] pip install -r tracker/requirements.txt```
 1. If you are under windows, you may need to delete the lines containing `psycopg2` and `chromium-compact-language-detector`
     from `tracker/requirements.txt` (both are optional, and require compilation of C code, which is typically a hassle for 
     people in a Windows environment).
 2. If you are under 'nix or Mac, you'll probably need to `sudo` this/run as administrator
 3. You also need to run `pip install django-paypal`. This isn't currently in `requirements.txt` for awful reasons that I'm hoping 
    will change very soon. The vanilla version on spookylukey's page (https://github.com/spookylukey/django-paypal) will work to 
    get things going. You can install it with
    ```> [sudo] pip install git+https://github.com/spookylukey/django-paypal.git``` 
    If you want to test receiving actual donations through PayPal, you will need to get our custom branch
    ```> git clone https://github.com/GamesDoneQuick/django-paypal.git
    > cd django-paypal
    > git checkout gdqversion
    > [sudo] python setup.py install```
    This branch exists due to certain features we patched in, that have all be implemented in the main trunk (save one). We are
    planning on removing our external branch and switching to the main trunk as soon as possible.
9. Initialize the database. This app, and all the apps it depends on, can be initialized into the database using django's
   migrate command
   ```> python manage.py migrate```
   Note that this is the actual command that will create the `db/testdb` file on your machine (if it does not exist already).
   Please note that if you are using a different location, or a different database type, you will need to make sure the 
   permissions and settings are set up correctly.
 1. This is the general command to migrate all changes in the app. If you ever update any of the dependent libraries, or the 
    tracker itself, you should run this command as well
10. Create a superuser account for the admin:
    ```> python manage.py createsuperuser``` 
    (Follow the promts for username, e-mail, and password)

## Running the test server
You can run the test server, using:
```> python manage.py runserver [port]``` (port argument is optional, the default will be 8000)

You can navigate to the tracker at http://127.0.0.1:8000/ (where `8000` is the the port specified).

To view the admin site, go to: http://127.0.0.1:8000/admin/

And log in using the username/password you set up with `createsuperuser`

If you have any questions, or would like some help getting set-up, or are interested in contributing, please
don't hesitate to contact me at stephen.kiazyk@gamesdonequick.com
