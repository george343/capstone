import json
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *


def index(request):
    page = "home"
    return render(request, "index.html", {"page": page})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {"message": "Invalid username and/or password!"})
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            try:
                user = User.objects.create_user(
                    username=username, password=password)
                user.save()
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            except IntegrityError:
                return render(request, "register.html", {"message": "Username taken"})
        else:
            return render(request, "register.html", {"message": "Passwords must match."})
    else:
        return render(request, "register.html")


# @login_required()
# def all(request):
#     videos = Video.objects.all()
#     return render(request, "index.html", {"videos": videos})


@api_view(('GET', 'POST'))
@login_required
def show_videos(request):
    videos = Video.objects.all()
    serializer = VideoSerializer(videos, many=True)
    return Response(serializer.data)


@api_view(('GET', 'POST'))
@login_required
def show_comments(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@login_required
def show_category(request, category):
    search = True
    videos = Video.objects.filter(category=category)
    return render(request, "category.html",
                  {"videos": videos, "category": category, "search": search})


@csrf_exempt
@login_required()
def show_profile(request, user):
    search = True
    page = "profile"
    if request.method == "POST":
        title = request.POST.get("title")
        category = request.POST.get("category")
        url = request.POST.get("url")
        url = url.replace(url[url.index("&"):], "").replace(
            "watch?v=", "embed/")
        picture = f"{url.replace('https://www.youtube.com/embed', 'http://img.youtube.com/vi')}/hqdefault.jpg"
        Video(title=title, category=category, url=url, picture=picture,
              user_upload=User.objects.get(username=user)).save()
    videos_uploaded = Video.objects.filter(
        user_upload=User.objects.get(username=user))
    videos_liked = Video.objects.filter(liked=User.objects.get(username=user))
    context = {"videos_uploaded": videos_uploaded,
               "videos_liked": videos_liked, "page": page, "search": search}
    return render(request, "profile.html", context)


@login_required()
def show_all(request):
    videos = Video.objects.all()
    page = "all"
    search = True
    return render(request, "all.html", {"videos": videos, "page": page, "search": search})


# @api_view(('POST', 'GET'))
@login_required
def show_video(request, id):
    video = Video.objects.get(pk=id)
    search = True
    videos = Video.objects.filter(category=video.category).exclude(pk=id)
    comments = Comment.objects.filter(video=video)
    if request.method == "POST":
        if "comment-btn" in request.POST:
            comment = request.POST.get("comment")
            commentor = User.objects.get(username=request.user)
            video = Video.objects.get(pk=id)
            Comment(comment=comment, commentor=commentor, video=video).save()
        elif "like" in request.POST:
            video.liked.add(User.objects.get(id=request.user.id))
    return render(request, "video.html",
                  {"video": video, "search": search, "videos": videos, "comments": comments})


@api_view(('PUT', 'GET'))
@login_required
def like_video(request, v_id):
    video = Video.objects.get(pk=v_id)
    if request.method == 'PUT':
        data = json.loads(request.body)
        video.liked.add(User)
        video.save()
        return HttpResponse(status=200)
    return HttpResponse(status=201)


def search_results(request, text):
    videos = Video.objects.filter(title__contains=text)
    return render(request, "results.html", {"videos": videos, "text": text, "search": True})
