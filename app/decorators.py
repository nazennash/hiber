from functools import wraps
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def administrator_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_admin:
            return HttpResponseForbidden("You are not an administrator")
        return view_func(request, *args, **kwargs)
    return login_required(_wrapped_view)

def agent_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_agent:
            return HttpResponseForbidden("You are not an agent")
        return view_func(request, *args, **kwargs)
    return login_required(_wrapped_view)

def lead_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_lead:
            return HttpResponseForbidden("You are not a lead")
        return view_func(request, *args, **kwargs)
    return login_required(_wrapped_view)
