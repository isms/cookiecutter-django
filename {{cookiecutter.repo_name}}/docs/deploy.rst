Deploy
========

Deployment with Heroku
----------------------

The Heroku `Django tutorial <https://devcenter.heroku.com/articles/getting-started-with-django>`_ is a good place to start, but here’s a general outline.

* ``Procfile`` tells Heroku how to run our processes.  We will have a ``web`` process (and possibly later on a ``worker`` process).
* On the Heroku side, we set our configuration variables with ``heroku config``. On the local side, ``.env`` holds all environment variables, including our secrets (e.g. Django’s session signing key, database login credentials, etc).  For this reason, we will keep that file out of version control.  When we need to test locally, those environment variables will automatically be set up by ``django-dotenv``, which is used via a couple of lines in ``manage.py``.
* ``{{ cookiecutter.project_name }}/requirements/production.txt`` tells Heroku what packages to install and build.

To deploy the app, merge your changes into the master branch. If database migrations are necessary, that takes more prior consideration. Run these commands to deploy the project to Heroku:

First deploy
------------

.. code-block:: bash

    heroku create --buildpack https://github.com/heroku/heroku-buildpack-python
    heroku addons:add heroku-postgresql:dev
    heroku addons:add pgbackups
    heroku addons:add sendgrid:starter
    heroku addons:add memcachier:dev
    heroku pg:promote HEROKU_POSTGRESQL_COLOR
    heroku config:set DJANGO_CONFIGURATION=Production
    heroku config:set DJANGO_SECRET_KEY=RANDOM_SECRET_KEY
    heroku config:set DJANGO_AWS_ACCESS_KEY_ID=YOUR_ID
    heroku config:set DJANGO_AWS_SECRET_ACCESS_KEY=YOUR_KEY
    heroku config:set DJANGO_AWS_STORAGE_BUCKET_NAME=BUCKET
    git push heroku master
    heroku run python {{cookiecutter.repo_name}}/manage.py syncdb --noinput --settings=config.settings
    heroku run python {{cookiecutter.repo_name}}/manage.py migrate --settings=config.settings
    heroku run python {{cookiecutter.repo_name}}/manage.py collectstatic --settings=config.settings


Subsequent deploys
------------------

.. code-block:: bash

    git push heroku master
    heroku run python {{cookiecutter.repo_name}}/manage.py migrate --settings=config.settings
    heroku run python {{cookiecutter.repo_name}}/manage.py collectstatic --settings=config.settings
