from django.contrib import admin
from App.models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'phone', 'email', 'age', 'location', 'gender', 'bio', 'created_at']
    search_fields = ['name', 'username', 'phone', 'email', 'age', 'location', 'gender']
    list_filter = ['gender']
    list_per_page = 10


admin.site.register(Member, MemberAdmin)
