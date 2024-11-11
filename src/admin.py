# src/admin.py
from django.contrib import admin
from django.apps import apps

# Get all models from the app
app = apps.get_app_config('src')

# Register each model dynamically
for model in app.get_models():
    admin.site.register(model)




