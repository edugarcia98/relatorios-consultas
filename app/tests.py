from django.test import TestCase

from .models import *

import datetime

# Create your tests here.
class RelatorioTestCase(TestCase):
    
    def setUp(self):
        medico1 = Medico(cod_medico=1, nome_medico='Medico1')
        medico1.save()

        medico2 = Medico(cod_medico=2, nome_medico='Medico2')
        medico2.save()

        data1 = datetime.date(2019, 4, 13)
        data2 = datetime.date(2019, 8, 2)

        consulta1 = Consulta(numero_guia=1, medico=medico1, data_consulta=data1, valor_consulta=50.0)
        consulta1.save()

        consulta2 = Consulta(numero_guia=2, medico=medico2, data_consulta=data2, valor_consulta=100.0)
        consulta2.save()

        exame1 = Exame(consulta=consulta1, nome_exame='HEMOGRAMA', valor_exame=10.0)
        exame1.save()

        exame2 = Exame(consulta=consulta2, nome_exame='HEMOGRAMA', valor_exame=15.0)
        exame2.save()

        exame3 = Exame(consulta=consulta2, nome_exame='RADIOGRAFIA', valor_exame=10.0)
        exame3.save()
    
    def test_count_consultas(self):
        self.assertEqual(Consulta.objects.all().count(), 2)
    
    def test_gasto_consulta(self):
        amostra_consulta1 = Consulta.objects.filter(numero_guia=1)[0]
        amostra_consulta2 = Consulta.objects.filter(numero_guia=2)[0]

        self.assertEqual(amostra_consulta1.gasto_consulta, 10)
        self.assertEqual(amostra_consulta2.gasto_consulta, 25)
    
    def test_qtd_exames(self):
        amostra_consulta1 = Consulta.objects.filter(numero_guia=1)[0]
        amostra_consulta2 = Consulta.objects.filter(numero_guia=2)[0]

        self.assertEqual(amostra_consulta1.qtd_exames, 1)
        self.assertEqual(amostra_consulta2.qtd_exames, 2)
    
    def test_filtro_medico(self):
        filtro = Consulta.objects.filter(medico__nome_medico__iexact='Medico1')
        self.assertEqual(filtro.count(), 1)
    
    def test_periodo_inicial(self):
        data_ini1 = datetime.date(2019, 4, 13) #data da consulta 1
        data_ini2 = datetime.date(2019, 8, 2) # data da consulta 2
        data_ini3 = datetime.date(2019, 3, 12) # data anterior a consultas
        data_ini4 = datetime.date(2019, 9, 12) # data posterior a consultas
        data_ini5 = datetime.date(2019, 5, 22) # data entre consultas

        filtro1 = Consulta.objects.filter(data_consulta__gte=data_ini1)
        filtro2 = Consulta.objects.filter(data_consulta__gte=data_ini2)
        filtro3 = Consulta.objects.filter(data_consulta__gte=data_ini3)
        filtro4 = Consulta.objects.filter(data_consulta__gte=data_ini4)
        filtro5 = Consulta.objects.filter(data_consulta__gte=data_ini5)

        self.assertEqual(filtro1.count(), 2)
        self.assertEqual(filtro2.count(), 1)
        self.assertEqual(filtro3.count(), 2)
        self.assertEqual(filtro4.count(), 0)
        self.assertEqual(filtro5.count(), 1)
    
    def test_periodo_final(self):
        data_fim1 = datetime.date(2019, 4, 13) #data da consulta 1
        data_fim2 = datetime.date(2019, 8, 2) # data da consulta 2
        data_fim3 = datetime.date(2019, 3, 12) # data anterior a consultas
        data_fim4 = datetime.date(2019, 9, 12) # data posterior a consultas
        data_fim5 = datetime.date(2019, 5, 22) # data entre consultas

        filtro1 = Consulta.objects.filter(data_consulta__lte=data_fim1)
        filtro2 = Consulta.objects.filter(data_consulta__lte=data_fim2)
        filtro3 = Consulta.objects.filter(data_consulta__lte=data_fim3)
        filtro4 = Consulta.objects.filter(data_consulta__lte=data_fim4)
        filtro5 = Consulta.objects.filter(data_consulta__lte=data_fim5)

        self.assertEqual(filtro1.count(), 1)
        self.assertEqual(filtro2.count(), 2)
        self.assertEqual(filtro3.count(), 0)
        self.assertEqual(filtro4.count(), 2)
        self.assertEqual(filtro5.count(), 1)
    
    def test_periodo(self):
        data_ini = datetime.date(2019, 4, 13)
        data_fim = datetime.date(2019, 8, 2)

        filtro = Consulta.objects.filter(data_consulta__gte=data_ini)
        filtro = filtro.filter(data_consulta__lte=data_fim)

        self.assertEqual(filtro.count(), 2)


