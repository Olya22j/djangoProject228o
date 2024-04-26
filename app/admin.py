from django.contrib import admin

from app.models import  ModelOla
# Register your models here.
import inspect
import app.models


ms = inspect.getmembers(app.models, inspect.isclass)
for model in ms: admin.site.register(model[1])