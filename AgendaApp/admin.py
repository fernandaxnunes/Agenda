from django.contrib import admin
from AgendaApp.models import Agenda, Cidade, Telefone, Interesse

class Telefones(admin.StackedInline):
    model = Telefone
    extra = 1

class AgendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'apelido', 'email']
    list_display_links = ['id', 'nome']
    list_filter = ['id', 'nome', 'apelido']
    search_fields = ['nome', 'id', 'apelido']
    inlines = [Telefones]
    filter_horizontal = ['interesses']

# Register your models here.
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Cidade)
admin.site.register(Telefone)
admin.site.register(Interesse)
