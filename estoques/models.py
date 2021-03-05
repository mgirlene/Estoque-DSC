from django.db import models

class Estoque(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey("accounts.CustomUsuario", db_column='id_usuario', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        db_table = 'estoque'
