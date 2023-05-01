from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from .forms import ContactForm
from django.urls import reverse
# Create your views here.
def contact(request):
   contact_form = ContactForm()
   if request.method == "POST":
      contact_form = ContactForm(data=request.POST)
      if contact_form.is_valid():
         name = request.POST.get('name', '')
         email = request.POST.get('email', '')
         content = request.POST.get('content', '')
         #Envio de correo y redirecion
         email=  EmailMessage(
            "Nuevo mensaje de contacto",
            "De{} <{}>\n\nEscribió\n\n{}".format(name, email, content),
            "no-repley@inbox.mailtrap.io",
            ["el12mejor@outlook.com"],
            reply_to=[email]
         )
         try:
            #Todo bien, se redireciona a ok!
            email.send()
            return redirect(reverse('contact')+"?ok")
         except:
            return(reverse('contact'+"?fail"))
         
   return render(request, "contact/contact.html",{
      'form': contact_form 
   })