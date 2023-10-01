from os import system
from art import *
from termcolor import colored

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def resto(a, b):
    return a % b

def div_int(a, b):
    return a // b

def exponenciar(a, b):
    return a ** b

def porcentagem(a, b):
    return (a * 0.01) * b

def raiz(a):
    return a ** 0.5

def tabuada(a):
  for e in range(1, 11):
      print(colored(f'{e} x {a} = {e * a}', 'yellow'))

def separador():
  separacao_colorida = colored('=', 'cyan')
  for e in range(115, 116):
      print(f'{e * separacao_colorida}', end=' ')

def separador_():
  separacao_colorida = colored('=', 'cyan')
  for e in range(115, 116):
      print(f'{e * separacao_colorida}', end=' ' '\n')

system('cls')

texto_ascii = text2art("Calculadora_Python", "big")
texto_ascii2 = text2art("Calculo_finalizado!", "big")
titulo_colorido = colored(texto_ascii, "cyan")
fim_colorido = colored(texto_ascii2, "red")  
digite_colorido = colored('Digite um número --> ', 'red')  
operador_colorido = colored('Digite um operador --> ', 'red')

def menu():
   print(colored("""Utilize (+) para realizar adições.\nUtilize (-) para realizar subtrações.\nUtilize (*) para realizar multiplicações.\nUtilize (/) para realizar divisões simples.\nUtilize (//) para realizar divisões inteirias.\nUtilize (**) para realizar exponenciações.\nUtilize (%) para realizar o cálculo de porcentagens.\nUtilize (!) para descobrir a raiz.\nUtilize (#) para vizualizar a tabuada de um número até 10.\nUtilize (.) para desligar a calculadora.""", 'grey'))
   
def fim():
      print('')
      separador_()
      print('')
      print(fim_colorido)
      separador_()
      print(colored("""\n
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡿⠟⠛⠛⠛⠛⢻⣿⣟⣛⣉⣉⣉⣉⠉⠉⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠟⠋⠀⠁⠐⠂⢀⠖⠁⠀⠀⠀⠀⠀⠀⠈⠉⠲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣤⣤⣄⣀⣠⠾⢯⣤⣦⣤⣤⣤⣀⡀⠀⠀⠀⢰⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡟⠉⢾⣿⠟⢉⡉⠉⢹⣟⢿⣷⣦⢢⠘⣿⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡟⠀⠀⠸⠁⢰⣿⣷⣶⣤⣿⣷⠙⢿⡃⠀⠛⠀⠀⢻⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡿⠀⠀⠀⠀⠀⠚⠻⠿⣿⣟⣻⡿⠀⠈⠁⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⡿⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠟⣿⠇⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣭⣕⡀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⣀⠉⠻⢿⣦⡀⠹⠙⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⢀⣾⣷⣄⠀⣦⡻⣷⡀⠀⠸⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣶⣦⡀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣧⢿⣧⠄⠀⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣦⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣏⡿⠃⣼⡿⠤⣰⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠀⠛⠃⣠⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿
⣧⡀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\nEspero que tenha gostado!""", 'magenta'))
   
print(titulo_colorido)

separador()
print(colored("\nOperadores e Funções:", 'grey'))
menu()
separador_()
print(' ')
resultado = None

while True:
    if resultado is not None:
        separador_()
        n1 = resultado
    else: 
        try:
            separador_()
            n1 = float(input(digite_colorido))
        except ValueError:
            continue
    operação = input(operador_colorido)
    if operação != '.' and operação != '#' and operação != '!':
      n2 = float(input(digite_colorido))

    if operação == '+':
      resultado = somar(n1, n2)

    elif operação == '-':
      resultado = subtrair(n1, n2)

    elif operação == '*':
      resultado = multiplicar(n1, n2)

    elif operação == '/':
      resultado = dividir(n1, n2)
  
    elif operação == '//':
      resultado = div_int(n1, n2)

    elif operação == '**':
      resultado = exponenciar(n1, n2)

    elif operação == '%':
      resultado = porcentagem(n1, n2)

    elif operação == '!':
      resultado = raiz(n1)

    elif operação == '#':
      print(colored('----TABUADA----', 'yellow'))
      resultado = tabuada(n1)
      fim()
      break

    elif operação == '.':
       fim()
       break
      
    if operação != '#' and operação != '/':
      print(colored(f'Resultado = [{resultado}]', 'green'))
      separador_()    
      print()

    if operação == '/':
      print(colored(f'Resultado = [{resultado}] Resto = [{resto(n1, n2)}]', 'green'))
      separador_()    
      print()
