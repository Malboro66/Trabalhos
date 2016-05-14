from datetime import datetime
from decimal import Decimal

from . import engine, Session
from .models import Base, Grupo, Cliente, Agencia, Conta, Emprestimo, Depositante, Devedor, CartaoCredito


Base.metadata.create_all(engine)

db = Session()
db.add_all([
    Grupo(nome='MyBank',
          razao_social='MyBank International SA',
          cnpj='11.222.333/0001-44'),

    Cliente(nome='Ana',
            rua='XV de Novembro',
            cidade='Joinville',
            nascimento=datetime(1980, 8, 6)),
    Cliente(nome='Laura',
            rua='07 de Setembro',
            cidade='Blumenau',
            nascimento=datetime(1981, 8, 8)),
    Cliente(nome='Vânia',
            rua='01 de Maio',
            cidade='Blumenau',
            nascimento=datetime(1982, 8, 6)),
    Cliente(nome='Franco',
            rua='Felipe Schmidt',
            cidade='Florianopolis',
            nascimento=datetime(1985, 8, 6)),
    Cliente(nome='Eduardo',
            rua='Beria Mar Norte',
            cidade='Florianópolis',
            nascimento=datetime(1970, 11, 10)),
    Cliente(nome='Bruno',
            rua='24 de maio',
            cidade='Criciúma',
            nascimento=datetime(1982, 7, 5)),
    Cliente(nome='Rodrigo',
            rua='06 de agosto',
            cidade='Joinville',
            nascimento=datetime(1981, 8, 6)),
    Cliente(nome='Ricardo',
            rua='João Colin',
            cidade='Joinville',
            nascimento=datetime(1980, 2, 15)),
    Cliente(nome='Alexandre',
            rua='Margem esquerda',
            cidade='Blumenau',
            nascimento=datetime(1980, 3, 7)),
    Cliente(nome='Luciana',
            rua='Estreito',
            cidade='Florianópolis',
            nascimento=datetime(1987, 9, 6)),
    Cliente(nome='Juliana',
            rua='Iririu',
            cidade='Joinville',
            nascimento=datetime(1970, 1, 6)),
    Cliente(nome='Pedro',
            rua='Aventureiro',
            cidade='Joinville',
            nascimento=datetime(1975, 6, 8)),
    Cliente(nome='Julia',
            rua='Nova Brasília',
            cidade='Joinville',
            nascimento=datetime(1985, 3, 18)),

    Agencia(nome='Verde Vale',
            cidade='Blumenau',
            fundos=Decimal('900000'),
            grupo_codigo=1),
    Agencia(nome='Cidade das Flores',
            cidade='Joinville',
            fundos=Decimal('800000'),
            grupo_codigo=1),
    Agencia(nome='Universitária',
            cidade='Florianópolis',
            fundos=Decimal('750000'),
            grupo_codigo=1),
    Agencia(nome='Joinville',
            cidade='Joinville',
            fundos=Decimal('950000'),
            grupo_codigo=1),
    Agencia(nome='Beira Mar',
            cidade='Florianópolis',
            fundos=Decimal('600000'),
            grupo_codigo=1),
    Agencia(nome='Criciúma',
            cidade='Criciúma',
            fundos=Decimal('500000'),
            grupo_codigo=1),
    Agencia(nome='Blumenau',
            cidade='Blumenau',
            fundos=Decimal('1100000'),
            grupo_codigo=1),
    Agencia(nome='Germânia',
            cidade='Blumenau',
            fundos=Decimal('400000'),
            grupo_codigo=1),

    Conta(agencia_codigo=4,
          numero='C-401',
          cliente_codigo=1,
          saldo=500,
          abertura=datetime(2014, 1, 1)),
    Conta(agencia_codigo=4,
          numero='C-402',
          cliente_codigo=2,
          saldo=200,
          abertura=datetime(2014, 2, 27)),
    Conta(agencia_codigo=4,
          numero='C-403',
          cliente_codigo=3,
          saldo=350,
          abertura=datetime(2013, 7, 21)),
    Conta(agencia_codigo=4,
          numero='C-404',
          cliente_codigo=7,
          saldo=870,
          abertura=datetime(2013, 8, 11)),
    Conta(agencia_codigo=1,
          numero='C-101',
          cliente_codigo=11,
          saldo=800,
          abertura=datetime(2013, 8, 3)),
    Conta(agencia_codigo=2,
          numero='C-201',
          cliente_codigo=4,
          saldo=800,
          abertura=datetime(2014, 1, 1)),
    Conta(agencia_codigo=3,
          numero='C-301',
          cliente_codigo=5,
          saldo=400,
          abertura=datetime(2014, 1, 1)),
    Conta(agencia_codigo=5,
          numero='C-501',
          cliente_codigo=6,
          saldo=300,
          abertura=datetime(2014, 1, 1)),
    Conta(agencia_codigo=6,
          numero='C-601',
          cliente_codigo=8,
          saldo=900,
          abertura=datetime(2014, 1, 1)),
    Conta(agencia_codigo=7,
          numero='C-701',
          cliente_codigo=9,
          saldo=550,
          abertura=datetime(2014, 1, 1)),
    Conta(agencia_codigo=8,
          numero='C-801',
          cliente_codigo=10,
          saldo=1000,
          abertura=datetime(2014, 1, 1)),

    Emprestimo(agencia_codigo=4,
               cliente_codigo=1,
               codigo='L-10',
               total=2000),
    Emprestimo(agencia_codigo=2,
               cliente_codigo=4,
               codigo='L-20',
               total=1500),
    Emprestimo(agencia_codigo=4,
               cliente_codigo=2,
               codigo='L-15',
               total=1800),
    Emprestimo(agencia_codigo=4,
               cliente_codigo=3,
               codigo='L-30',
               total=2500),
    Emprestimo(agencia_codigo=6,
               cliente_codigo=8,
               codigo='L-40',
               total=3000),
    Emprestimo(agencia_codigo=1,
               cliente_codigo=11,
               codigo='L-35',
               total=2800),
    Emprestimo(agencia_codigo=4,
               cliente_codigo=7,
               codigo='L-50',
               total=2300),

    Depositante(agencia_codigo=4,
                conta_numero='C-401',
                cliente_codigo=1,
                valor=500,
                data=datetime(2014, 1, 1)),
    Depositante(agencia_codigo=4,
                conta_numero='C-402',
                cliente_codigo=2,
                valor=200,
                data=datetime(2014, 2, 27)),
    Depositante(agencia_codigo=4,
                conta_numero='C-403',
                cliente_codigo=3,
                valor=350,
                data=datetime(2013, 7, 21)),
    Depositante(agencia_codigo=2,
                conta_numero='C-201',
                cliente_codigo=4,
                valor=800,
                data=datetime(2013, 4, 12)),
    Depositante(agencia_codigo=3,
                conta_numero='C-301',
                cliente_codigo=5,
                valor=400,
                data=datetime(2014, 7, 4)),
    Depositante(agencia_codigo=4,
                conta_numero='C-404',
                cliente_codigo=7,
                valor=870,
                data=datetime(2013, 8, 11)),
    Depositante(agencia_codigo=5,
                conta_numero='C-501',
                cliente_codigo=6,
                valor=300,
                data=datetime(2011, 3, 23)),
    Depositante(agencia_codigo=6,
                conta_numero='C-601',
                cliente_codigo=8,
                valor=900,
                data=datetime(2013, 10, 12)),
    Depositante(agencia_codigo=7,
                conta_numero='C-701',
                cliente_codigo=9,
                valor=550,
                data=datetime(2011, 9, 2)),
    Depositante(agencia_codigo=8,
                conta_numero='C-801',
                cliente_codigo=10,
                valor=1000,
                data=datetime(2007, 8, 1)),
    Depositante(agencia_codigo=1,
                conta_numero='C-101',
                cliente_codigo=11,
                valor=800,
                data=datetime(2013, 8, 3)),

    Devedor(agencia_codigo=4,
            cliente_codigo=1,
            emprestimo_codigo='L-10',
            saldo=1000),
    Devedor(agencia_codigo=2,
            cliente_codigo=4,
            emprestimo_codigo='L-20',
            saldo=500),
    Devedor(agencia_codigo=4,
            cliente_codigo=2,
            emprestimo_codigo='L-15',
            saldo=800),
    Devedor(agencia_codigo=4,
            cliente_codigo=3,
            emprestimo_codigo='L-30',
            saldo=2000),
    Devedor(agencia_codigo=6,
            cliente_codigo=8,
            emprestimo_codigo='L-40',
            saldo=2000),
    Devedor(agencia_codigo=1,
            cliente_codigo=11,
            emprestimo_codigo='L-35',
            saldo=2600),
    Devedor(agencia_codigo=4,
            cliente_codigo=7,
            emprestimo_codigo='L-50',
            saldo=2300),

    CartaoCredito(agencia_codigo=1,
                  cliente_codigo=12,
                  codigo='1111-2222-3333-4444',
                  limite=1000),
    CartaoCredito(agencia_codigo=4,
                  cliente_codigo=13,
                  codigo='1234-4567-8910-1112',
                  limite=1000),
    CartaoCredito(agencia_codigo=4,
                  cliente_codigo=13,
                  codigo='2222-3333-4444-5555',
                  limite=2000),
])
db.commit()
