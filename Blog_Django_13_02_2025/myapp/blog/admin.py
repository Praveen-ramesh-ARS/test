from django.contrib import admin
from .models import *
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title', 'content')
    list_filter = ('category', 'created_at')

#Resgister you models here
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(AboutUs)
