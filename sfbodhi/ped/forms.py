from django import forms
from .models import Person, Relationship


class RelationshipForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'gender']
        labels = {
            'name': 'New Person Name',
            'gender': 'Gender',
        }
        widgets = {
            'gender': forms.RadioSelect
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].required = True
        # Remove the '---------'
        self.fields['gender'].empty_label = None  # this is for ModelChoiceField, so next line is key
        self.fields['gender'].choices = Person.GENDER_CHOICES  # force only M and F

class ExistingRelationshipForm(forms.Form):
    from_person = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        label="Person"
    )
    to_person = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        label="Related Person"
    )
    relationship_type = forms.ChoiceField(
        choices=Relationship.RELATIONSHIP_CHOICES,
        label="Relationship Type"
    )