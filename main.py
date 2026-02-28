import secrets
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*?"
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("=== Gerador de Senhas ===")
    tamanho = int(input("Digite o tamanho da senha: "))
    senha = gerar_senha(tamanho)
    print(f"Sua senha gerada é: {senha}")

if __name__ == "__main__":
    main()