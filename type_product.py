#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def buy_product(ts):
    o = {}
    d = {}
    total = 0

    for t in ts:
        d['price'] = int(t[1])
        d['quantity'] = 0
        name_product = (t[0])
        o[name_product] = d
        d = {}

    p = True

    while p:
        num = 0
        print("Realize su orden")
        for product, detail in o.items():
            num += 1
            print(
                "%s. %s | cantidad %s" % 
                (num, product, detail.get('quantity'))
            )
        choice_number = input("opcion: ")
        order_quantity = input("cantidad: ")
        choice = ts[(int(choice_number)-1)]
        previous_quantity = o.get(choice[0]).get('quantity')
        o.get(choice[0])['quantity'] =  int(order_quantity) \
                                        + int(previous_quantity)

        print("deseas pedir mas productos")
        op = input("si / no :")
        if op == "no":
            p = False
            print("Calculando pedido...")
        else:
            p = True
    
    print("______________________________________________________")
    print("Steel Store!!!")
    print("Nota de Pedido")
    print("______________________________________________________")
    print("Cant. | Producto        | Precio Unit.  | Sub. Total")
    for pt, dl in o.items():
        if dl.get('quantity') > 0:
            st = int(dl.get('quantity')) * int(dl.get('price'))
            total += st
            print(" %s    %s     %s             %s" % 
                (dl.get('quantity'), pt, dl.get('price'), st)
            )
    print("______________________________________________________")
    print("                                 Total  |  %s" % (total))
    print("¡Gracias por su compra!")


type_products = [
    ['angulo de 1" x 2.0', 20], ['Platina 1/2 x 1/8', 6 ], ['tubo redondo', 28], ['tubo cuadrado 1 1/2 x 1.2', 38], 
    ['angulo de 2" x 2.0', 20], ['doble', 25], ['tubo redondo 1 x 1.2', 28], ['tubo cuadrado 1 1/4 x 1.2', 30], 
]

buy_product(type_products)
