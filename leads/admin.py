from django.contrib import admin

from .models import User, Lead, Agent, UserProfile, Category, FollowUp, Order


class LeadAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    list_display_links = ['first_name']
    search_fields = ['first_name', 'last_name', 'email']


admin.site.register(Category)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Lead, LeadAdmin)
admin.site.register(Agent)
admin.site.register(FollowUp)
admin.site.register(Order)
