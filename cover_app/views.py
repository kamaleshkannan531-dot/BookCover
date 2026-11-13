from django.shortcuts import render

def book_cover(request):
    """
    Renders the Book Back Cover Page Design.
    Ex. 05 - Web Application Development
    Student: V Kamalesh Kannan (26011247)
    """
    context = {
        'title': 'Mastering Full Stack Development & Artificial Intelligence',
        'subtitle': 'A Comprehensive Practical Guide for Engineers & Developers',
        'author': 'V Kamalesh Kannan',
        'edition': 'Second International Edition',
        'isbn': '978-93-89845-05-9',
        'price': '₹799 / $39.99',
    }
    return render(request, 'bookcover.html', context)
