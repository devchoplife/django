"""
Django is a Python framework that makes it easier to create web sites using Python.

Django takes care of the difficult stuff so that you can concentrate on building your web applications.

Django emphasizes reusability of components, also refereed to as DRY (Don't Repeat Yourself), and comes with ready-to-use features like login system, database connection and 
CRUD operations (Create Read Update Delete).

Django follows the MVT design pattern (Model View Template).
- Model - The data you want to present, usually data from a database.
- View - A request handler that returns the relevant template and content - based on the request from the user.
- Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.

Model
The model provides data from the database.
In Django, the data is delivered as an Object Relational Mapping (ORM), which is a technique designed to make it easier to work with databases.
The most common way to extract data from a database is SQL. One problem with SQL is that you have to have a pretty good understanding of the database structure to be able to work with it.
Django, with ORM, makes it easier to communicate with the database, without having to write complex SQL statements.
The models are usually located in a file called models.py.

View
A view is a function or method that takes http requests as arguments, imports the relevant model(s), and finds out what data to send to the template, and returns the final result.
The views are usually located in a file called views.py.

Template
A template is a file where you describe how the result should be represented.
Templates are often .html files, with HTML code describing the layout of a web page, but it can also be in other file formats to present other results, but we will concentrate on .html files.
Django uses standard HTML to describe the layout, but uses Django tags to add logic:

<h1>My Homepage</h1>
<p>My name is {{ firstname }}.</p>

The templates of an application is located in a folder named templates.

URLs
Django also provide a way to navigate around the different pages in a website.
When a user requests a URL, Django decides which view it will send it to.
This is done in a file called urls.py.
"""
