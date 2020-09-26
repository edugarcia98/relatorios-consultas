from django.contrib import admin
from app.models import *

# Register your models here.
class ConsultaAdmin(admin.ModelAdmin):
    #list_display = ("gasto_consulta", "qtd_exames")
    readonly_fields = [
        "gasto_consulta",
        "qtd_exames"
    ]

admin.site.register(Medico)
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Exame)