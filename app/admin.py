from django.contrib import admin
from .models import Recruit, StoreList, User

admin.site.register(StoreList)
admin.site.register(Recruit)
admin.site.register(User)
