from django.shortcuts import render, redirect
from django.http import HttpRequest
from markdown2 import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, page):
    content = util.get_entry(page)
    if content == None:
        return render(request, "encyclopedia/error.html")
    return render(request, "encyclopedia/entry.html", {
        "title": page,
        "content": content,
    })


