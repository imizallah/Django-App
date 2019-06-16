
############################### SEEDSTARS DEVELOPER CASE STUDY ###############################
### PROBLEM: ###
Make an application which stores names and email addresses in a database (SQLite is fine). Make sure it:

Has welcome page in http://localhost/ 
Note: this page has links to list and create functions
Lists all stored names/email address in http://localhost/list
Adds a name/email address to the database in http://localhost/add 
Note: should validate input and show errors

The challenge is a Django based application, so please make sure you use all of Django infrastructure (form, template inheritance, ORM) correctly. Also make sure the app does not have major security problems: CSRF, XSS, SQL Injection.

Make reasonable assumptions, state your assumptions, and proceed. Once you have completed the challenge, let us know and share your thoughts on the problems/solutions.

### HOW TO RUN APP ###
Run: "python manage.py runserver"

#NOTE:# if errors:
Try: "python manage.py migrate"

### SECURITY PROBLEMS ###
#CSRF#
The default CSRF Middleware is activated by default in the MIDDLEWARE setting. django will send a random key both in cookie, and form data. Then, when users POSTs, it will check if two keys are identical. In case where user is tricked, 3rd party website cannot get your site's cookies, thus causing auth error.

In my create.html POST form, we used the csrf_token tag inside the <form> element if the form is for an internal URL.
e.g <form method="post">{% csrf_token %}

This is done for POST forms that target external URLs, since that would cause the CSRF token to be leaked, leading to a vulnerability.

#NOTE:#
The 'django.middleware.csrf.CsrfViewMiddleware' should come before any view middleware that assume that CSRF attacks have been dealt with.


#xss#
I used the 'django.middleware.security.SecurityMiddleware'. The django.middleware.security.SecurityMiddleware provides several security enhancements to the request/response cycle which also includes: SECURE_BROWSER_XSS_FILTER to handle Cross-site request forgery.

#SQL INJECTION#

The use of Object Relational Mapper (ORM) will prevent any possibility of SQL injection.
I employed the use of Python Database API to build models which should also solve the SQL injection vulnerabilities.
usage: # from django.db import models #

Thank You 

## ISHAYA SUNDAY ##
## ishayasunday@gmail.com ##