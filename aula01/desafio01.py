# Ctrl; torna tudo ccomentário

nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
profissao = input("Informe sua profissão: ")
ano_atual = int(input("Informe o ano atual: "))
idade_pessoa = ano_atual - ano_nascimento

print(f"Olá {nome}. Conforme consulta você possui {idade_pessoa} esse ano e trabalha como {profissao}.")

