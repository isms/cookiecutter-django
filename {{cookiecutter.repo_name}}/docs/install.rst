Install
=======

Getting started with a development environment
----------------------------------------------

* ``git clone`` the repo.
* Install the `Heroku toolbelt <https://toolbelt.heroku.com/>`_.
* Get the ``.env`` file from a team member in a secure way and put it in the project root.
* Create and activate a new ``virtualenv`` (preferably using ``virtualenvwrapper``).
* Run ``pip install -r {{ cookiecutter.project_name }}/requirements/local.txt`` to install dependencies.

Modular settings file
---------------------

We keep our settings files tailored to the context using ``django-configurations``.  Settings are defined in ``{{ cookiecutter.project_name }}/config/settings.py`` using secrets in either ``.env`` (locally) or ``heroku:config`` (in production).

For configuration purposes, the following table maps the environment variables to their Django setting:

======================================= ===========================
Environment Variable                    Django Setting             
======================================= ===========================
DJANGO_AWS_ACCESS_KEY_ID                AWS_ACCESS_KEY_ID          
DJANGO_AWS_SECRET_ACCESS_KEY            AWS_SECRET_ACCESS_KEY      
DJANGO_AWS_STORAGE_BUCKET_NAME          AWS_STORAGE_BUCKET_NAME    
DJANGO_CACHES                           CACHES                     
DJANGO_DATABASES                        DATABASES                  
DJANGO_DEBUG                            DEBUG                      
DJANGO_EMAIL_BACKEND                    EMAIL_BACKEND              
DJANGO_SECRET_KEY                       SECRET_KEY                 
DJANGO_SECURE_BROWSER_XSS_FILTER        SECURE_BROWSER_XSS_FILTER  
DJANGO_SECURE_SSL_REDIRECT              SECURE_SSL_REDIRECT        
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF      SECURE_CONTENT_TYPE_NOSNIFF
DJANGO_SECURE_FRAME_DENY                SECURE_FRAME_DENY          
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS   HSTS_INCLUDE_SUBDOMAINS    
DJANGO_SESSION_COOKIE_HTTPONLY          SESSION_COOKIE_HTTPONLY    
DJANGO_SESSION_COOKIE_SECURE            SESSION_COOKIE_SECURE      
======================================= ===========================

Default values:

======================================= ===================== ===================
Environment Variable                    Development Default   Production Default
======================================= ===================== ===================
DJANGO_AWS_ACCESS_KEY_ID                n/a                   raises error
DJANGO_AWS_SECRET_ACCESS_KEY            n/a                   raises error
DJANGO_AWS_STORAGE_BUCKET_NAME          n/a                   raises error
DJANGO_CACHES                           locmem                memcached
DJANGO_DATABASES                        See .env file         See code
DJANGO_DEBUG                            True                  False
DJANGO_EMAIL_BACKEND                    console.EmailBackend  smtp.EmailBackend
DJANGO_SECRET_KEY                       CHANGEME!!!           raises error
DJANGO_SECURE_BROWSER_XSS_FILTER        n/a                   True
DJANGO_SECURE_SSL_REDIRECT              n/a                   True
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF      n/a                   True
DJANGO_SECURE_FRAME_DENY                n/a                   True
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS   n/a                   True
DJANGO_SESSION_COOKIE_HTTPONLY          n/a                   True
DJANGO_SESSION_COOKIE_SECURE            n/a                   False
======================================= ===================== ===================


Running a development server locally
------------------------------------

Running ``python manage.py runserver`` will use the built-in Django debug server -- which is nice because it gives us all kind of debugging information via the built-in ``DEBUG=True`` option and also because we have the ``django-debug-toolbar`` package installed.  This server will come up by default on ``http://localhost:8000/``.
