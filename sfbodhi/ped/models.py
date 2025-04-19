from django.db import models

# Create your models here.
class Person(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False)

    def __str__(self):
        return self.name
    
class Relationship(models.Model):
    RELATIONSHIP_CHOICES = [
        ('parent', 'Parent'),
        ('child', 'Child'),
        ('partner', 'Partner'),
        ('sibling', 'Sibling'),
    ]

    #Symmetrical & Directional Relationships (with implicit inverses)
    RELATIONSHIP_INVERSES = {
        'parent': 'child',
        'child': 'parent',
        'partner': 'partner',
        'sibling': 'sibling',
    }

    from_person = models.ForeignKey(
        Person,
        related_name='from_people',
        on_delete=models.CASCADE
    )
    to_person = models.ForeignKey(
        Person,
        related_name='to_people',
        on_delete=models.CASCADE
    )
    relationship_type = models.CharField(
        max_length=10,
        choices=RELATIONSHIP_CHOICES
    )

    #This constraint ensures that the same relationship type between two individuals cannot be entered multiple times
    class Meta:
        unique_together = ('from_person', 'to_person', 'relationship_type')

    def __str__(self):
        return f"{self.from_person} is {self.relationship_type} of {self.to_person}"
    

    #The save method now automatically creates the inverse relationship based on the RELATIONSHIP_INVERSES mapping.
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        inverse_type = self.RELATIONSHIP_INVERSES.get(self.relationship_type)
        if inverse_type:
            if not Relationship.objects.filter(
                from_person=self.to_person,
                to_person=self.from_person,
                relationship_type=inverse_type
            ).exists():
                Relationship.objects.create(
                    from_person=self.to_person,
                    to_person=self.from_person,
                    relationship_type=inverse_type
                )