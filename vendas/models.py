from django.db import models


class Vendas(models.Model):
    numero = models.CharField(max_length=100)
    data = models.DateTimeField(verbose_name="Data")
    cliente = models.CharField(max_length=100)
    produto = models.ForeignKey("produtos.Produto", on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    usuario = models.ForeignKey("accounts.CustomUsuario", db_column='id_usuario', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.quantidade)


    class Meta:
        db_table = 'vendas'
