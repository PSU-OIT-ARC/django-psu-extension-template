from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from psu_base.classes.Log import Log
from psu_base.services import utility_service, message_service
from psu_base.decorators import require_authority, require_authentication


log = Log()


@require_authentication()
def index(request):
    """
    Menu of ...
    """
    log.trace()
    return render(
        request, 'index.html',
        {}
    )

