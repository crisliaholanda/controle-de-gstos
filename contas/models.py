from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255) 
    dt_criacao = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categoriaa'


class Transacao(models.Model):
    data = models.DateTimeField()
    descriacao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.descriacao

    def data_str(self):
        return self.data.strftime("%d/%m/%Y")

    def valo_rs(self):
        return 'R$ {}'.format(self.valor)

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'