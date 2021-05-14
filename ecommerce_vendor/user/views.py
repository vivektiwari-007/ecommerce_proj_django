from django.shortcuts import render, redirect
from setting.models import Role
from catalog.models import Product
from myapp.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as django_logout
# Create your views here.


def index(request):
    return render(request, 'user/index.html')


def register(request):
    role = Role.objects.get(name="user")
    if request.method == "POST":
        print("hello")
        # first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_passsword = request.POST.get('confirm_passsword')
        role_id = request.POST.get('role_id')
        roleid = Role.objects.get(pk=role_id)
        if password != confirm_passsword:
            print(password)
            messages.error(request, "new password or confirm password not match")
            return redirect(register)
        else:
            password = make_password(password)
        user = User(username=email, email=email, password=password, role_id=roleid)
        user.save()
        return redirect(login)
    print("hiiii")
    return render(request, 'user/registration.html', {'role':role})


def login(request):
    role = Role.objects.get(name="user")
    user = User.objects.filter(role_id=role.role_id)
    # for i in user:
    #     return i
    if request.method == "POST":
        username = request.POST['username']
        password =  request.POST['password']
        role_id = request.POST.get('role_id')
        roleid = Role.objects.get(pk=role_id)
        print(username)
        userdetail = []
        for i in user:
            userdetail.append(i)
            if i.username == username:
                user = authenticate(username=username,password=password)
                if user is not None:
                    auth_login(request,user)
                    return redirect(index)
                else:
                    print("hello")
                    messages.info(request, "username or password is wrong")
            else:
                print("hii")
                messages.info(request, "username or password is wrong")
    return render(request, 'user/login.html', {'role':role})


def logout(request):
    django_logout(request)
    return redirect(login)


def product_detail(request):
    product = Product.objects.all()
    return render(request, 'user/product_detail.html', {'product':product})
# def password_reset_email(request):
#     return render(request, 'registration/user_password_reset_email.html')


# from django.contrib.auth.tokens import default_token_generator
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template import loader
# from django.core.mail import send_mail
# # from ..ecommerce_ settings import DEFAULT_FROM_EMAIL
# from django.views.generic import FormView
# from .forms import PasswordResetRequestForm
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.db.models.query_utils import Q


# class ResetPasswordRequestView(FormView):
#     template_name = "user/index.html"
#     success_url = '/login'
#     form_class = PasswordResetRequestForm

#     def form_valid(self, *args, **kwargs):
#         form = super(ResetPasswordRequestView, self).form_valid(*args, **kwargs)
#         data= form.cleaned_data["email_or_username"]
#         user= User.objects.filter(Q(email=data)|Q(username=data)).first()
#         if user:
#             c = {
#                 'email': user.email,
#                 'domain': self.request.META['HTTP_HOST'],
#                 'site_name': 'your site',
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'user': user,
#                 'token': default_token_generator.make_token(user),
#                 'protocol': self.request.scheme,
#             }
#             email_template_name='registration/user_password_reset_email.html'
#             subject = "Reset Your Password"
#             email = loader.render_to_string(email_template_name, c)
#             send_mail(subject, email, [user.email], fail_silently=False)
#         messages.success(self.request, 'An email has been sent to ' + data +" if it is a valid user.")
#         return form