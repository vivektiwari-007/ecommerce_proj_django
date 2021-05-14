from myapp.models import Permission
from django.http import HttpResponse
from django.shortcuts import redirect, render
from myapp.views import UserProfile, register

class BaseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)


class ProcessViewNoneMiddleware(BaseMiddleware):
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('----- Middleware view %s' % view_func.__name__)
        function1 = view_func.__name__
        print(function1)
        
        # print(permission[0].json_permission)
        # if request.user == .user_id:
        #     print(request.user)
        if not request.user.is_authenticated:
            return None
        else:
            permission = Permission.objects.filter(user_id=request.user)
            if function1 == "login" or function1 == "register" or function1 == "logout" or function1 == "index" or function1 == "PermissionAdd" or function1 == "UserProfile" or function1 == "UpdateProfileView" or function1 == "UserDetail" or function1 == "VarientInfo":
                return None
            else:
                if permission:
                    for i in permission[0].json_permission:
                        if i == function1:
                            return None
                        else:
                            continue
                            # return None
                            # return render(request, 'myapp/permissionnot.html')
                    # return render(request, 'myapp/permissionnot.html')
                    return None
                return None
        