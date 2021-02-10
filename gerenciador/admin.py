from django.contrib import admin
from.models import estoque, categoria, produto, pedido
# Register your models here.
admin.site.register(estoque)
admin.site.register(categoria)
admin.site.register(produto)
admin.site.register(pedido)
