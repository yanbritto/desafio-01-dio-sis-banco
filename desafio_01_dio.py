
import operacoes
menu  = """"
 
 ================ MENU ================
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nc] Nova conta
    [nu] Novo usuário
    [q]  Sair
    => """

LIMITE_SAQUES = 3
AGENCIA = "0001"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []#nome,data nascikento, cpf, endereco / apenas um usuraio por cpf
contas = []



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
  operacoes.extrato(saldo,extratoe=extrato)
 
 elif menu_aux == "nu":
      operacoes.criar_usuarios(usuarios)
      


 elif menu_aux == "nc":
      numero_conta = len(contas) + 1
      conta = operacoes.nova_conta(AGENCIA, numero_conta, usuarios)

      if conta:
        contas.append(conta)

 elif menu_aux == "q":
  break
 
else:
   print("Operação inválida, por favor selecione novamente a operação desejada.")
 





 
