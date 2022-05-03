from django.contrib import admin
from .models import Filme, Epsodio, Usuario
from django.contrib.auth.admin import UserAdmin

# Só existe porque a gente quer que no admin apareça o compo personalizado filmes_visto
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Filme)
admin.site.register(Epsodio)
admin.site.register(Usuario, UserAdmin)