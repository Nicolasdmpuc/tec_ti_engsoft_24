#calculo do perimetro de um quadrado

#L=float (input("Digite o valor do lado:"))
#P=4*L

#print(f"\n\n\tO Perímetro do Quadrado de lado {L:.2f} é {P:.2f}")

def FODASE():
 L=float (input("digite um numero:"))
 A= L- 1

 S= L + 1

 print(f"\n\n\tO sucessor é {A:.2f} e o antecessor é {S:.2f}")

def triangulo():

 H=float (input("digite sua altura:"))
 B=float (input("digite sua base:"))

 R= (H * B)/2
 print(f"\n\n\t A base do triangulo é:{R:.2f}")

def salario():

 S=float (input("digite o salario reportado pelo funcionario:"))
 P=float (input("digite o percentual dado pelo patrão:"))

 ns= S + S * (P/100)

 print(f"o reajuste salarial é de: {ns:.1f}")

def cubo():

 H=float (input("digite a altura do seu cubo:"))
 C=float (input("digite seu comprimento:"))
 L=float (input("digite sua largura:"))

 V= H * C * L

 print(f"o volume do cubo é de {V:.1f} metros")

def gasolina():

 D=float (input("a distancia percorrida é de:"))
 G=float (input("o valor total gasto foi de:"))

 C= D/G
 print(f"o consumo foi de {C:.2f}")

def tapete():

 C=float (input("digite seu comprimento:"))
 L=float (input("digite sua largura:"))

 T= C*L
 mq= 5
 V= T*mq

 print(f"o valor do preço do metro quadrado é de {mq}BRL sendo o valor total de {V:.2f}")

def imc():
 P=float (input("o peso da pessoa é de:"))
 H=float (input("a altura da pessoa é de:"))

 c= H*H
 imc= P/c

 print(f"o imc da pessoa é de:{imc:.2f}")

def premio():

 P=float (input("valor do premio:"))

 n1= P * 0.46
 n2= P * 0.32
 n3= P * 0.22

 print(f"valor divido vai ser {n1:.2f} e {n2:.2f} e {n3:.2f}")


def troco():

 vc=float (input("valor da compra foi de:"))
 vp=float (input("valor pago foi de:"))

 t= vp - vc
 tt= t

 c20= t//20
 t= t - c20*20

 c10= t//10
 t= t - c10*10

 c5= t//5
 t= t - c5*5

 c2=t//2
 t= t - c2*2

 m1=t//1
 t= t - m1*1

 print(f"o troco vai ser de {tt:.2f} notas de 20:{c20:.2f} notas de 10:{c10:.2f} notas de 5:{c5:.2f} notas de 2:{c2:.2f} moedas de 1 real:{m1:.2f}")

def ab():
 
 A=13
 B=5

 AUX=A
 A=B
 B=AUX

 print(f"{A} {B}")

 # ==(igual)
 # != (diferente)
 # > (maior)
 # >= (maior ou igual)
 # < (menor)
 # <= (menor ou igual)

def impar():
  
 num=int(input("digite um numero:"))

 if(num % 2 == 0):
  
  print(f"o valor é {num}")
  numa=num+1
  print(f"o valor de numero é {numa}")

 else:
  print(f"o numero é igual a {num}")

def quadrilatero():
 num=int(input("digite um numero:"))
 lado=int(input("digite um lado:"))

 if(num * num != 2 * lado):

  num="é retangulo"

  print(f"é um {num}")
 else:
 
  print("é um quadrado")

def maior():
 num1=int(input("digite um numero:"))
 num2=int(input("digite outro numero:"))

 if(num1 > num2 ):
  print(f"numero é {num1}")
 else:
  print(f"numero é {num2}")  

def sinais():
 num=int(input("digite um numero:"))

 if(num > 0):
  print("o numero é positivo")

 elif(num < 0):
  print("o numero é negativo")
 else:
  
  print("o numero é nulo")

def multiplo():
 num=int(input("digite um numero:"))

 if( num % 5 == 0):
  print("o numero é divisivel por 5")
 else:
  print("o numero não é divisivel por 5") 

def calculo():
 valora=int(input("digite um valor:"))
 valorb=int(input("digite um valor:"))

 if(valora == valorb):
  c=valora+valorb
  print(f"o novo resultado atribuido da soma é de {c}")

 else:
  c= valora*valorb
  print(F"o valor atribuido pela multiplicação dos numeros é de {c}")


