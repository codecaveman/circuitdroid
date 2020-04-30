from django.contrib import admin

# Register your models here.
from .models import Circuit, Congregation, CircuitSection, CircuitOverseer, KingdomHall


# class CongregationInline(admin.TabularInline):
#     model = Congregation
#     extra = 10


# class CircuitAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Circuit Details', {'fields': [
#          'name', 'number']}),
#     ]
#     inlines = [CongregationInline]


admin.site.register(Circuit)
admin.site.register(CircuitOverseer)
admin.site.register(KingdomHall)
admin.site.register(CircuitSection)
