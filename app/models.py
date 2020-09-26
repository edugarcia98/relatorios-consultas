from django.db import models
from django.db.models import Sum

# Create your models here.
class Medico(models.Model):
    cod_medico = models.IntegerField(primary_key=True, verbose_name="Código")
    nome_medico = models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self):
        return self.nome_medico
    
    class Meta:
        ordering = ('cod_medico',)
        verbose_name = ("Médico")
        verbose_name_plural = ("Médicos")

class Consulta(models.Model):
    numero_guia = models.IntegerField(primary_key=True, verbose_name="Guia")
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name="Médico")
    data_consulta = models.DateField(verbose_name="Data da Consulta")
    valor_consulta = models.FloatField(verbose_name="Valor da Consulta")

    
    def _get_gasto_consulta(self):
        return Exame.objects.filter(consulta=self).aggregate(Sum('valor_exame'))['valor_exame__sum']
    _get_gasto_consulta.short_description = "Gasto por Consulta"
    
    def _get_qtd_exames(self):
        return Exame.objects.filter(consulta=self).count()
    _get_qtd_exames.short_description = "Quantidade de Exames"
    
    gasto_consulta = property(_get_gasto_consulta)
    qtd_exames = property(_get_qtd_exames)

    def __str__(self):
        return '{} - Consulta com {} no dia {}'.format(self.numero_guia, self.medico.nome_medico, self.data_consulta)
    
    class Meta:
        ordering = ('numero_guia',)
        verbose_name = ("Consulta")
        verbose_name_plural = ("Consultas")

class Exame(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, verbose_name="Consulta")
    nome_exame = models.CharField(max_length=100, verbose_name="Nome")
    valor_exame = models.FloatField(verbose_name="Valor do Exame")

    def __str__(self):
        return 'Consulta {} - {}'.format(self.consulta.numero_guia, self.nome_exame)
    
    class Meta:
        ordering = ('consulta__numero_guia',)
        verbose_name = ("Exame")
        verbose_name_plural = ("Exames")