from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from LoginApp.models import AdminInfo

LOGIN_REQUEST = [
    '/login/index/'
]

LOGIN_REQUEST_JSON = [

]


class LoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path in LOGIN_REQUEST:

            user_id = request.session.get('user_id')
            if user_id:
                user = AdminInfo.objects.get(pk=user_id)
                request.user = user
            else:
                return redirect(reverse('login:login'))

        if request.path in LOGIN_REQUEST_JSON:
            pass
