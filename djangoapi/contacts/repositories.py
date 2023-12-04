from .models import Contact

class ContactRepository:
    @staticmethod
    def get_all_contacts():
        return Contact.objects.all()

    @staticmethod
    def get_contact_by_id(contact_id):
        return Contact.objects.get(pk=contact_id)
        
    @staticmethod
    def create_contact(data):
        return Contact.objects.create(**data)

    @staticmethod
    def update_contact(contact, data):
        for key, value in data.items():
            setattr(contact, key, value)
        contact.save()
        return contact

    @staticmethod
    def delete_contact(contact):
        contact.delete()