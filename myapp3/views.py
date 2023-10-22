from django.shortcuts import render

# Create your views here.
from .form import CreateContactForm
from .models import Contact
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

def home(request):
	contacts = Contact.objects.all()
	return render(request, 'myapp3/index.html', {'contacts': contacts})

def createcontact(request):
	if request.method == 'POST':
		form = CreateContactForm(request.POST)
		if form.is_valid():
			formdata=form.cleaned_data
			name = formdata['name']
			address = formdata['address']
			profession = formdata['profession']
			telnumber = formdata['telnumber']
			Contact.objects.create(name=name,address=address,profession=profession,telnumber=telnumber)
			contacts = Contact.objects.all()
			return render(request, 'myapp3/index.html', {'contacts': contacts})
	else:
		form = CreateContactForm()
	return render(request, 'myapp3/createcontact.html', {'form': form})

def delete_contact(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
        contact.delete()
    except Contact.DoesNotExist:
        pass  # Handle the case where the contact does not exist

    contacts = Contact.objects.all()
    return render(request, 'myapp3/index.html', {'contacts': contacts})

def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        form = CreateContactForm(request.POST)  # Create the form instance without the 'contact' parameter
        if form.is_valid():
            # Update the contact object with the form data
            contact.name = form.cleaned_data['name']
            contact.address = form.cleaned_data['address']
            contact.profession = form.cleaned_data['profession']
            contact.telnumber = form.cleaned_data['telnumber']
            contact.save()  # Save the updated contact object
    else:
        form = CreateContactForm(contact)  # Create the form instance with the 'contact' parameter
        return render(request, 'myapp3/edit.html', {'contact': contact, 'form': form})

    contacts = Contact.objects.all()
    return render(request, 'myapp3/index.html', {'contacts': contacts})  
