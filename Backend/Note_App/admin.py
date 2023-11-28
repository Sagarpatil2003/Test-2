from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display=('title','content','created_at')
    search_fields = ('title','content')
    list_filter=('created_at',)

admin.site.register(Note,NoteAdmin)