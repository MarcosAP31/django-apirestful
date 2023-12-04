from django.db import models

class Contact(models.Model):
    ContactId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.EmailField()
    Phone = models.BigIntegerField()
    Address = models.TextField()
    Image = models.ImageField(upload_to='contact_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.Name} {self.LastName}"

    class Meta:
        db_table = 'contact'  # Set the desired table name



