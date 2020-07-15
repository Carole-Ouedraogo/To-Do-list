To-Do
Release 0: Setup
We are going to create a CRUD app to create To-Do lists. Start by setting up a new Django project. We will be deploying this project to Heroku so you'll want to install psycopg2 and set up your project with a Postgresql database.

Release 1: Models
Once you're project is set up, create a new app for To-Do lists and set up your models.

A User should be able to create multiple lists.
Each list can have many tasks associated with it.
Each task belongs to one List.
Users should be able to create, read, update, and destroy a List.
Users should be able to create, read, update, and destroy Tasks on a List.
Each Task should have a boolean value for completion. task.completed = True
Each Task should have a due date.
Release 2: Front End
Start a new react app to act as the front end for your To-Do List.

On the main page, a user should see all of Lists that still have incomplete tasks.
Clicking on a list will take you to a List page that displays all the tasks for that list.
From here a user should be able to:
create new tasks
update existing tasks
mark a task as complete
Release 3: Additional Functionality
Once you have the basic CRUD functionality working, add at least one of the following features. You'll have to-do your own research to figure out how to impliment some of these. Don't worry, spending hours and hours reading blogs and documentation is a huge part of programming. If you get frustrated, you're doing it right.

Easy-ish
Add a feature for users to view all their completed Lists.
Add the ability to add a status to each task. Something like task.status = 'Awaiting Review' or task.status = 'Started'
Less Easy
Add the ability to link a task to another List. Example: Say you had a list called Tasks For the Week, and one of the tasks was "Create a new Crud Challenge for Code Platoon Students" That task might have many steps, so it would link to a new List with a list of tasks for writing the challenge.
Right now our tasks are probably displayed in the order they were created. How can you add the ability to order and re-order tasks for a given list?
