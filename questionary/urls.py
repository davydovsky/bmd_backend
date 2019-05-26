from django.urls import path
from questionary import views

urlpatterns = [
    path('questionaries/', views.QuestionaryListView.as_view(), name='questionary-list'),
    path('questionaries/<uuid:pk>/', views.QuestionaryDetailView.as_view(), name='questionary-detail'),
    path('questionary-status/', views.QuestionaryStatusListView.as_view(), name='questionary-status-list'),
    path('questionary-status/<int:pk>/', views.QuestionaryStatusDetailView.as_view(), name='questionary-status-detail'),
    path('questionary-fields/', views.QuestionaryFieldsListView.as_view(), name='questionary-fields-list'),
    path('questionary-fields/<int:pk>/', views.QuestionaryFieldsDetailView.as_view(), name='questionary-fields-detail'),
    path('document-templates/', views.DocumentTemplateListView.as_view(), name='document-template-list'),
    path('document-templates/<int:pk>/', views.DocumentTemplateDetailView.as_view(), name='document-template-detail'),
    path('delete-accepted/', views.DeleteAcceptedView.as_view(), name='delete-accepted'),
    path('delete-rejected/', views.DeleteRejectedView.as_view(), name='delete-rejected'),
]
