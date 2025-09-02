from django.contrib import admin
from .models import NewPost

@admin.register(NewPost)
class NewPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date_short')
    list_filter = ('pub_date', 'author')
    search_fields = ('title', 'short_description', 'text')
    readonly_fields = ('pub_date',)

    def pub_date_short(self, obj):
        return obj.pub_date.strftime('%d.%m.%Y')
    pub_date_short.short_description = 'Дата'
