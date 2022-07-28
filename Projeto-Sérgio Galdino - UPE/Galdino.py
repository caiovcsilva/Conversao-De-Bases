#PyScript conversor de bases

#OBS: tanto num_original quanto dec podem ser passados a função como string, ou inteiros, porém base deve ser sempre um inteiro.

#OBS2:: Ambas as funções retornam sempre strings. (nunca valores)

#OBS3: As bases base_original e base_final são convertidas para inteiro (independente se seu input for uma String, para ser trabalho, será considerado como um valor inteiro!)

#   any2dec: (Esse, mais simplificado, converte o valor em decimal para base final diretamente. Nesse caso você perde pontos, pois, só pode converter da base 10 para qualquer outra base)
#
#   dec2any: (nesse você insere o número em decimal, a base original e a base para que você deseja a conversão. Nesse caso você pode converter da base 2 para qualquer outra base, por exemplo, o que não é possível no método anterior.)


def any2dec(num_original,base_original):
    num_original = str(num_original)
    base_original = int(base_original)
    dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    dec = 0
    dec_temp = list(num_original)
    dec_temp.reverse()
    for x,i in enumerate(dec_temp):
        dec += dic.index(i) * base_original**(x)
    return str(dec)


def dec2any(dec,base_final):
    base_final = int(base_final)
    dec = int(dec)
    dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numero_final_temp = []
    numero_final = ''
    while True:
        temp_numero_final = dec%base_final
        numero_final_temp.append(temp_numero_final)
        if int(dec/base_final) == 0:
            break
        dec = int(dec/base_final)
    numero_final_temp.reverse()
    for i in numero_final_temp:
        numero_final += dic[i]     
    return numero_final

def any2any(num_original,base_original,base_final):
    num_dec = any2dec(num_original,base_original)
    num_final = dec2any(num_dec,base_final)
    print(num_final)


while True:
    num_original = int(input("digite o valor do número: "))
    base_original = int(input("Digite a base original: "))
    base_final = int(input("Digite a base destino: "))
    any2any(num_original,base_original,base_final)
    break
input()