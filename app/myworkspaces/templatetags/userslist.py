from django import template
from django.utils import timezone
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.template.loader import get_template

register = template.Library()


def get_all_logged_in_users():
    # Query all non-expired sessions
    # use timezone.now() instead of datetime.now() in latest versions of Django
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []

    # Build a list of user ids from that query
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    # Query all logged in users based on id list
    return User.objects.filter(id__in=uid_list)


t = get_template('../templatetags/logged_in_user_list.html')
@register.inclusion_tag(t)
def render_logged_in_user_list():
    return { 'users': get_all_logged_in_users() }

