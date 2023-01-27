"""
views.py holds functions/classes that handle what data is displayed in the HTML templates.
Each function and class handles the logic that gets processed when a URL is visited.
"""
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    """a view function which takes an HttpRequestObject that is created whenever
        a page is loaded. The render() method displays templates to the user."""
    return render(request, 'hello_world.html', {})
