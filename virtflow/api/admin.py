from django.contrib import admin
from django.apps import apps
from guardian.admin import GuardedModelAdmin

app = apps.get_app_config('api')
for model in app.get_models():
    admin.site.register(model, GuardedModelAdmin)
