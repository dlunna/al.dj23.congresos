from django.shortcuts import render, redirect
from .forms import CapturaForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here .

def captura (request):
    #para debugger si es get o POST
    print("Tipo de petición: {}".format(request.method))
    #
    # crea la plantilla vacia
    captura_form = CapturaForm()

    if request.method == "POST":
        # si recibe informacion por POST la carga en la plantilla
        captura_form = CapturaForm(data=request.POST)
        if captura_form.is_valid():
            nombre = request.POST.get('name', '')
            paterno = request.POST.get('father', '')
            materno = request.POST.get('mother', '')
            universidad = request.POST.get('university', '')
            celphone = request.POST.get('celphone', '')
            email = request.POST.get('email', '')
            # suponemos que todo va bien, a redireccionar
            #return redirect(reverse('reg_captura')+"?ok")

            # en vez de redireccionar se va a mandar email
            email = EmailMessage(
                "Bienvenido al congreso",
                "De {} <{}>\n\nEscribió:\n\n{}".format(nombre, email, universidad),
                "no-contestar@inbox.mailtrap.io",
                ["congreso@upp.edu.mx"],
                reply_to=[email]
            )

            try:
                email.send()
                return redirect(reverse('reg_captura')+"?ok")
            except:
                return redirect(reverse('reg_captura')+"?fail")
    
    return render(request, "registration/captura.html", {'form':captura_form})
