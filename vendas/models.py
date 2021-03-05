from django.db import models


class Vendas(models.Model):
    numero = models.CharField(max_length=100)
    data = models.DateTimeField(verbose_name="Data")
    cliente = models.ForeignKey("accounts.CustomUsuario", db_column='id_usuario', on_delete=models.CASCADE)
    produto = models.ForeignKey("produtos.Produto", on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.nome)


    class Meta:
        db_table = 'vendas'
