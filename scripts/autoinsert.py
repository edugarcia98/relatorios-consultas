from app.models import *
import csv

def run():
    
    # Inserindo médicos e consultas
    Medico.objects.all().delete()
    Consulta.objects.all().delete()
    Exame.objects.all().delete()

    with open('data/consulta.csv', newline='') as csvconsulta:
        reader = csv.DictReader(csvconsulta, delimiter=';')
        for row in reader:
            medico, created = Medico.objects.get_or_create(
                cod_medico=row['cod_medico'],
                nome_medico=row['nome_medico']
            )

            if created:
                medico.save()
                print('Cadastrou Médico:', medico)
            
            consulta, created = Consulta.objects.get_or_create(
                numero_guia=row['numero_guia'],
                medico=medico,
                data_consulta=row['data_consulta'],
                valor_consulta=row['valor_consulta']
            )

            if created:
                consulta.save()
                print('Cadastrou Consulta:', consulta)

            with open('data/exames.csv', newline='') as csvexame:
                exame_reader = csv.DictReader(csvexame, delimiter=';')

                for item in exame_reader:
                    if item['numero_guia_consulta'] == consulta.numero_guia:
                        exame, created = Exame.objects.get_or_create(
                            consulta=consulta,
                            nome_exame=item['exame'],
                            valor_exame=item['valor_exame']
                        )

                        if created:     
                            exame.save()
                            print('Cadastrou Exame:', exame)