from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(State)
admin.site.register(District)
admin.site.register(SelfMgr)
admin.site.register(Post)
admin.site.register(Tag)
