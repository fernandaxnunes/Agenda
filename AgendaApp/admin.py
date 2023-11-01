from django.contrib import admin
from AgendaApp.models import Agenda, Cidade

class AgendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'apelido', 'email']
    list_display_links = ['id', 'nome']
    list_filter = ['id', 'nome', 'apelido']
    search_fields = ['nome', 'id', 'apelido']
    

# Register your models here.
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Cidade)
