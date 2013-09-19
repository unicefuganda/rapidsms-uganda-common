from django.shortcuts import render
from uganda_common.models import Access

__author__ = 'kenneth'


class AccessMiddleWare(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path in ['/', '/accounts/login/', '/accounts/logout', '/national-pulse/', '/bestviz/']:
            return None
        if not 'wraps' in view_func.func_globals:
            return None
        if request.user.is_authenticated():
            try:
                access = Access.objects.get(user=request.user)
                if access.denied(request):
                    return render(request, '403.html', status=403)
            except Access.DoesNotExist:
                return None
        return None


class AccessTemplateMiddleWare(object):
    pass