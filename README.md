# Jira Clone

### Project link Github
* https://github.com/nuthanc/jiraClone/projects/1

### Guide for reference
* https://docs.djangoproject.com/en/3.0/intro/tutorial01/
* https://github.com/nuthanc/simplesocial

### Structure sketch
* accounts
* projects 
* issues (similar to posts)
* comments

### Project setup
* conda create --name jiraEnv django
* source activate jiraEnv
* django-admin startproject jiraClone
* python manage.py startapp accounts
* python manage.py startapp projects
* python manage.py startapp issues
* python manage.py startapp comments
* Adding the apps in settings.py

### Issues setup
##### Basic
* Type: Story, Bug, Task
* Status: Open, In Progress, Closed
* Details
##### Advanced
* Reporter: Dependency with Accounts
* Assignee: Dependency with Accounts
* Links to other issues
* Attachments

