from django.contrib import admin

from core.models import Categoria, Fornecedor, Tipo

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
