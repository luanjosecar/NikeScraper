from NikeScraper import NikeScraper
from objects import Product
import time
import keyboard

listaBase = []
newList = []


listaBase = NikeScraper()

while True:
    newItens = []
    newList = NikeScraper()
    i = 0
    for itens1 in newList:
        check = 0
        for itens2 in listaBase:
            print(itens2.name)
            if itens1.id == itens2.id:
                check = 1
                break
        if check == 0:
            newItens.append(itens1)

    if not newItens:
        print("Lista Vazia")
        print(listaBase[1].name)
    else:
        print(newItens)

    if keyboard.is_pressed("q"):
        print("Parando Execusão")
        break
    time.sleep(2)
    for base in listaBase:
        print(base.name)
    
            

    




