

def depositar (saldo, valor, extrato):
 if valor > 0 :
    print(valor)
    saldo += valor
    extrato+= f"Você fez umm Depósito de:\tR$ {valor:.2f}\n"
    print("operação realizada com sucesso")
 else:
    print("Operação falhou! O valor informado é inválido.")

 return saldo, extrato

def sacar (*,valor,limite,limite_saques,saldo, numero_saques,extrato):
     
      if numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        return saldo, extrato
      else:
            
            if valor > saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif valor > limite:
                 print("Operação falhou! O valor do saque excede o limite.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("\n=== Saque realizado com sucesso! ===")
                print(f"\nSaldo: R$ {saldo:.2f}")

                return saldo, extrato          
        
            else:
             print("Operação falhou! O valor informado é inválido.")


def extrato (saldo,extrato): 
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        return saldo, extrato
