
import operacoes
menu  = """"
 
Informe a operação desejada!

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 1000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



while True:
 menu_aux = input(menu) 


 if menu_aux == "d":
  valor =float(input("Infomre o valor que deseja depositar na conta: "))
  operacoes.depositar(valor,saldo,extrato)

 elif menu_aux == "s":
  valor =float(input("Infomre o valor que deseja sacar da conta "))
  operacoes.sacar(saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,)
 elif menu_aux == "e":
  operacoes.extrato(saldo,extrato)
  
 elif menu_aux == "q":
  break
 





 

