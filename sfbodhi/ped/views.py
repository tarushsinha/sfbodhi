from django.shortcuts import render, redirect
from .forms import RelationshipForm
from .models import Person

def rishta_view(request):
    if request.method == 'POST':
        form = RelationshipForm(request.POST)
        if form.is_valid():
            # Save the new person
            new_person = Person.objects.create(name=form.cleaned_data['name'])
            # Here you can handle the relationship logic as needed
            return redirect('rishta')  # Replace with your desired redirect
    else:
        form = RelationshipForm()
    return render(request, 'rishta.html', {'form': form})
# Create your views here.
