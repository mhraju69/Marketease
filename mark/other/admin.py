from django.contrib import admin
from other.models import *
# Register your models here.
class serviceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('heading',)}
    
class blogadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    
    
    
admin.site.register(Service,serviceAdmin)

admin.site.register(Project)

admin.site.register(Blog,blogadmin)

admin.site.register(Message)

admin.site.register(Contact)

admin.site.register(Review)