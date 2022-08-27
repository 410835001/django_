from django.contrib import auth
from django.shortcuts import render, redirect
from .forms import LoginForm
from .forms import RegisterForm, GoodsInfoForm, favForm
from .forms import UpdateForm
from .models import GoodsInfo, favorite
from .models import User
from django.views.generic.base import View

# Create your views here.
def home_view(request, *args, **kwargs):
    home_form = GoodsInfoForm()
    products = GoodsInfo.objects.all()
    return render(request, "home.html", locals())

def navbar(request, *args, **kwargs):
    home_form = GoodsInfoForm()
    products = GoodsInfo.objects.all()
    return render(request, "navbar.html", locals())

def contact_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, "contact.html", context)


def sign_in(request, *args, **kwargs):

    return render(request, "sign.html")

def logout_view(request):
    auth.logout(request)
    return redirect('/home/')

def login_view(request):
    form = LoginForm()
    if request.user.is_authenticated:
        return redirect('../sign/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return redirect('../sign/')
    else:
        return render(request, 'login.html', locals())

def text_view(request):
    user = request.user
    form = UpdateForm(request.POST or None, instance=user)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/listall/')

    context = {'state': "更新資料",
        'form': form}
    return render(request, "text.html", context)

def car_view(request, *args, **kwargs):

    return render(request, "car.html")

def order_view(request, *args, **kwargs):

    return render(request, "order.html")

def material(request,*args, **kwargs):


    return render(request, "material.html")

def listall(request, *args, **kwargs):
    user = request.user
    form = UpdateForm(request.POST or None, instance=user)
    return render(request, "listall.html", locals())

def delete(request, *args, **kwargs):
    goods = GoodsInfo.objects.get(id=id)
    goods.delete()
    return render(request, "collect.html", locals())

def about(request, *args, **kwargs):

    return render(request, "about.html")

def collect(request, id, *args, **kwargs):

    form = favForm()

    return render(request, "collect.html", {'form': form})

def us(request, *args, **kwargs):

    return render(request, "us.html")

def detail(request, id, *args, **kwargs):
    products = GoodsInfo.objects.all()
    goods = GoodsInfo.objects.get(id=id)

    return render(request, "detail.html", {'goods': goods,
                                           'products': products})

class history(View):

    def get(self, request,goods_id):
        user = request.user
        if request.user.is_authenticated:

            history_key = 'history_%d' % user.username

        return render(request, "history.html")

def detail1(request, *args, **kwargs):

    products = GoodsInfo.objects.get(id=id)

    return render(request, "detail1.html", locals())



def detail3(request, *args, **kwargs):
    return render(request, "detail3.html")


def detail4(request, *args, **kwargs):
    return render(request, "detail4.html")


def detail5(request, *args, **kwargs):
    return render(request, "detail5.html")


def detail6(request, *args, **kwargs):
    return render(request, "detail6.html")


def detail7(request, *args, **kwargs):
    return render(request, "detail7.html")
