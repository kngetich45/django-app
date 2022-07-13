
from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.frontend, name="frontend"),
    
    path('login/', include('django.contrib.auth.urls')),

#--------------- backend ---------------------------|
# Backend section.
path('backend/', views.backend, name="backend"),
# Add member.
path('add_member', views.add_member, name="add_member"),
# Edit member.
path('member/<str:member_id>', views.member, name="member"),
# Edit member.
path('edit_member', views.edit_member, name="edit_member"),
# Delete member.
path('delete_member/<str:member_id>', views.delete_member, name="delete_member"),
]
