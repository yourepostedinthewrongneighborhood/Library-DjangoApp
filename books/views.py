from django.shortcuts import render
from django.http import HttpResponse


books = [
    {
        'ISBN': '1234567890',
        'year': '2020',
        'author': 'Berenfus K. A.',
        'title': "Big Black Nigger's Balls",
        'count': '200',
        'description': 'Long long description about that book'
    },
    {
        'ISBN': '1234567890',
        'year': '2020',
        'author': 'Kruk D. N.',
        'title': 'Boobs',
        'count': '2',
        'description': 'Book about SERIOUS honkers, a real set of BADONKERS, packing some DOHBANHONKOROS, MASSIVE BOHONKABHANKOLOOS'
    }
]


def home(request):
    context = {
        'books': books
    }
    return render(request, 'books/home.html', context)
