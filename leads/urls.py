from django.urls import path
from .views import (
    LeadListView, UnassignedLeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView, LeadArchiveView,
    AssignAgentView, CategoryListView,
    CategoryDetailView, LeadCategoryUpdateView, CategoryCreateView,
    CategoryUpdateView, CategoryDeleteView,
    FollowUpCreateView, FollowUpUpdateView, FollowUpDeleteView,
    lead_toggle_active,
)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('archive/', LeadArchiveView.as_view(), name='lead-archive'),
    path('archive/<int:pk>/', lead_toggle_active, name='lead-toggle-active'),
    path('unassigned/', UnassignedLeadListView.as_view(), name='unassigned-lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name='assign-agent'),
    path('<int:pk>/category/', LeadCategoryUpdateView.as_view(), name='lead-category-update'),
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
