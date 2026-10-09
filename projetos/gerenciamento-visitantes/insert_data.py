import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from app.models import Visitor

# Mapear tipo de ingresso para número
ticket_type_map = {
    'VIP': 1,
    'Premium': 2
}

# Dados a inserir
visitors_data = [
    {
        'first_name': 'Zé',
        'last_name': '',
        'cpf': '19652192090',  # Remover formatação
        'birth_date': datetime.strptime('11/09/2001', '%d/%m/%Y').date(),
        'ticket_date': datetime.strptime('29/10/2026', '%d/%m/%Y').date(),
        'ticket_type': ticket_type_map['VIP'],
        'ticket_number': 'bbd693d9-fbe4-48e5-92ae-a11f1ceb5b4d'
    },
    {
        'first_name': 'Johnson',
        'last_name': '',
        'cpf': '83213526002',  # Remover formatação
        'birth_date': datetime.strptime('26/02/1999', '%d/%m/%Y').date(),
        'ticket_date': datetime.strptime('12/11/2026', '%d/%m/%Y').date(),
        'ticket_type': ticket_type_map['Premium'],
        'ticket_number': '446d5523-9989-4682-939e-eda29442bae5'
    },
    {
        'first_name': 'Zed',
        'last_name': '',
        'cpf': '39097476046',  # Remover formatação
        'birth_date': datetime.strptime('01/12/1993', '%d/%m/%Y').date(),
        'ticket_date': datetime.strptime('09/10/2026', '%d/%m/%Y').date(),
        'ticket_type': ticket_type_map['VIP'],
        'ticket_number': '40da93d4-949d-4f57-985b-854a5a0ca71b'
    }
]

# Inserir dados
for visitor_data in visitors_data:
    visitor = Visitor.objects.create(**visitor_data)
    print(f"✓ Visitante criado: {visitor.first_name} | CPF: {visitor.cpf} | Tipo: {'VIP' if visitor.ticket_type == 1 else 'Premium'}")

print("\n✓ Todos os visitantes foram inseridos com sucesso!")
