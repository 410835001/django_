from django.contrib import admin
from .models import Account
from .models import GoodsInfo, favorite

admin.site.register(Account)


admin.site.register(GoodsInfo)

admin.site.register(favorite)