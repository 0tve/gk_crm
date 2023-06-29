from django.urls import path

from .views import (AssignAgentView, CategoryCreateView, CategoryDeleteView,
                    CategoryDetailView, CategoryUpdateView,
                    FollowUpCreateView, FollowUpDeleteView, FollowUpUpdateView,
                    LeadArchiveView, LeadCreateView, CategoryListView,
                    LeadDeleteView, LeadDetailView, LeadListView,
                    LeadUpdateView, UnassignedLeadListView, lead_toggle_active, OrderUpdateView, 
                    export_leads_to_excel, import_leads_from_excel)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('archive/', LeadArchiveView.as_view(), name='lead-archive'),
    path('archive/<int:pk>/', lead_toggle_active, name='lead-toggle-active'),
    path('unassigned/', UnassignedLeadListView.as_view(), name='unassigned-lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/order/', OrderUpdateView.as_view(), name='lead-orders'),
    path('export/', export_leads_to_excel, name='lead-export'),
    path('import/', import_leads_from_excel, name='lead-import'),    
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name='assign-agent'),
    path('<int:pk>/followups/create/', FollowUpCreateView.as_view(), name='lead-followup-create'),
    path('followups/<int:pk>/', FollowUpUpdateView.as_view(), name='lead-followup-update'),
    path('followups/<int:pk>/delete/', FollowUpDeleteView.as_view(), name='lead-followup-delete'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('create-category/', CategoryCreateView.as_view(), name='category-create'),
    
]
