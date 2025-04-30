import os
from time import sleep

users = []


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    clear()
    dashes = 40
    dash(dashes)
    print("Sistema de Cadastro de Usuários".center(dashes))
    dash(dashes)
    print("1 - Cadastrar um novo usuário")
    print("2 - Ver dados cadastrados")
    print("3 - Sair")
    dash(dashes)
    print("Escolha uma opção: ", end="")


def get_option():
    menu()
    while True:
        try:
            option = int(input())
            if option in [1, 2, 3]:
                return option
            else:
                print("Opção inválida. Tente novamente.")
                sleep(1)
                clear()
                menu()
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            sleep(1)
            clear()
            menu()


def get_user_data():
    clear()
    dash(30)
    print("Cadastro de Usuário".center(30))
    dash(30)
    print()

    user_data = {}

    while True:
        try:
            dash(40)
            user_data["name"] = input("Nome: ").strip()
            dash(40)
            if user_data["name"] == "":
                clear()
                dash(40)
                raise ValueError("O nome não pode ser vazio.")
            if not user_data["name"].replace(" ", "").isalpha():
                clear()
                dash(40)
                raise ValueError("O nome deve conter apenas letras.")
            break
        except ValueError as e:
            print(e)
            sleep(1)
            clear()

    while True:
        try:
            dash(40)
            age = input("Idade: ").strip()
            dash(40)
            if age == "":
                clear()
                dash(40)
                raise ValueError("A idade não pode ser vazia.")
            if not age.isdigit():
                clear()
                dash(40)
                raise ValueError("A idade deve ser um número inteiro.")
            age = int(age)
            if age <= 0:
                clear()
                dash(40)
                raise ValueError("A idade não pode menor que 1.")
            if age > 120:
                clear()
                dash(40)
                raise ValueError("A idade não pode ser maior que 120.")
            user_data["age"] = age
            break
        except ValueError as e:
            print(e)
            sleep(1)
            clear()

    while True:
        try:
            dash(40)
            user_data["email"] = input("Email: ").strip()
            dash(40)
            if "@" not in user_data["email"] or "." not in user_data["email"]:
                clear()
                dash(40)
                raise ValueError("Email inválido.")
            break
        except ValueError as e:
            print(e)
            sleep(1)
            clear()

    return user_data


def save_user_data():
    users.append(get_user_data())
    print()
    dash(35)
    print("Usuário cadastrado com sucesso!".center(35))
    dash(35)
    sleep(1.5)
    clear()


def show_users():
    clear()
    dash(80)
    print("Usuários Cadastrados".center(80))
    dash(80)
    print()

    if users:
        for i, user in enumerate(users):
            print("-" * 80)
            print(
                f"Usuário {i + 1}: Nome: {user['name']} - Idade: {user['age']} - Email: {user['email']}".center(
                    80
                )
            )
            if i == len(users) - 1:
                print("-" * 80)
    else:
        dash(30)
        print("Nenhum usuário cadastrado.".center(30))
        dash(30)
    print()
    input("Pressione Enter para continuar...")


def start():
    while True:
        option = get_option()
        if option == 1:
            save_user_data()
        elif option == 2:
            show_users()
        elif option == 3:
            clear()
            dash(30)
            print("Saindo...".center(30))
            dash(30)
            sleep(1)
            break


def dash(num=30):
    print("=" * num)


def main():
    clear()
    dash(50)
    print("Bem-vindo ao sistema de cadastro de usuários!".center(50))
    dash(50)
    sleep(2)
    start()


main()
