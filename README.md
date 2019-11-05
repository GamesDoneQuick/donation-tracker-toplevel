# donation-tracker-toplevel

## AS OF 2019/11/01 PYTHON 3.6/3.7 IS REQUIRED (3.8 IS UNTESTED)

Contains the settings and configuration for creating a simple deploy of the tracker.

In order to deploy the tracker, some boilerplate code is neccessary for configuration and management. The goal of this repository is to make doing so as simple as possible for any given user to get started developing on the tracker.

## Getting a Working Copy of the Tracker

1. [Install Git](http://www.git-scm.com/download). I'm assuming if you're here, you know enough about git and version control to get started. You can check if you have git with the command `which git`, and which version you have with `git --version`.
1. [Install Python](https://www.python.org/downloads/). The code requires 3.6+. 3.8 is not thoroughly tested. You can determine if Python is installed with the command `which python`, and which version of Python you have with the command `python -V`.
1. [Install pip](https://pip.pypa.io/en/stable/installing/) This is the package management system we use with the tracker, and its generally the best option for getting Python packages.
1. [Install node](https://nodejs.org/en/download/). Currently the JS code is only tested with node 12, but others may work.
1. [Install yarn](https://yarnpkg.com/en/). If you have npm installed, you can just run `npm i -g yarn` and it should do the right thing.
1. [Install direnv](https://github.com/direnv/direnv). *Optional, Linux/OSX only* This will help set up an isolated development environment. PyCharm might do the job on Windows, but no promises.
    1. If you do _not_ want to use `direnv`, you may need to set the environment variables `LC_ALL` and `LC_CTYPE` when running the server (specifically on macOS). Check `.envrc` for the values to use for these variables.
1. Clone this repository, typically I put it in a folder called `donations`, which is the path to which this repo will be referred for the remainder of these instructions:
    ```> git clone https://github.com/GamesDoneQuick/donation-tracker-toplevel.git donations```
1. Make an empty directory under `donations` called `db`. This is where you can keep the working copy of your sqlite database. By default, the settings are such that one called `db/testdb` will be created, but of course you can modify that to suit your needs.
1. Make a copy of `example_local.py` under `donations`, and call it `local.py`. This is where you will enter any deployment-specific settings for your instance of the website.
    ```> cp example_local.py local.py```
    1. (optional) Change the `NAME` field under the `DATABASES` variable to point at a different location if you wish.
    2. There are some other config variables related to timezone, e-mail, google docs, and giantbomb's API. None of these are neccessary to get started, and mostly can be ignored unless you are interested in that specific feature. Documentation on these fields is lacking, but it shouldn't be too diffficult to figure out how they work if you take a look at `settings.py`.
1. Clone the submodules.
    ```> git submodule update --init```
    1. This will clone `tracker`.
1. Download the requirements in using pip:
    ```> pip install -r requirements.txt```
    1. If you are using Windows, you may need to delete the lines containing `psycopg2` and `chromium-compact-language-detector` from `tracker/requirements.txt` (both are optional, and require compilation of C code, which is typically a hassle for people in a Windows environment).
    2. If you are under 'nix or Mac, you'll probably need to `sudo` this/run as administrator, unless you're using `direnv` as suggested above.
    3. The default pip configuration performs a fresh install of all packages, meaning that previously installed packages will be uninstalled before being reinstalled. If you get any exceptions during uninstallation, you can try the flag `--ignore-installed` to leave those packages alone and continue with other packages.
1. Install the required npm packages.
    ```> cd tracker && yarn```
1. Initialize the database. This app, and all the apps it depends on, can be initialized into the database using django's migrate command, `python manage.py migrate`. Notes:
    1. This is the actual command that will create the `db/testdb` file on your machine (if it does not exist already).
    2. If you are using a different location, or a different database type, you will need to make sure the permissions and settings are set up correctly.
    3. This is the general command to migrate all changes in the app. If you ever update any of the dependent libraries, or the tracker itself, you should run this command again.
1. Create a superuser account for the admin with the command `python manage.py createsuperuser` and follow the prompts. This is the account you'll use to access your testing instance of the app.

## Running the test server (see below on how to launch the UI)

You can run the test server, using the command `python manage.py runserver [port]`. The `port` argument is optional; the default is 8000.

You can navigate to the tracker at [http://127.0.0.1:8000/tracker/](http://127.0.0.1:8000/tracker/) (where `8000` is the the port specified). To view the admin site, go to: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/) and log in using the username/password you set up with `createsuperuser`.

## Running the UI development server

Webpack has a development server that can proxy requests to the backend. Once you've installed the required packages, you can run the server with the following command while in the `tracker` folder:
```> yarn start```

It defaults to port 8080, so simply visit [http://127.0.0.1:8080/tracker/](http://127.0.0.1:8080/tracker/) and you should be able to view the site just like the Django development server.

Note that if you change the port that the server is running on you'll need to edit `webpack.config.js` to point to the correct port in the proxy section.

## Building the UI package (release mode)

Simply run the build command in the `tracker` directory:
```> yarn build```

This does two things:

1. Builds the UI Javascript and CSS bundles and puts them in `tracker/static/gen`.
1. Outputs a manifest file to `ui-tracker.manifest.json` so that Django knows where to find the resulting bundles.

This will allow the tracker UI to function, though if you want to develop with it you'll want to use the development proxy, otherwise you'll not only have a minified build (difficult to debug!) but you'll have to rerun the command every time you make a change.

## Server deployment

There are far too many different ways to deploy the server to go over every possibility here, so you should start with [Deploying Django](https://docs.djangoproject.com/en/1.11/howto/deployment/).

Node is NOT required to actually run the server, just to build the JS bundles. You can either build them on another machine and copy them (don't forget the manifest file!) or build them on the server, but Node is NOT required to actively serve any network requests.

`PAYPAL_TEST` in the settings file will determine whether or not Paypal operates in sandbox mode. It is no longer possible to set this on a per-event basis.

## Docker (experimental, development environments only)

Alternately, you can use [Docker](https://www.docker.com/). The packaged Dockerfile should build an isolated development environment for you, regardless of what OS you're on. While this is potentially the easiest to set up, it also has the most overhead. Note that this container is *NOT* intended for production use.

You can also download the latest image from [Dockerhub](https://hub.docker.com/r/gamesdonequick/donation-tracker-toplevel/).

## Contact

If you have any questions, or would like some help getting set-up, or are interested in contributing, please don't hesitate to contact us at [tracker@gamesdonequick.com](tracker@gamesdonequick.com).
