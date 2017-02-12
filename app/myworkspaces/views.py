#!env/bin/python
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError, JsonResponse
from django.template import Context, loader
from django.contrib.auth.models import User
from models import Comments
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
import redis
from django.utils import timezone


# Create your views here.
def index(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())


def workspaces(request):
    user = request.user
    return render(request, 'wp.html', locals())


def docs(request):
    template = loader.get_template("doc.html")
    return HttpResponse(template.render())


def board(request):
    template = loader.get_template("board.html")
    return HttpResponse(template.render())


@login_required
def chat(request):
    comments = Comments.objects.select_related().all()[0:]
    template = loader.get_template("chat.html")
    users = get_current_users()
    return render(request, 'chat.html', locals())

@login_required
def calendar(request):
    template = loader.get_template("calendar.html")
    return HttpResponse(template.render())

@csrf_exempt
def node_api(request):
    try:
        # Get User from sessionid
        session = Session.objects.get(session_key=request.POST.get('sessionid'))
        user_id = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(id=user_id)

        # Create comment
        Comments.objects.create(user=user, text=request.POST.get('comment'))

        # Once comment has been created post it to the chat channel
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        r.publish('chat', user.username + ': ' + request.POST.get('comment'))

        return HttpResponse("Everything worked :)")

    except Exception, e:
        return HttpResponseServerError(str(e))


def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    # Query all logged in users based on id list
    return User.objects.filter(id__in=user_id_list)


# def get_all_logged_in_users():
#     # Query all non-expired sessions
#     # use timezone.now() instead of datetime.now() in latest versions of Django
#     sessions = Session.objects.filter(expire_date__gte=timezone.now())
#     uid_list = []
#
#     # Build a list of user ids from that query
#     for session in sessions:
#         data = session.get_decoded()
#         uid_list.append(data.get('_auth_user_id', None))
#
#     # Query all logged in users based on id list
#     return User.objects.filter(id__in=uid_list)