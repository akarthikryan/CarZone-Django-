from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Contact

def contact(request):
    
    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        phone_number = request.POST.get("phone")
        message = request.POST.get("message")
        
        print("name",name)

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            phone_number=phone_number,
            message=message
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")

    return render(request, "contacts/contact.html")


def contact_details(request, contact_id):
    contact_data = get_object_or_404(Contact, id=contact_id)
    return render(request, "contacts/contact_details.html", {"contact": contact_data})
