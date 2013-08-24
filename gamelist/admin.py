from django.contrib import admin

from .models import Connection, Game


class ConnectionInline(admin.TabularInline):
    model = Connection


class GameAdmin(admin.ModelAdmin):
    inlines = [ConnectionInline]


admin.site.register(Game, GameAdmin)