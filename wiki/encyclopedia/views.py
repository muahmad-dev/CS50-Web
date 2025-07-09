from django.shortcuts import render, redirect
from markdown2 import markdown

from . import util
import random 


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, page_name):
    content = util.get_entry(page_name)
    if content is None:
        return render(request, "encyclopedia/3s.html", {
            "error": "Error: Page doesn't exist"
        })
    html_content = markdown(content)
    return render(request, "encyclopedia/entry.html", {
        "title": page_name,
        "content": html_content,
    })


def search(request):
    if request.method == "POST":
        value = request.POST.get("q")
        content = util.get_entry(value)
        if content == None:
            new_entry=[]
            entries = util.list_entries()
            for entry in entries:
                if value.lower() in entry.lower():
                    new_entry.append(entry)
            return render(request, "encyclopedia/search.html", {
                "entries": new_entry,
                "search": value,
            })
        else:
            return render(request, "encyclopedia/entry.html", {
                "title": value,
                "content": markdown(content)
            })
        
def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        markdowns = request.POST.get("markdown")
        entries = util.list_entries()
        if title in entries:
            return render(request, "encyclopedia/error.html", {
                "error": "Page with this title already exists"
            })
        util.save_entry(title, markdowns)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": markdown(markdowns),
        })
    else:
        return render(request, "encyclopedia/create.html")
    
def edit(request, page_name):
    title = page_name
    content = util.get_entry(title)
    if request.method == "GET":
        return render(request, "encyclopedia/edit.html", {
            "content": content,
        })
    elif request.method == "POST":
        new_content = request.POST.get("edit")
        util.save_entry(title, new_content)
        new_content = markdown(new_content)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": new_content,
        })

def randoms(request):
    entries = util.list_entries()
    lenght = len(entries)
    num = random.randint(0, lenght-1)
    return redirect("entry_page", page_name = entries[num])
