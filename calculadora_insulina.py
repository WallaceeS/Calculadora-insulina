import math
from decimal import Decimal, ROUND_HALF_UP
def menu():
    global op
    op = int(input("[1] Café\n[2] Almoço\n[3] Lanche da Tarde\n[4] Janta\n"))


def calcularCafe():
    soma = 0
    sucoUva = 0
    sucoLaranja = 0
    bolacha = 0
    qtBolacha = 0
    qtPao = 0
    while True:
        print("-=" *20)
        opcao = int(input("[1] Pão\n[2] Suco de uva\n[3] Suco de laranja\n[4] Bolacha de Agua e sal\n"))
        print("-=" *20)
        if opcao == 1:
            pao = int(input("Digite a quantidade de fatias de pao: "))
            qtPao = pao * 12
        elif opcao == 2:
            sucoUva = 36
        elif opcao == 3:
            sucoLaranja = 31
        elif opcao == 4:
             bolacha = int(input("Digite quantas bolachas de agua e sal você vai comer: "))
             qtBolacha = bolacha * 5
             
        op = int(input("\nDeseja continuar adicionando? \n[1] Sim\n[2] Nao\n"))
        if op == 2:
            break
    destro = float(input("Digite quanto deu o destro: "))
    
    if destro >= 101:
        contaDestro = (destro - 100.0) / 150.0
        
    else: 
        contaDestro = 0
    
    soma += qtPao + sucoUva + sucoLaranja + qtBolacha
    contaCarbo = Decimal(soma) / Decimal('18.0')
    resultadoFinal = Decimal(contaDestro) + contaCarbo

#   Fazer o arrendomento correto para a quantidade de insulina    
    Correto = (resultadoFinal % 1).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

    if Correto == Decimal('0.5'):
        print(f"\n {resultadoFinal.quantize(Decimal('0.1'))} de insulina")
    elif Correto == Decimal('0.6'):
        print(f"\n {(resultadoFinal - Decimal('0.1')).quantize(Decimal('0.1'))} de insulina")
    elif Correto == Decimal('0.7'):
        print(f"\n {(resultadoFinal - Decimal('0.2')).quantize(Decimal('0.1'))} de insulina")
    elif Correto == Decimal('0.4'):
        print(f"\n {(resultadoFinal + Decimal('0.1')).quantize(Decimal('0.1'))} de insulina")
    elif Correto == Decimal('0.3'):
        print(f"\n {(resultadoFinal + Decimal('0.2')).quantize(Decimal('0.1'))} de insulina")
    else:
        arredondado = resultadoFinal.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        print(f"\n {arredondado:.1f} de insulina")

        
def calcularAlmoco():
    soma = 0
    arroz = 0
    qtArroz = 0
    feijao = 0
    qtFeijao = 0
    fileEmpanado = 0
    qtfeijaoTropeiro = 0
    batataFrita = 0
    qtPure = 0
    qtMacarrao = 0
    lasanha = 0
    panqueca = 0
    qtFarofa = 0
    qtPirao = 0
    batata = 0
    sucoUva = 0
    sucoLaranja = 0
    chocolate = 0
    while True:
        print("-=" *20)
        opcao = int(input("[1] Arroz\n[2] Feijão\n[3] Filé empanado\n[4] Feijão Tropeiro\n[5] Batata frita\n[6] Purê de batata\n[7] Macarrão\n[8] Lasanha\n[9] Panqueca\n[10] Farofa\n[11] Pirão\n[12] Carne de Panela com Batata\n[13] Suco de uva\n[14] Suco de laranja\n[15] Chocolate\n"))
        print("-=" *20)
        if opcao == 1:
            arroz = int(input("Digite a quantidade de colheres de arroz: "))
            qtArroz = arroz * 13
        elif opcao == 2:
            feijao = int(input("Digite a quantidade de colheres de feijão"))
            qtFeijao = feijao * 3
            
        elif opcao == 3:
            fileEmpanado = 11
        elif opcao == 4:
            feijaoTropeiro = int(input("Digite a quantidade de colheres de feijão tropeiro: "))
            qtfeijaoTropeiro = feijaoTropeiro * 7
        elif opcao == 5:
            batataFrita = 23
        elif opcao == 6:
            pure = int(input("Digite a quantidade de colheres de purê: "))
            qtPure = pure * 8
        elif opcao == 7:
            macarrao = int(input("Digite a quantidade de colheres de macarrão: "))
            qtMacarrao = 22 * macarrao
        elif opcao == 8:
            lasanha = 27
        elif opcao == 9:
            panqueca = 18
        elif opcao == 10:
            farofa = int(input("Digite a quantidade de colheres de farofa: "))
            qtFarofa = farofa * 12
        elif opcao == 11:
            pirao =  int(input("Digite a quantidade de colheres de pirao: "))     
            qtPirao = pirao * 9
        elif opcao == 12:
            batata = 6
        elif opcao == 13:
            sucoUva = 36
        elif opcao == 14:
            sucoLaranja = 31
        elif opcao == 15:
            chocolate = 7
        op = int(input("Deseja continuar adicionando? \n[1] Sim\n[2] Nao\n"))
        if op == 2:
            break
    destro = float(input("Digite quanto deu o destro: "))
    
    if destro >= 101:
        contaDestro = (destro - 100.0) / 150.0
        
    else: 
        contaDestro = 0
    
    soma += qtArroz + qtFeijao + fileEmpanado + qtfeijaoTropeiro +  batataFrita +  qtPure + qtMacarrao + lasanha + panqueca +  qtFarofa +  qtPirao + batata + sucoUva + sucoLaranja + chocolate
    contaCarbo = Decimal(soma) / Decimal('17.0')
    resultadoFinal = Decimal(contaDestro) + contaCarbo


    Correto = (resultadoFinal % 1).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

    if Correto == Decimal('0.5'):
        print(f"\n {resultadoFinal.quantize(Decimal('0.1'))} de insulina")
    elif Correto == Decimal('0.6'):
        print(f"\n {(resultadoFinal - Decimal('0.1')).quantize(Decimal('0.1'))} de insulina")
    elif Correto == Decimal('0.7'):
        print(f"\n {(resultadoFinal - Decimal('0.2')).quantize(Decimal('0.1'))} de insulina")
    elif Correto == Decimal('0.4'):
        print(f"\n {(resultadoFinal + Decimal('0.1')).quantize(Decimal('0.1'))} de insulina")
    elif Correto == Decimal('0.3'):
        print(f"\n {(resultadoFinal + Decimal('0.2')).quantize(Decimal('0.1'))} de insulina")
    else:
        arredondado = resultadoFinal.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        print(f"\n {arredondado:.1f} de insulina")
        
def calculoLanche():
    
    soma = 0
    qtpao = 0
    sucouva = 0
    bolacha = 0
    qtbolacha = 0
    chocolate = 0        
    coxinhaGrande = 0
    coxinhaMini = 0
    qtcoxinha = 0
    milho = 0
    pipoca = 0
    maca = 0
    boloChocolate = 0
    boloLaranja = 0 
    while True:
        print("-=" *20)
        opcao = int(input("[1] Pão\n[2] Bolacha de água e sal\n[3] Coxinha Grande\n[4] Coxinha Pequena\n[5] Miho\n[6] Pipoca\n[7] Maçã\n[8] Chocolate\n[9] Suco de uva\n[10] Bolo de chocolate\n[11] Bolo de laranja\n"))
        print("-=" *20)
        if opcao == 1:
            pao = int(input("Digite a quantidade de fatias de pao: "))
            qtpao = pao * 12
        elif opcao == 2:
            bolacha = int(input("Digite quantas bolachas de agua e sal você vai comer: "))
            qtbolacha = bolacha * 5
        elif opcao == 3:
            coxinhaGrande = 40
        elif opcao == 4:
            coxinhaMini = int(input("Digite quantas coxinhas vai comer: "))
            qtcoxinha = coxinhaMini * 4
        elif opcao == 5:
            milho = 32
        elif opcao == 6:
            pipoca = 14
        elif opcao == 7:
            maca = 14
        elif opcao == 8:
            chocolate = 7
        elif opcao == 9:
            sucouva = 36
        elif opcao == 10:
            boloChocolate = 20
        elif opcao == 11:
            boloLaranja = 20
        op = int(input("\nDeseja continuar adicionando? \n[1] Sim\n[2] Nao\n"))
        if op == 2:
            break
    destro = float(input("Digite quanto deu o destro: "))
    
    if destro >= 101:
        contaDestro = (destro - 100.0) / 150.0
        
    else: 
        contaDestro = 0
    
    soma += qtpao + qtbolacha + coxinhaGrande + qtcoxinha + milho + pipoca + maca + chocolate + sucouva + boloChocolate + boloLaranja;
    contaCarbo = Decimal(soma) / Decimal('17.0')
    resultadoFinal = Decimal(contaDestro) + contaCarbo


    Correto = (resultadoFinal % 1).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

    if Correto == Decimal('0.5'):
        print(f"\n {resultadoFinal.quantize(Decimal('0.1'))} de insulina")
    elif Correto == Decimal('0.6'):
        print(f"\n {(resultadoFinal - Decimal('0.1')).quantize(Decimal('0.1'))} de insulina")
    elif Correto == Decimal('0.7'):
        print(f"\n {(resultadoFinal - Decimal('0.2')).quantize(Decimal('0.1'))} de insulina")
    elif Correto == Decimal('0.4'):
        print(f"\n {(resultadoFinal + Decimal('0.1')).quantize(Decimal('0.1'))} de insulina")
    elif Correto == Decimal('0.3'):
        print(f"\n {(resultadoFinal + Decimal('0.2')).quantize(Decimal('0.1'))} de insulina")
    else:
        arredondado = resultadoFinal.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        print(f"\n {arredondado:.1f} de insulina")

def calculoJanta():
    soma = 0
    arroz = 0
    qtArroz = 0
    feijao = 0
    qtFeijao = 0
    fileEmpanado = 0
    qtfeijaoTropeiro = 0
    qtPure = 0
    qtMacarrao = 0
    lasanha = 0
    panqueca = 0
    qtFarofa = 0
    qtPirao = 0
    batata = 0
    sucoUva = 0
    sucoLaranja = 0
    pizzaCalabresa = 0
    qtpizzaCalabresa = 0
    pizzaMucarela = 0
    qtpizzaMucarela = 0
    esfihaCarne = 0
    qtesfihaCarne = 0
    esfihaQueijo = 0
    qtesfihaQueijo = 0
    chocolate = 0
    while True:
        print("-=" *20)
        opcao = int(input("[1] Arroz\n[2] Feijão\n[3] Filé empanado\n[4] Feijão Tropeiro\n[5] Purê de batata\n[6] Macarrão\n[7] Lasanha\n[8] Panqueca\n[9] Farofa\n[10] Pirão\n[11] Carne de Panela com Batata\n[12] Suco de uva\n[13] Suco de laranja\n[14] Pizza de Calabresa\n[15] Pizza de Muçarela\n[16] Esfiha de Carne\n[17] Esfiha de Queijo\n[18] Chocolate\n"))
        print("-=" *20)
        if opcao == 1:
            arroz = int(input("Digite a quantidade de colheres de arroz: "))
            qtArroz = arroz  * 13
        elif opcao == 2:
            feijao = int(input("Digite a quantidade de colheres de feijão: "))
            qtFeijao = feijao * 3
        elif opcao == 3:
            fileEmpanado = 11
        elif opcao == 4:
            feijaoTropeiro = int(input("Digite a quantidade de colheres de feijão tropeiro: "))
            qtfeijaoTropeiro = feijaoTropeiro * 7
        elif opcao == 5:
            pure = int(input("Digite a quantidade de colheres de purê: "))
            qtPure = pure * 8
        elif opcao == 6:
            macarrao = int(input("Digite a quantidade de colheres de macarrão: "))
            qtMacarrao = 22 * macarrao
        elif opcao == 7:
            lasanha = 27
        elif opcao == 8:
            panqueca = 18
        elif opcao == 9:
            farofa = int(input("Digite a quantidade de colheres de farofa: "))
            qtFarofa = farofa * 12
        elif opcao == 10:
            pirao =  int(input("Digite a quantidade de colheres de pirao: "))     
            qtPirao = pirao * 9
        elif opcao == 11:
            batata = 6
        elif opcao == 12:
            sucoUva = 36
        elif opcao == 13:
            sucoLaranja = 31
        elif opcao == 14:
            pizzaCalabresa = int(input("Digite quantas fatias de Pizza de Calabresa você vai comer: "))
            qtpizzaCalabresa = pizzaCalabresa * 21
        elif opcao == 15:
            pizzaMucarela = int(input("Digite quantas fatias de Pizza de Muçarela você vai comer: "))
            qtpizzaMucarela = pizzaMucarela * 22
        elif opcao == 16:
            esfihaCarne = int(input("Digite quantas esfihas de carne vai comer: "))
            qtesfihaCarne = esfihaCarne * 18
        elif opcao == 17:
            esfihaQueijo = int(input("Digite quantas esfihas de queijo vai comer: "))
            qtesfihaQueijo = esfihaQueijo * 19
        elif opcao == 18:
            chocolate = 7
        op = int(input("Deseja continuar adicionando? \n[1] Sim\n[2] Nao\n"))
        if op == 2:
            break
    destro = float(input("Digite quanto deu o destro: "))
    
    if destro >= 101:
        contaDestro = (destro - 100.0) / 150.0
        
    else: 
        contaDestro = 0
        
    soma +=  qtArroz + qtFeijao + fileEmpanado + qtfeijaoTropeiro + qtPure + qtMacarrao + lasanha + panqueca + qtFarofa + qtPirao + batata + sucoUva +  sucoLaranja + qtpizzaCalabresa +  qtpizzaMucarela + qtesfihaCarne + qtesfihaQueijo + chocolate
    contaCarbo = Decimal(soma) / Decimal('20.0')
    resultadoFinal = Decimal(contaDestro) + contaCarbo


    Correto = (resultadoFinal % 1).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

    if Correto == Decimal('0.5'):
        print(f"\n {resultadoFinal.quantize(Decimal('0.1'))} de insulina")
    elif Correto == Decimal('0.6'):
        print(f"\n {(resultadoFinal - Decimal('0.1')).quantize(Decimal('0.1'))} de insulina")
    elif Correto == Decimal('0.7'):
        print(f"\n {(resultadoFinal - Decimal('0.2')).quantize(Decimal('0.1'))} de insulina")
    elif Correto == Decimal('0.4'):
        print(f"\n {(resultadoFinal + Decimal('0.1')).quantize(Decimal('0.1'))} de insulina")
    elif Correto == Decimal('0.3'):
        print(f"\n {(resultadoFinal + Decimal('0.2')).quantize(Decimal('0.1'))} de insulina")
    else:
        arredondado = resultadoFinal.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        print(f"\n {arredondado:.1f} de insulina")
            
            
menu()
if op == 1:
    calcularCafe()
elif op == 2:
    calcularAlmoco()
elif op == 3:
    calculoLanche()
elif op == 4:
    calculoJanta()

    

             
            
        
    

