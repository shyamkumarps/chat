from django.contrib import admin
from web.models import Registration,Login,User,News_Feed,Message
# Register your models here.
#myModels = [models.Registration, models.Login, models.User,models.News_Feed,models.Message]
admin.register(Registration,Login,User,News_Feed,Message)(admin.ModelAdmin)