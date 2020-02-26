#  The Badlu Online store in Django and Postgres
<pre>
A database backed order-processing system for Badlu's chai adda. Assume there are only three products for now: idli, chai and samosa.
</pre>
### The user interaction is as follows: 
<pre>
User:	Open  localhost:8000/login    method type: 'GET'
App:	Returns an empty login form with username and password
User:	Fills form and submits it.  URL: localhost:8000/login, method type 'POST'.   (Use http, not https)
App:	If user in database and validated correctly, return a redirect to localhost:8000/orders
	See: https://www.tutorialspoint.com/django/django_page_redirection.htm
	Browser goes to localhost:8000/orders with a 'GET' method
	App returns an order-view-create page, which contains  the last 5 orders (at most), one on each line, along with a form that has fields for the quantities to be ordered of each item. 
User:	Fills form and hits submit. URL: localhost:8000/orders, method_type: 'POST'. The parameters will automatically be encoded in the body of the request as 'samosa=10&idli=0&chai=10'. 
App:	Inserts order into order history in the database, and returns the order-view-create page, with the order history updated, and the form fields emptied. A status line at the bottom should be in green to convey acknowledgment, or in red to convey error.
</pre>
### Now for some implementation details: 
<pre>
The django app should be called orders
The database contains users and order history.  You can pre-populate the list of users
At this point we don't want to use Django's built-in users table. We'll just create our own. 
Create table addaUsers with (loginName (primary key), password) in postgres


Create table public.order (orderId(pk), loginName, dateTime)
I used the fully qualified name public.order instead of 'order' because the order is a reserved word. 
Use postgres serial sequence to auto-increment orderId. 
See: https://www.postgresqltutorial.com/postgresql-serial/



Use the "insert into order… returning id' form of the insert query (specific to postgres), so that the order id is returned in the confirmation message to the user.
You must use the session mechanism in django (see See 'https://docs.djangoproject.com/en/3.0/topics/http/sessions/'. This is to maintain continuity between the time the login screen is shown and subsequently the order is submitted.
For this exercise, I am not too fussy about what the UI looks like (for this exercise!). But for the sake of automated testing, the form fields should have the names 'idli', 'samosa', 'chai', and there should be a  <div id="status"> somewhere in the form that begins with "Success" or "Error". 

</pre>
