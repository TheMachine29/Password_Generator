import random
import string
import re

def generador_contraseña():
    while True:
        try:
            longitud = int(input("\nIngrese la longitud de la contraseña (mínimo 10 caracteres): "))
            if longitud < 10:
                print("⚠️ La longitud mínima es de 10 caracteres. Inténtelo de nuevo.")
            else:
                break
        except ValueError:
            print("⚠️ Entrada inválida. Ingrese un número válido.")

    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    while True:
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        if (any(c.islower() for c in contraseña)
            and any(c.isupper() for c in contraseña)
            and sum(c.isdigit() for c in contraseña) >= 2
            and any(c in string.punctuation for c in contraseña)):
            break

    return contraseña

def validar_contraseña(contraseña):
    if len(contraseña) < 10:
        print("❌ La contraseña debe tener al menos 10 caracteres.")
        return False

    if not re.search(r'[^\w\s]', contraseña):  # Verifica caracteres especiales
        print("❌ La contraseña debe contener al menos un carácter especial.")
        return False

    if not re.search(r'[A-Z]', contraseña):
        print("❌ La contraseña debe contener al menos una letra mayúscula.")
        return False

    if not re.search(r'[a-z]', contraseña):
        print("❌ La contraseña debe contener al menos una letra minúscula.")
        return False

    if sum(c.isdigit() for c in contraseña) < 2:  # Verifica que haya al menos 2 números
        print("❌ La contraseña debe contener al menos dos números.")
        return False

    return True

def main():
    print("\n🔐 Generador y Validador de Contraseña 🔐\n")
    
    while True:
        print("\n📌 Opciones:")
        print("1️⃣ Generar una contraseña")
        print("2️⃣ Validar una contraseña")
        print("3️⃣ Salir")
        
        try:
            opcion = int(input("\nIngrese la opción deseada: "))
        except ValueError:
            print("⚠️ Opción inválida. Ingrese un número entre 1 y 3.")
            continue

        if opcion == 1:
            contraseña = generador_contraseña()
            print(f"\n✅ Contraseña generada: {contraseña}")
        
        elif opcion == 2:
            contraseña = input("\nIngrese la contraseña a validar: ")
            if validar_contraseña(contraseña):
                print("✅ La contraseña es válida.")
            else:
                print("❌ La contraseña es inválida.")
        
        elif opcion == 3:
            print("\n👋 ¡Hasta pronto!")
            break
        
        else:
            print("⚠️ Opción incorrecta. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
