from .repositories import ContactRepository
from .serializers import ContactSerializer

class ContactService:
    @staticmethod
    def get_all_contacts():
        contacts = ContactRepository.get_all_contacts()
        serializer = ContactSerializer(contacts, many=True)
        return serializer.data

    @staticmethod
    def get_contact_by_id(contact_id):
        contact = ContactRepository.get_contact_by_id(contact_id)
        serializer = ContactSerializer(contact)
        return serializer.data

    @staticmethod
    def create_contact(data):
        serializer = ContactSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return ContactRepository.create_contact(serializer.validated_data)

    @staticmethod
    def update_contact(contact_id, data):
        contact = ContactRepository.get_contact_by_id(contact_id)
        serializer = ContactSerializer(instance=contact, data=data)
        serializer.is_valid(raise_exception=True)
        return ContactRepository.update_contact(contact, serializer.validated_data)

    @staticmethod
    def delete_contact(contact_id):
        contact = ContactRepository.get_contact_by_id(contact_id)
        ContactRepository.delete_contact(contact)