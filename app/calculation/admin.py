from django.contrib import admin
from .models import Calculation

class CalculationAdmin(admin.ModelAdmin):
    fields = (
        "num1",
        "num2",
        "symbol",
        "result",
        "update_date",
        "delete_date",
    )


admin.site.register(Calculation, CalculationAdmin)
