from django.db.models import Q
from django.shortcuts import render, redirect
from datetime import datetime, date
from uuid import uuid4
from validate_docbr import CPF

from .forms.create_visitor_form import CreateVisitorForm
from .models import Visitor, TicketType

# Create your views here.
def home(request):
    return render(request, 'home.html')

def visitors(request):
    search = request.GET.get('name_or_cpf', '').strip()
    ticket_type = request.GET.get('ticket_type', '0')

    visitors = Visitor.objects.all()

    visitors = visitors.filter(
        Q(first_name__icontains=search)
        | Q(last_name__icontains=search)
        | Q(cpf__contains=search)
    )

    valid_types = {str(value) for value in TicketType.values}

    ticket_type_int = int(ticket_type)

    if ticket_type in valid_types:
        visitors = visitors.filter(ticket_type=ticket_type_int)

    response = {
        'visitors': visitors,
        'search': search,
        'ticket_type': ticket_type_int
    }

    return render(request, 'visitors.html', response)

def create_visitor(request):
    if request.method == 'POST':
        visitor_form = CreateVisitorForm(request.POST)

        if visitor_form.is_valid():
            visitor = visitor_form.save(commit=False)
            visitor.ticket_number = str(uuid4())
            visitor.save()

            return redirect('visitors')
    else:
        visitor_form = CreateVisitorForm()

    response = {
        'form': visitor_form
    }

    return render(request, 'create-visitor.html', response)

def update_visitor(request, id):
    visitor = Visitor.objects.get(pk=id)
    if request.method == 'POST':
        visitor.first_name = request.POST['first_name']
        visitor.last_name = request.POST['last_name']
        visitor.cpf = request.POST['cpf']
        visitor.birth_date = datetime.strptime(request.POST['birth_date'], '%Y-%m-%d')
        visitor.ticket_date = datetime.strptime(request.POST['ticket_date'], '%Y-%m-%d')
        visitor.ticket_type = request.POST['ticket_type']

        visitor.save()

        return redirect('visitors')

    response = {
        'visitor': visitor    
    }

    return render(request, 'update-visitor.html', response)

def delete_visitor(request, id):
    visitor = Visitor.objects.get(pk=id)
    visitor.delete()

    return redirect('visitors')

def statistics(request):
    quant = 0
    quant_normal = 0
    quant_vip = 0
    quant_premium = 0
    idade = 0

    for object in Visitor.objects.all():
        quant += 1

    for object in Visitor.objects.filter(ticket_type = 1):
        quant_normal += 1

    for object in Visitor.objects.filter(ticket_type = 2):
        quant_vip += 1

    for object in Visitor.objects.filter(ticket_type = 3):
        quant_premium += 1

    hoje = date.today()
    idades = []

    for object in Visitor.objects.all():
        idade = hoje.year - object.birth_date.year

        if (hoje.month, hoje.day) < (object.birth_date.month, object.birth_date.day):
            idade -= 1

        idades.append(idade)

    idade_media = sum(idades) / len(idades)

    response = {
        'quant': quant,
        'quant_normal': quant_normal,
        'quant_vip': quant_vip,
        'quant_premium': quant_premium,
        'idade_media': idade_media
    }


    return render(request, 'statistics.html', response)