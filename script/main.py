import os
import toml
import emoji
import socket

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_config():
    # Carregar o arquivo TOML
    with open('mhelp.toml', 'r') as file:
        config = toml.load(file)
    return config

def salvar_config(config):
    # Salvar as alterações de volta no arquivo TOML
    with open('mhelp.toml', 'w') as file:
        toml.dump(config, file)

clear_screen()

logo = '''\n
\033[1;96m ||\||\|  |\||\|  ||\|  ||\|      |\|   \033[1;91m||\||\||\|  ||\||\||\||\|
\033[1;96m ||\||\|  |\||\|  ||\|    ||\|  |\|     \033[1;91m||\|        ||\|      |\|
\033[1;96m ||\|   |\|  |\|  ||\|       ||\|       \033[1;91m||\||\||\|  ||\||\||\||\|
\033[1;96m ||\|   |\|  |\|  ||\|    ||\|   |\|    \033[1;91m||\|        ||\|   |\|
\033[1;96m ||\|        |\|  ||\|  ||\|       |\|  \033[1;91m||\|        ||\|      |\|
\033[1;96m ||\|        |\|  ||\| ||\|         |\| \033[1;91m||\||\||\|  ||\|        |\|

\033[1;96m Version 1.0.0 Codded By \033[1;91m@jabfx
\033[94mDigite mhelp para ver a lista de comandos (ou digite 'exit' para sair)
\n'''

print(logo)

imput_shell = emoji.emojize(":game_die:")

while True:
    pergunta = input("\033[94m %s $" % imput_shell)
    if pergunta == "exit":
        break
    elif pergunta == "mls":
        os.system('dir' if os.name == 'nt' else 'ls')
    elif pergunta == "mhelp":
        mhelp = carregar_config()
        print("\033[97m\nApp:\033[97m", mhelp['app']['name'])
        print("\033[97mComands:", mhelp['app']['comands'])
        print("Dependencias:\n\033[1;91m", mhelp['app']['dependecies'])
        print("\033[97mVersão:\033[97m", mhelp['app']['version'])
        print("\033[94m")
    elif pergunta == "mcat":
        os.system('nc')
    elif not pergunta:
        print("\nDigite algo\n")

os.system('cls' if os.name == 'nt' else 'clear')
print("\nByeBye!")