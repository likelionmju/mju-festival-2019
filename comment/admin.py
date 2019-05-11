from django.contrib import admin
from .models import BoardComment, LostComment

# Register your models here.
admin.site.register(BoardComment)
admin.site.register(LostComment)