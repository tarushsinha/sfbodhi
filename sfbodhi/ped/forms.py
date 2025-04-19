from django import forms
from .models import Person


class RelationshipForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    existing_person = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        required=False,
        empty_label="Select a person"
    )
    RELATIONSHIP_CHOICES = [
        ('parent', 'Parent'),
        ('child', 'Child'),
    ]
    relationship_type = forms.ChoiceField(choices=RELATIONSHIP_CHOICES)