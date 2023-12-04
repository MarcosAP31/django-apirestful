from django.shortcuts import render
from rest_framework import generics
from .services import ContactService
from .serializers import ContactSerializer
# Create your views here.
class ContactListCreateView(generics.ListCreateAPIView):
    queryset = ContactService.get_all_contacts()
    serializer_class = ContactSerializer  # Make sure this line is present
    
    def get_serializer_class(self):
        return ContactSerializer

    def perform_create(self, serializer):
        ContactService.create_contact(serializer.validated_data)

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return ContactService.get_contact_by_id(self.kwargs['pk'])

    def perform_update(self, serializer):
        ContactService.update_contact(self.kwargs['pk'], serializer.validated_data)

    def perform_destroy(self, instance):
        ContactService.delete_contact(self.kwargs['pk'])
