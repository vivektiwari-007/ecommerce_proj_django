from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import User, UserGroup, Permission
from setting.models import Role
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from ecommerce_vendor import settings
from django.contrib import messages
import getmac
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, "myapp/index.html")


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        # password = request.POST['username']

        if len(username) > 10:
            messages.error(request, "Username must be under the 10 characters")
            return redirect(register)

        if password != confirmpassword:
            messages.error(request, "new password or confirm password not match")
            return redirect(register)
        else:
            password = make_password(password)


        user = User(username=username,email=email,password=password)
        subject = "Greeting"
        message = "successfully account created"
        to = email
        res = send_mail(subject, message, settings.EMAIL_HOST_USER, [to])
        if res == 1:
            print("mail send successfully")
        else:
            print("mail not sent")
        user.save()
        return redirect(login)
    return render(request, "myapp/register.html")


def login(request):
    role = Role.objects.get(name="user")
    user = User.objects.filter(role_id=role.role_id)
    if request.method == "POST":
        username = request.POST['username']
        password =  request.POST['password']
        for i in user:
            if i.username != username:
                user = authenticate(username=username,password=password)
                if user is not None:
                    auth_login(request,user)
                    return redirect(index)
                else:
                    messages.info(request, "username or password is wrong")
            # messages.info(request, "username or password is wrong")
    return render(request, "myapp/login.html")



def logout(request):
    django_logout(request)
    return redirect(login)


def ChangePassword(request):
    currentpassword = request.user.password
    if request.method == "POST":
        oldpassword = request.POST.get('oldpassword')
        newpassword = request.POST['newpassword']
        newconfirmpassword = request.POST['newconfirmpassword']

        matchcheck = check_password(oldpassword, currentpassword)
        
        if matchcheck:
            if newpassword != newconfirmpassword:
                messages.error(request, "new password or confirm password not match")
            else:
                passw = User.objects.get(username=request.user.username)
                passw.set_password(newpassword)
                print(passw)
                passw.save()
                return redirect(login)
        else:
            messages.error(request, "Old password not match")
    return render(request, "myapp/change_password.html")



@login_required(login_url='/admin/')
def UserProfile(request):
    return render(request, "myapp/user_profile.html")


@login_required(login_url='/admin/')
def UpdateProfileView(request, user_id):
    user = User.objects.get(user_id=user_id)
    print(user)
    if request.method == "POST":
        username = user.username
        email = user.email
        password = user.password
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        code = request.POST.get('code')
        ip = getmac.get_mac_address()
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        delete_flag = request.POST.get('delete_flag')
        created_date = user.created_date
        if request.FILES:
            avatar = request.FILES['avatar']
        else:
            avatar = request.user.avatar

        user = User(user_id=user_id, username=username, email=email, password=password, first_name=first_name, last_name=last_name, code=code, ip=ip, address=address, phone_number=phone_number, 
                    created_by=created_by, modified_by=modified_by, delete_flag=delete_flag, avatar=avatar, created_date=created_date)
        user.save()
        return redirect(UserProfile)
    return render(request, "myapp/user_profile.html")


@login_required(login_url='/admin/')
def UserDetail(request):
    user = User.objects.all()
    count1= User.objects.filter(is_active=True).count()
    count2= User.objects.filter(is_active=False).count()
    return render(request, 'myapp/userdetail.html', {'user':user,'count1':count1,'count2':count2})


@login_required(login_url='/admin/')
def UserAdd(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password = make_password(password)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_group_id = request.POST['user_group_id']
        user_group = UserGroup.objects.get(pk=user_group_id)
        role_id = request.POST.get('role_id')
        roleid = Role.objects.get(pk=role_id) 
        avatar = request.FILES['avatar']
        is_active = request.POST['is_active']
        code = request.POST['code']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        ip = getmac.get_mac_address()
        user = User(username=username, email=email, password=password, first_name=first_name,
            last_name=last_name, user_group_id=user_group, role_id=roleid, avatar=avatar, is_active=is_active, 
            code=code, address=address, phone_number=phone_number, created_by=created_by,
            modified_by=modified_by, ip=ip)
        user.save()
        return redirect(UserDetail)
    usergroup = UserGroup.objects.all()
    role = Role.objects.all()
    return render(request, 'myapp/useradd.html', {'usergroup':usergroup, 'role':role})


@login_required(login_url='/admin/')
def UserUpdate(request, user_id):
    userupdate = User.objects.get(user_id=user_id)
    if request.method == "POST":
        username = userupdate.username
        email = userupdate.email
        password = userupdate.password
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_group_id = request.POST['user_group_id']
        user_group = UserGroup.objects.get(pk=user_group_id)
        role_id = request.POST.get('role_id')
        roleid = Role.objects.get(pk=role_id)
        is_active = request.POST['is_active']
        code = request.POST['code']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        created_date = userupdate.created_date
        ip = getmac.get_mac_address()
        if request.FILES:
            avatar = request.FILES['avatar']
        else:
            avatar = userupdate.avatar
        user = User(user_id=user_id, username=username, email=email, password=password, first_name=first_name,
            last_name=last_name, user_group_id=user_group, role_id=roleid, avatar=avatar, is_active=is_active, 
            code=code, address=address, phone_number=phone_number, created_by=created_by,
            modified_by=modified_by, ip=ip, created_date=created_date)
        user.save()
        return redirect(UserDetail)
    usergroup = UserGroup.objects.all()
    role = Role.objects.all()
    return render(request, 'myapp/useradd.html', {'usergroup':usergroup, 'role':role,'userupdate':userupdate})


@login_required(login_url='/admin/')
def UserDelete(request, user_id):
    user = User.objects.get(user_id=user_id)
    user.delete()
    return redirect(UserDetail)


@login_required(login_url='/admin/')
def UserGroupDetail(request):
    usergroup = UserGroup.objects.all()
    count1 = UserGroup.objects.filter(is_active=True).count()
    count2 = UserGroup.objects.filter(is_active=False).count()
    return render(request, "myapp/user_group_detail.html", {"usergroup":usergroup, 'count1':count1, 'count2':count2})


@login_required(login_url='/admin/')
def UserGroupAdd(request):
    if request.method == "POST":
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        usergroup = UserGroup(name=name, slug=slug, is_active=is_active,
        created_by=created_by, modified_by=modified_by)
        usergroup.save()
        return redirect(UserGroupDetail)
    return render(request, 'myapp/user_group_add.html')


@login_required(login_url='/admin/')
def UserGroupUpdate(request, group_id):
    usergroup = UserGroup.objects.get(group_id=group_id)
    if request.method == "POST":
        name = request.POST['name']
        slug = request.POST['slug']
        is_active = request.POST['is_active']
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        created_date = usergroup.created_date
        usergroup = UserGroup(group_id=group_id, name=name,slug=slug, is_active=is_active,
            created_by=created_by,modified_by=modified_by, created_date=created_date)
        usergroup.save()
        return redirect(UserGroupDetail)
    return render(request, "myapp/user_group_add.html", {"usergroup":usergroup})


@login_required(login_url='/admin/')
def UserGroupDelete(request, group_id):
    usergroup = UserGroup.objects.get(group_id=group_id)
    usergroup.delete()
    return redirect(UserGroupDetail)


def PermissionAdd(request, user_id):
    userdetail = User.objects.get(user_id=user_id)
    permissions = Permission.objects.filter(user_id=user_id)
    if request.method == "POST":
        if request.POST['action_form'] == 'add':
            user_id = request.POST.get('user_id')
            userid = User.objects.get(pk=user_id)
            permission = request.POST.getlist('permission[]')
            permissiondetail = Permission(user_id=userid, json_permission=permission)
            permissiondetail.save()
        elif request.POST['action_form'] == 'update':
            permissiondetail = Permission.objects.get(permission_id=request.POST['action_form_update_id'])
            user_id = request.POST.get('user_id')
            userid = User.objects.get(pk=user_id)
            permission = request.POST.getlist('permission[]')
            permissiondetail = Permission(permission_id=request.POST['action_form_update_id'], user_id=userid, json_permission=permission)
            permissiondetail.save()
        # elif request.POST['action_form'] == 'update':
    if permissions:
        # permissions.json_permission = "".join("".join(permissions.json_permission.split("['")).split("']")).split("', '")
        # varient.sort_order_value = "".join("".join(varient.sort_order_value.split("['")).split("']")).split("', '")
        # res = {}
        # for key in varient.varient_value:
        #     for value in varient.sort_order_value:
        #         res[key] = value
        #         varient.sort_order_value.remove(value)
        #         break
        print('gussa')
        return render(request, 'myapp/permissionadd.html', {'userdetail':userdetail,'permissions':permissions[0]})
    return render(request, 'myapp/permissionadd.html', {'userdetail':userdetail})
