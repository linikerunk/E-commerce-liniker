from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from produto.models import Variacao


# Create your views here.

class Pagar(View):
    template_name = 'pedido/pagar.html'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(
            self.request,
            'Você precisa realizar login'
            )
            return redirect('perfil:criar')

        if not self.request.session.get('carrinho'):
            messages.error(
            self.request,
            'Carrinho vazio.'
            )
            return redirect('produto:lista')

        carrinho = self.request.session.get('carrinho')
        carrinho_variacao_ids = [v for v in carrinho]
        bd_variacoes = list(Variacao.objects.select_related('produto').filter(id__in=carrinho_variacao_ids))


        for variacao in bd_variacoes:
            vid = str(variacao.id)
            estoque = variacao.estoque
            qtd_carrinho = carrinho[vid]['quantidade']
            preco_unt = carrinho[vid]['preco_unitario']
            preco_unt_promo = carrinho[vid]['preco_unitario_promocional']

            error_msg_estoque = ''

            if estoque < qtd_carrinho:
                carrinho[vid]['quantidade'] = estoque
                carrinho[vid]['preco_quantitativo'] = estoque * preco_unt
                carrinho[vid]['preco_quantitativo_promocional'] = estoque * \
                    preco_unt_promo

                error_msg_estoque = 'Estoque insuficiente para alguns produtos do seu carrinho.\
                            Reduzimos a quantidade desses produtos. Por favor, verifique \
                            no seu carrinho quais produtos foram afetados a seguir'

            if error_msg_estoque:
                messages.error(
                    self.request,
                    error_msg_estoque
                )
                
                self.request.session.save()
                return redirect('produto:carrinho')
            
        contexto = {

        }
        return render(self.request, self.template_name, contexto)



class SalvarPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Salvar Pedido')

class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')
