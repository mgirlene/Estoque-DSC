from django.db import models

class estoque(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey("accounts.CustomUsuario", db_column='id_usuario', on_delete=models.CASCADE)

    class Meta:
        db_table = 'estoque'


def __str__(self):
    return '{}'.format(self.nome)


class categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        db_table = 'categoria'


def __str__(self):
    return '{}'.format(self.nome)


class produto(models.Model):
    nome = models.CharField(max_length=100)
    data_validade = models.DateTimeField(verbose_name="Data de Validade")
    preco = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantidade = models.IntegerField()
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    estoque = models.ForeignKey(estoque, on_delete=models.CASCADE)

    class Meta:
        db_table = 'produto'


def __str__(self):
    return '{}'.format(self.id)


class pedido(models.Model):
    numero = models.CharField(max_length=100)
    cliente = models.ForeignKey("accounts.CustomUsuario", db_column='id_usuario', on_delete=models.CASCADE)
    produto = models.ForeignKey(produto, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pedido'

        def __str__(self):
            return '{}'.format(self.id)
