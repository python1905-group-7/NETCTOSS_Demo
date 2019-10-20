from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from LoginApp.models import AdminInfo

LOGIN_REQUEST = [
    '/login/index/'
]

LOGIN_REQUEST_JSON = [
    '/login/get_user/'
]


class LoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user_id = request.session.get('user_id')
        if request.path in LOGIN_REQUEST:
            if user_id:
                user = AdminInfo.objects.get(pk=user_id)
                request.user = user
                print(request.user.id)
            else:
                return redirect(reverse('login:login'))

        if request.path in LOGIN_REQUEST_JSON:
            if not user_id:
                data = {
                    'msg': '未登录',
                    'status': 201
                }
                return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})
