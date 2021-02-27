from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        db_table = 'categoria'


def __str__(self):
    return '{}'.format(self.nome)


class Pedido(models.Model):
    numero = models.CharField(max_length=100)
    cliente = models.ForeignKey("accounts.CustomUsuario", db_column='id_usuario', on_delete=models.CASCADE)
    produto = models.ForeignKey("produtos.Produto", on_delete=models.CASCADE)

    class Meta:
        db_table = 'pedido'

        def __str__(self):
            return '{}'.format(self.id)
