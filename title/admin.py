from django.contrib import admin
from .models import Idea
from .models import Reviewer


admin.site.register(Idea)
admin.site.register(Reviewer)
