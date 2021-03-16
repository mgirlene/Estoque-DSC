from django.db import models


# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantidade = models.IntegerField()
    categoria = models.ForeignKey("gerenciador.Categoria", on_delete=models.CASCADE)
    estoque = models.ForeignKey("estoques.Estoque", on_delete=models.CASCADE)


    def __str__(self):
        return '{}'.format(self.quantidade)

    class Meta:
        db_table = 'produto'
