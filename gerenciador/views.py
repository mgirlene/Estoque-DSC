from django.views.generic.base import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from estoques.models import Estoque
from produtos.models import Produto
from vendas.models import Vendas
from django.db.models import Q
from django.db.models import Sum
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from Estoque.utils import render_to_pdf


class GeneratePDFVendas(View):
    def get(self, request, *args, **kwargs):

        vendas = Vendas.objects.order_by('data').filter(usuario=self.request.user)
        data = {'vendas': vendas}

        pdf = render_to_pdf('relatorio.html', data)

        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Relatorio_Vendas.pdf"
            content = 'attachment; filename=%s' % (filename)
            response['Content-Disposition'] = content
            return response
        else:
            return HttpResponse("Not found")


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_queryset(self):
        estoque = Estoque.objects.get(usuario=self.request.user.id)
        return estoque

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        est = Estoque.objects.filter(Q(usuario=self.request.user.id)).count()
        context['list_estoque'] = est

        estok = Estoque.objects.filter(Q(usuario=self.request.user.id))
        prod = Produto.objects.filter(estoque__in=estok).aggregate(qtd=Sum('quantidade'))['qtd']
        context['list_produto'] = prod

        venda = Vendas.objects.filter(Q(usuario=self.request.user.id)).count()
        context['list_venda'] = venda
        return context

        ##Gráficos##

    def home(request):
        return render(request, 'index.html')

    def vendas_chart(request):
        user = request.user.id
        labels = []
        data = []

        queryset = Vendas.objects.filter(usuario=user).values('produto__nome').annotate(Sum('quantidade'))[:10]
        for entry in queryset:
            labels.append(entry['produto__nome'])
            data.append(entry['quantidade__sum'])

        return JsonResponse(data={
            'labels': labels,
            'data': data,
        })

    def estoques_chart(request):
        user = request.user.id
        estoques = Estoque.objects.filter(usuario=user)

        labels1 = []
        data1 = []

        query = Produto.objects.filter(estoque__in=estoques).values('estoque__nome').annotate(Sum('quantidade'))[:10]
        for e in query:
            labels1.append(e['estoque__nome'])
            data1.append(e['quantidade__sum'])

        return JsonResponse(data={
            'labels1': labels1,
            'data1': data1,
        })
