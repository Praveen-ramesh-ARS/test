
# Register your models here.
from django.contrib import admin
from .models import PredictionLog

@admin.register(PredictionLog)
class PredictionLogAdmin(admin.ModelAdmin):
    list_display = ("city", "prediction", "created_at")
    search_fields = ("city", "prediction")
    list_filter = ("prediction", "created_at")

