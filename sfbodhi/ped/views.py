from django.shortcuts import render, redirect
from .forms import RelationshipForm, ExistingRelationshipForm
from .models import Person, Relationship

# Create your views here.

def persona_view(request):
    if request.method == 'POST':
        form = RelationshipForm(request.POST)
        if form.is_valid():
            form.save()
            # Here you can handle the relationship logic as needed
            return redirect('persona')  # Replace with your desired redirect
    else:
        form = RelationshipForm()
    return render(request, 'persona.html', {'form': form})

def designate_rishta_view(request):
    if request.method == 'POST':
        form = ExistingRelationshipForm(request.POST)
        if form.is_valid():
            from_person = form.cleaned_data['from_person']
            to_person = form.cleaned_data['to_person']
            relationship_type = form.cleaned_data['relationship_type']
            # Create the relationship; the model's save method handles inverse relationships
            Relationship.objects.create(
                from_person=from_person,
                to_person=to_person,
                relationship_type=relationship_type
            )
            return redirect('designate_rishta')  # Replace with your desired redirect
    else:
        form = ExistingRelationshipForm()
    return render(request, 'designate_rishta.html', {'form': form})