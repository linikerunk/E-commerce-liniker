def formata_preco(value):
    return f'R${value:.2f}'.replace('.', ',')


def cart_total_qtd(carrinho):
    return sum([item['quantidade'] for item in carrinho.values() ])
