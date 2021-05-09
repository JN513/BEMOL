from django.shortcuts import render, redirect
from .models import Person
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "index.html")


def cadastrados(request):
    persons = Person.objects.all().order_by("-id")
    return render(request, "cadastrados.html", {"persons": persons})


def form(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        email = request.POST["email"]
        cep = request.POST["cep"]
        uf = request.POST["uf"]
        cidade = request.POST["cidade"]
        logradouro = request.POST["logradouro"]
        numero = request.POST["numero"]
        bairro = request.POST["bairro"]

        if not nome.strip():
            messages.error(request, "E necessario um nome")
            return redirect("form")
        if not email.strip():
            messages.error(request, "O campo email e obrigatorio")
            return redirect("form")
        if not cep.strip():
            messages.error(request, "O campo cep e obrigatorio")
            return redirect("form")
        if not uf.strip():
            messages.error(request, "O campo uf e obrigatorio")
            return redirect("form")
        if not cidade.strip():
            messages.error(request, "O campo cidade e obrigatorio")
            return redirect("form")
        if not logradouro.strip():
            messages.error(request, "O campo logradouro e obrigatorio")
            return redirect("form")
        if not numero.strip():
            messages.error(request, "O campo numero e obrigatorio")
            return redirect("form")
        if not bairro.strip():
            messages.error(request, "O campo bairro e obrigatorio")
            return redirect("form")

        if Person.objects.all().filter(email=email.strip()).exists():
            messages.error(request, "Email já utilizado")
            return redirect("form")

        person = Person(
            nome=nome,
            email=email,
            cep=cep,
            uf=uf,
            cidade=cidade,
            logradouro=logradouro,
            numero=numero,
            bairro=bairro,
        )

        person.save()

        messages.success(request, "Cadastro Realizado com sucesso")
        return redirect("cadastrados")

    return render(request, "form.html")
