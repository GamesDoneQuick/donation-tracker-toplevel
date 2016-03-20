# donation-tracker-toplevel

Contains the settings and configuration for creating a simple deploy of the tracker.

In order to deploy the tracker, some boilerplate code is neccessary for configuration and management. The goal of this repository is to make doing so as simple as possible for any given user to get started developing on the tracker. It does not go into any details about doing a full production deployment, as this would be better handled by a full installer.

## Getting a Working Copy of the Tracker

1. [Install Git](http://www.git-scm.com/download). I'm assuming if you're here, you know enough about git and version control to get started. You can check if you have git with the command `which git`, and which version you have with `git --version`.
2. [Install Python](https://www.python.org/downloads/). Currently, the tracker only supports version 2.6+ for now. Thus, getting whatever the latest 2.7 version is ideal. You can determine if Python is installed with the command `which python`, and which version of Python you have with the command `python -V`. Python version 3.x is **not** supported by our code at this time. If someone wants that to change, they will have to do the legwork themselves, we are not in a position to support both versions at this time.
3. [Install pip](https://pip.pypa.io/en/stable/installing/) This is the package management system we use with the tracker, and its generally the best option for getting Python packages.
4. Clone this repository, typically I put it in a folder called `donations`, which is the path to which this repo will be referred for the remainder of these instructions:
    ```> git clone https://github.com/GamesDoneQuick/donation-tracker-toplevel.git donations```
5. Make an empty directory under `donations` called `db`. This is where you can keep the working copy of your sqlite database. By default, the settings are such that one called `db/testdb` will be created, but of course you can modify that to suit your needs.
6. Make a copy of `example_local.py` under `donations`, and call it `local.py`. This is where you will enter any deployment-specific settings for your instance of the website.
    ```> cp example_local.py local.py```
    1. (optional) Change the `NAME` field under the `DATABASES` variable to point at a different location if you wish.
    2. There are some other config variables related to timezone, e-mail, google docs, and giantbomb's API. None of these are neccessary to get started, and mostly can be ignored unless you are interested in that specific feature. Documentation on these fields is lacking, but it shouldn't be too diffficult to figure out how they work if you take a look at `settings.py`.
7. Clone the [main repository](https://github.com/GamesDoneQuick/donation-tracker). The easiest way to do this is as a submodule of this top-level repository. The only restriction is that the module _must_ be called `tracker`:
    ```> git submodule add https://github.com/GamesDoneQuick/donation-tracker.git tracker```
8. Download the requirements in `tracker/requirements.txt` using pip:
    ```> pip install -r tracker/requirements.txt```
    1. If you are using Windows, you may need to delete the lines containing `psycopg2` and `chromium-compact-language-detector` from `tracker/requirements.txt` (both are optional, and require compilation of C code, which is typically a hassle for people in a Windows environment).
    2. If you are under 'nix or Mac, you'll probably need to `sudo` this/run as administrator.
    3. The default pip configuration performs a fresh install of all packages, meaning that previously installed packages will be uninstalled before being reinstalled. If you get any exceptions during uninstallation, you can try the flag `--ignore-installed` to leave those packages alone and continue with other packages.
9. You also need to run `pip install django-paypal`. This isn't currently in `requirements.txt` for awful reasons that I'm hoping  will change very soon. The [vanilla version from spookylukey](https://github.com/spookylukey/django-paypal) will work to get things going. You can install it with.
    ```> pip install git+https://github.com/spookylukey/django-paypal.git```
0. Initialize the database. This app, and all the apps it depends on, can be initialized into the database using django's migrate command, `python manage.py migrate`. Notes:
    1. This is the actual command that will create the `db/testdb` file on your machine (if it does not exist already).
    2. If you are using a different location, or a different database type, you will need to make sure the permissions and settings are set up correctly.
    3. This is the general command to migrate all changes in the app. If you ever update any of the dependent libraries, or the tracker itself, you should run this command again.
1. Create a superuser account for the admin with the command `python manage.py createsuperuser` and follow the prompts. This is the account you'll use to access your testing instance of the app.

## Running the test server

You can run the test server, using the command `python manage.py runserver [port]`. The `port` argument is optional; the default is 8000.

You can navigate to the tracker at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) (where `8000` is the the port specified). To view the admin site, go to: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/) and log in using the username/password you set up with `createsuperuser`.

## Testing PayPal Donations

If you want to test receiving actual donations through PayPal, you will need to get our custom branch

1. `> git clone https://github.com/GamesDoneQuick/django-paypal.git`
2. `> cd django-paypal`
3. `> git checkout gdqversion`
4. `> [sudo] python setup.py install`


This branch exists due to certain features we patched in, that have all be implemented in the main trunk (save one). We are planning on removing our external branch and switching to the main trunk as soon as possible.

## Contact

If you have any questions, or would like some help getting set-up, or are interested in contributing, please don't hesitate to contact me at [stephen.kiazyk@gamesdonequick.com](stephen.kiazyk@gamesdonequick.com).
