from django.shortcuts import render, redirect
from .forms import RelationshipForm, ExistingRelationshipForm
from .models import Person, Relationship
from pyvis.network import Network
from django.http import HttpResponse
import os
from django.db import IntegrityError
from django.contrib import messages

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
            try:
                Relationship.objects.create(
                    from_person=from_person,
                    to_person=to_person,
                    relationship_type=relationship_type
                )
                messages.success(request, "Relationship created successfully.")
            except IntegrityError:
                messages.warning(request, "This relationship already exists.")
                # return redirect('designate_rishta')
            return redirect('designate_rishta')  # Replace with your desired redirect
    else:
        form = ExistingRelationshipForm()
    return render(request, 'designate_rishta.html', {'form': form})

def relationship_graph_view(request):
    net = Network(height="600px", width="100%", bgcolor="#ffffff", font_color="black")
    net.force_atlas_2based()

    people = Person.objects.all()
    relationships = Relationship.objects.all()

    for person in people:
        net.add_node(person.id, label=person.name)

    for rel in relationships:
        label = rel.relationship_type
        net.add_edge(rel.from_person.id, rel.to_person.id, label=label)

   # Use Django static folder
    output_file = "relationship_graph.html"
    output_path = os.path.join("static", output_file)

    # Instead of net.show() which tries to auto-open
    net.write_html(output_path)

    # Embed in iframe
    return HttpResponse(f'<iframe src="/static/{output_file}" width="100%" height="700"></iframe>')