import random
import re

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw
from django.conf import settings

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.utils.six import BytesIO
from django.views import View

from LoginApp.models import AdminInfo
from LoginApp.serializers import UserSerializers


def login(request):
    if request.method == 'GET':
        return render(request, 'NETCTOSS_Demo/user/login.html')
    if request.method == 'POST':
        valicode = request.POST.get('valicode')
        verify_code = request.session.get('verify_code')

        b = re.search(r'^' + valicode + r'$', verify_code, re.I)

        context = dict()

        if b:
            username = request.POST.get('username')
            users = AdminInfo.objects.filter(admin_code=username)
            if users.count() > 0:
                user = users.first()
                password = request.POST.get('password')
                if password == user.password:
                    request.session['user_id'] = user.id

                    return redirect(reverse('login:index'), context={'user': user})
                else:
                    context['password_error_info'] = '密码错误!'
            else:
                context['username_error_info'] = '用户不存在!'
        else:
            context['valicode_error_info'] = '验证码错误!'

        return render(request, 'NETCTOSS_Demo/user/login.html', context=context)


def logout(request):
    request.session.flush()
    return redirect(reverse('login:login'))


def index(request):
    return render(request, 'NETCTOSS_Demo/main/index/index.html')


def get_code(request):
    # 初始化画布，初始化画笔

    mode = "RGB"

    size = (64, 34)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)

    imagefont = ImageFont.truetype(settings.FONT_PATH, 33)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(16 * i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(100):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(201), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")


def get_color():
    return random.randrange(256)


def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    code = ""

    for i in range(4):
        code += random.choice(source)

    return code


class UserView(View):
    def get(self, request):
        user = AdminInfo.objects.get(pk=request.session.get('user_id'))
        userSerializers = UserSerializers(user)

        data = {
            'msg': '获取成功!',
            'status': 200,
            'data': userSerializers.data
        }

        return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})
