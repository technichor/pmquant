from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import ideas
# Register your models here.

@admin.register(ideas)
class IdeaAdmin(ImportExportModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('id','title','description','author','elo_score','created')
    list_filter = ('status','created','modified','release')
    search_fields = ('title', 'author', 'description')
    # raw_id_fields = ('',)
    # date_hiearchy = 'created'
    ordering = ('-created','title')