from django.contrib import admin

# Register your models here.
from .models import *

# class PageAdmin(admin.ModelAdmin):
#     list_filter = ['author']
#
#     class Meta:
#         model = Post


admin.site.register(State)
admin.site.register(District)
# admin.site.register(SelfMgr)
# admin.site.register(Post)
admin.site.register(Tag)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ['author']
    list_display = ('title','created_date','update','author')

@admin.register(SelfMgr)
class SelfMgrAdmin(admin.ModelAdmin):
    list_display = ('name','district')