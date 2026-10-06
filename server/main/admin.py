# main/admin.py
from django.apps import apps
from django.contrib import admin

# Get all models from the app
app = apps.get_app_config('main')

# Register each model dynamically
for model in app.get_models():
    admin.site.register(model)




