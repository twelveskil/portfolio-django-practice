# portfolio-django-practice

The 'showcase' branch specifically functions to display a page which can display projects.

Projects to be displayed are created by creating an instance of the model class Project. You must enter the Django shell ((venv) $python manage.py shell) and then import the class (Project) from models (projects.models). Then you can create instances of Project according to the model (and 'save()' them(!!!)) which get stored with an id that can help in the need of deleting/mutating the objects.

I found out that editing the objects in the terminal is possible with the help of looking at the objects [print(Project.objects.all())] and mutating them as needed with a for loop or something (and saving them within the loop!!!). I can also print the objects out since I made a str method in the Project class.
