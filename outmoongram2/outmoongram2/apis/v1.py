from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.validators import validate_email, ValidationError

class BaseView(View):
    @staticmethod
    def response(data={}, message='', status=200):
        result = {
            'data': data,
            'message': message,
        }
        return JsonResponse(result, status=status)


class UserCreateView(BaseView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # 테스트하기 위해서 씁니다.
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        # Restful 하게 하기 위해선 POST, DELETE 다 나누어야 하지만, 편의상 POST만 사용
        username = request.POST.get('username', '')
        if not username:
            return self.response(message='아이디를 입력해 주세요.', status=400)
        password = request.POST.get('password', '')
        if not password:
            return self.response(message='비밀번호를 입력해 주세요.', status=400)
        email = request.POST.get('email', '')
        try:
            validate_email(email)
        except ValidationError:
            return self.response(message='올바른 이메일을 입력해 주세요.', status=400)


        user = User.objects.create_user(username, email, password)
        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return self.response(message='이미 존재하는 아이디입니다.', status=400)

        return self.response({'user.id': user.id})
