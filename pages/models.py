from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.urls import reverse
from django.db import models
from django.conf import settings
from django.core.mail import send_mail

class AccountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have an email address')
        user = self.model(
            username=username,
            email=email,
          )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email, password=None):
        user = self.create_user(
             username,
             email=email,
             password=password,
          )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    sex_choice = ((0, '生理女'),(1, '生理男'))
    identity = ((0, '顧客'), (1, '廠商'))
    type = models.IntegerField(choices=identity, default=False, blank=True, null=False)
    username = models.CharField(max_length=150, unique=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    gender = models.IntegerField(choices=sex_choice, default=1, blank=True, null=True)
    date_of_birth = models.DateField(null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False,
                                    help_text="Designates whether the user can log into this admin site.", )
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = AccountManager()
    USERNAME_FIELD= "username"
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def is_staff(self):
        return self.is_admin
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return self.is_admin

    def email_user(self, subject, message, from_email=None, **kwargs):
         """Send an email to this user."""
         send_mail(subject, message, from_email, [self.email], **kwargs)


# Create your models here.
class User(models.Model):
    user_image = models.ImageField(upload_to='image/')
    user_name = models.CharField(max_length=30)
    user_email = models.CharField(max_length=30)
    user_date_of_birth = models.DateField()
    user_phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.user_name

#商品分類表
#模型類
class GoodsCategory(models.Model):
    cag_name = models.CharField(max_length=30)
    cag_css = models.CharField(max_length=20)
    cag_img = models.ImageField(upload_to='cag')

#商品表
#模型類
class GoodsInfo(models.Model):
    goods_name = models.CharField(max_length=100)
    goods_price = models.IntegerField(default=0)
    goods_desc = models.CharField(max_length=2000)
    goods_img = models.ImageField(upload_to='goods')
    goods_cag = models.ForeignKey('GoodsCategory', on_delete=models.CASCADE)
    goods_tag = models.CharField(max_length=100, blank=True, null=True)
    def get_absolute_url(self):
        # return f"/products/{self.id}/" #依據產品編號提取資料
        return reverse("detail", kwargs={"id": self.id})  # 動態依據搜尋路徑名稱提取資料

class favorite(models.Model):
    list = models.ForeignKey('GoodsInfo', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{}_{}".format(self.list)

