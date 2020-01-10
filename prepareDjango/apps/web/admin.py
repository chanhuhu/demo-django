from django.contrib import admin
# Register your models here.
from django.utils.html import format_html

from prepareDjango.apps.web.models import User, Post, Tag, Comment


class UserLogAdmin(admin.ModelAdmin):
    list_display = ("login_time", "username", "password")

    def my_btn(self, obj):
        return format_html(
            """
            <a href="#" class="btn--primary">submit</a>
            """,
            obj.id
        )


admin.site.register(User, UserLogAdmin)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)