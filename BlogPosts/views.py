from django.shortcuts import render
from django.http import HttpResponse


# Test html for page
html = '<html lang="en-US">' \
            '<body>' \
                '<h1>Test Page!</h1>' \
                '<ul>' \
                    '<li>TestList</li>' \
                '</ul>' \
            '</body>' \
       '</html>'


def post_view(request):
    return HttpResponse(html);
