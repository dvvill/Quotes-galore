from django.contrib import admin
from .models.user import User

# Register user with admin
admin.site.register(User)
