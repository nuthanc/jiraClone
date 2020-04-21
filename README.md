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
* Title
* Issue_no
* Type: Story, Bug, Task
* Status: Open, In Progress, Closed
* Details

##### Advanced
* Reporter: Dependency with Accounts
* Assignee: Dependency with Accounts
* Links to other issues
* Attachments

#### Model, Template, View and Url setup of Issues
* issues/templates/issues/issue_form.html
* project urls.py and issues urls.py
* issues models.py and views.py
* Styling issue_form using django-crispy-forms
  * https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html

#### DetailView for Issues
* issues views.py, urls.py and issue_detail.html
* Complete with issue_detail.html and start issue_list.html
* Add get_context_data in IssueDetail view for passing the className to display appropriate colors for Issue type

#### ListView for Issues
* Next loop issue_list in views.py and attach className to each issue to give colors in ListView

#### UpdateView for Issues
* views.py and urls.py
* https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-editing/

#### DeleteView for Issues
* views.py, issue_confirm_delete urls.py

#### String representation for model
* Add String representation for model so that it is displayed appropriately in the Admin page

#### Admin templates from lecture
* Project dir -> templates -> admin -> template files
* Django source code: https://github.com/django/django
* https://github.com/django/django/tree/master/django/contrib/admin/templates
* Registration page: https://github.com/django/django/tree/master/django/contrib/admin/templates/registration
* Admin page: https://github.com/django/django/tree/master/django/contrib/admin/templates/admin
* Need to have same directory structure as above since we are overriding
* base_site.html which extends admin/base.html
* We just really want to play with base_site.html
* So copy that code to admin/base_site.html