import os

def convertir_a_decimal(a, base_a):
    
    caracteres = [
                  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                  'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z',
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', '+', '/'
                  ]
    
    a_decimal = 0
    
    for i, caracter in enumerate(a):
        
        char_pos_in_chars = caracteres.index(caracter)
        a_size = len(a)
        a_size -= 1
        char_pos_in_a = len(a) - i -1
        pos_value = int(base_a) ** char_pos_in_a
        char_value = char_pos_in_chars * pos_value
        
        a_decimal += char_value
    
    return(a_decimal)



def convertir_a_base_final(a_decimal, base_final):
    
    resultado = ""
    dividiendo = a_decimal
    base_final = int(base_final)
    
    for _ in range(len(str(a_decimal))+1):
        quociente = dividiendo // base_final
        resto = dividiendo % base_final
        dividiendo = quociente
        resultado = str(resto) + resultado
    
    return resultado
        

        
while True:
    print("""
╔══════════════════════════════╗
║      🔢  C O N V E R T I X   ║
║      ⚡ Base Converter ⚡      ║
╚══════════════════════════════╝
""")
    print("\nIntroduce el número y las bases  __✏️")
    a, base_a, base_final = input("\nA, base A, base final ➜  ").split(",")

    a_decimal = convertir_a_decimal(a, base_a)
        
    resultado = convertir_a_base_final(a_decimal, base_final)
        
    print(f"\n🧮   Resultado: {resultado}")
    input("\n🔙  Volver")
    os.system("cls")