from django.shortcuts import render, redirect, HttpResponse
from .models import *

def reviews_list(request):
    reviews = Review.objects.all()
    context = {
        "reviews" : reviews
    }
    return render(request, 'review_list.html', context)

def review_read(request, pk) :
    review = Review.objects.get(id = pk)
    context = {
        "post" : post
    }

def review_create(request) :
    if request.method == "POST" :
        Review.objects.create(
            title = request.POST["title"],
            releasedate = request.POST["releasedate"],
            genre = request.POST["genre"],
            garde = request.POST["garde"],
            runningtime = request.POST["runningtime"],
            content = request.POST["content"],
            director = request.POST["director"],
            actor = request.POST["actor"],
        )
        return redirect("/reviews")
    return render(request, "review_create.html")