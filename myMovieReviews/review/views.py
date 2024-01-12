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
        "review" : review
    }
    return render(request, "review_read.html", context)

def review_create(request) :
    if request.method == "POST" :
        Review.objects.create(
            title = request.POST["title"],
            releasedate = request.POST["releasedate"],
            genre = request.POST["genre"],
            grade = request.POST["grade"],
            runningtime = int(request.POST["runningtime"]),
            runningtimehour = int(request.POST["runningtime"])//60,
            runningtimeminute = int(request.POST["runningtime"])%60,
            content = request.POST["content"],
            director = request.POST["director"],
            actor = request.POST["actor"],
        )
        return redirect("/reviews")
    return render(request, "review_create.html")

def review_update(request, pk) :
    review = Review.objects.get(id=pk)
    if request.method == "POST" :
        review.title = request.POST["title"]
        review.releasedate = request.POST["releasedate"]
        review.genre = request.POST["genre"]
        review.grade = request.POST["grade"]
        review.runningtime = int(request.POST['runningtime'])
        review.runningtimehour = int(request.POST['runningtime'])//60
        review.runningtimeminute = int(request.POST['runningtime'])%60
        review.content = request.POST["content"]
        review.director = request.POST["director"]
        review.actor = request.POST["actor"]
        review.save()
        return redirect(f"/reviews/{pk}")
    
    context={
        "review" : review
    }
    return render(request, "review_update.html", context)

def review_delete(request, pk) :
    if request.method == "POST" :
        review = Review.objects.get(id=pk)
        review.delete()
    return redirect("/reviews")