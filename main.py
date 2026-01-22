import os
import time
import shutil
from colorama import init, Fore, Style
import turtle
from PIL import Image

init()

MIN_WIDTH = 170

# Banner
print(f"{Fore.GREEN}───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
time.sleep(.1)
print(f"{Fore.GREEN}─██████████████─██████──██████─████████████████───██████████████─██████─────────██████████████─────────────██████████████─██████████████─████████████───██████████████─")
time.sleep(.1)
print(f"{Fore.GREEN}─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─────────────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░████─██░░░░░░░░░░██─")
time.sleep(.1)
print(f"{Fore.GREEN}─██████░░██████─██░░██──██░░██─██░░████████░░██───██████░░██████─██░░██─────────██░░██████████─────────────██░░██████████─██░░██████░░██─██░░████░░░░██─██░░██████████─")
time.sleep(.1)
print(f"{Fore.GREEN}─────██░░██─────██░░██──██░░██─██░░██────██░░██───────██░░██─────██░░██─────────██░░██─────────────────────██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██─────────")
time.sleep(.1)
print(f"{Fore.GREEN}─────██░░██─────██░░██──██░░██─██░░████████░░██───────██░░██─────██░░██─────────██░░██████████─────────────██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██████████─")
time.sleep(.1)
print(f"{Fore.GREEN}─────██░░██─────██░░██──██░░██─██░░░░░░░░░░░░██───────██░░██─────██░░██─────────██░░░░░░░░░░██─────────────██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░░░░░░░░░██─")
time.sleep(.1)
print(f"{Fore.GREEN}─────██░░██─────██░░██──██░░██─██░░██████░░████───────██░░██─────██░░██─────────██░░██████████─────────────██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██████████─")
time.sleep(.1)
print(f"{Fore.GREEN}─────██░░██─────██░░██──██░░██─██░░██──██░░██─────────██░░██─────██░░██─────────██░░██─────────────────────██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██─────────")
time.sleep(.1)
print(f"{Fore.GREEN}─────██░░██─────██░░██████░░██─██░░██──██░░██████─────██░░██─────██░░██████████─██░░██████████─────────────██░░██████████─██░░██████░░██─██░░████░░░░██─██░░██████████─")
time.sleep(.1)
print(f"{Fore.GREEN}─────██░░██─────██░░░░░░░░░░██─██░░██──██░░░░░░██─────██░░██─────██░░░░░░░░░░██─██░░░░░░░░░░██─────────────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░████─██░░░░░░░░░░██─")
time.sleep(.1)
print(f"{Fore.GREEN}─────██████─────██████████████─██████──██████████─────██████─────██████████████─██████████████─────────────██████████████─██████████████─████████████───██████████████─")
time.sleep(.1)
print(f"{Fore.GREEN}───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
time.sleep(.1)
print(f"{Fore.CYAN}Made by: System64{Style.RESET_ALL}")

# Estado global do Turtle
t = None
screen = None
lines = []
script_files = []

def create_window():
    """Cria (ou recria) a janela e a tartaruga, evitando turtle.Terminator."""
    global t, screen

    # Se já existir uma janela antiga, tenta fechá-la com segurança
    try:
        if screen is not None:
            turtle.bye()
    except turtle.Terminator:
        # Se já estiver encerrada, apenas ignora
        pass

    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.title("TurtleCode")
    t = turtle.Turtle()

def process_command(line: str) -> int:
    """Processa uma linha de comando vinda do shell ou de script."""
    global t, screen
    parameters = line.split()
    if not parameters:
        return 0

    cmd_input = parameters[0].lower()

    if cmd_input == "new" and len(parameters) > 1 and parameters[1] == "window":
        create_window()
        return 1

    if cmd_input == "forward" and len(parameters) == 2:
        if t is None:
            print(f"{Fore.RED}[ERR] Abra uma janela primeiro com 'new window'{Style.RESET_ALL}")
            return 0
        try:
            dist = int(parameters[1])
        except ValueError:
            print(f"{Fore.RED}[ERR] Valor inválido para 'forward'{Style.RESET_ALL}")
            return 0
        try:
            t.forward(dist)
        except turtle.Terminator:
            t = None
            screen = None
            print(f"{Fore.RED}[ERR] A janela Turtle foi fechada. Crie outra com 'new window'.{Style.RESET_ALL}")
            return 0
        return 1

    if cmd_input == "left" and len(parameters) == 2:
        if t is None:
            print(f"{Fore.RED}[ERR] Abra uma janela primeiro com 'new window'{Style.RESET_ALL}")
            return 0
        try:
            angle = int(parameters[1])
        except ValueError:
            print(f"{Fore.RED}[ERR] Valor inválido para 'left'{Style.RESET_ALL}")
            return 0
        try:
            t.left(angle)  # gira no sentido anti-horário [web:19][web:21]
        except turtle.Terminator:
            t = None
            screen = None
            print(f"{Fore.RED}[ERR] A janela Turtle foi fechada. Crie outra com 'new window'.{Style.RESET_ALL}")
            return 0
        return 1

    if cmd_input == "right" and len(parameters) == 2:
        if t is None:
            print(f"{Fore.RED}[ERR] Abra uma janela primeiro com 'new window'{Style.RESET_ALL}")
            return 0
        try:
            angle = int(parameters[1])
        except ValueError:
            print(f"{Fore.RED}[ERR] Valor inválido para 'right'{Style.RESET_ALL}")
            return 0
        try:
            t.right(angle)  # gira no sentido horário [web:19][web:21]
        except turtle.Terminator:
            t = None
            screen = None
            print(f"{Fore.RED}[ERR] A janela Turtle foi fechada. Crie outra com 'new window'.{Style.RESET_ALL}")
            return 0
        return 1
    if cmd_input == "backward" and len(parameters) == 2:
        if t is None:
            print(f"{Fore.RED}[ERR] Abra uma janela primeiro com 'new window'{Style.RESET_ALL}")
            return 0
        try:
            dist = int(parameters[1])
        except ValueError:
            print(f"{Fore.RED}[ERR] Valor inválido para 'backward'{Style.RESET_ALL}")
            return 0
        try:
            t.backward(dist)
        except turtle.Terminator:
            t = None
            screen = None
            print(f"{Fore.RED}[ERR] A janela Turtle foi fechada. Crie outra com 'new window'.{Style.RESET_ALL}")
            return 0
        return 1
    if cmd_input == "pen_up":
        if t is None:
            print(f"{Fore.RED}[ERR] Abra uma janela primeiro com 'new window'{Style.RESET_ALL}")
            return 0
        try:
            t.penup()
            return 1
        except turtle.Terminator:
            t = None
            screen = None
            print(f"{Fore.RED}[ERR] A janela Turtle foi fechada. Crie outra com 'new window'.{Style.RESET_ALL}")
    if cmd_input == "pen_down":
        if t is None:
            print(f"{Fore.RED}[ERR] Abra uma janela primeiro com 'new window'{Style.RESET_ALL}")
            return 0
        try:
            t.pendown()
            return 1
        except turtle.Terminator:
            t = None
            screen = None
            print(f"{Fore.RED}[ERR] A janela Turtle foi fechada. Crie outra com 'new window'.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[WARN] Comando desconhecido: {cmd_input}{Style.RESET_ALL}")
    return 0

# Verificação de largura do terminal
size = shutil.get_terminal_size()
while int(size.columns) < MIN_WIDTH:
    size = shutil.get_terminal_size()
    if int(size.columns) < MIN_WIDTH:
        print(f"{Fore.RED}[ERR] Seu terminal é muito pequeno para o texto, aumente e pressione Enter para tentar de novo{Style.RESET_ALL}")
        input()

print(f'{Style.RESET_ALL}\n\nTodos os comandos podem ser vistos usando o comando "help"')
print("\nTurtleCode Shell")

# Garante pasta scripts
os.makedirs("scripts", exist_ok=True)

while True:
    try:
        raw_input_cmd = input("> ")
    except (EOFError, KeyboardInterrupt):
        print("\nSaindo...")
        break

    parameters = raw_input_cmd.split()
    if not parameters:
        continue

    cmd_input = parameters[0].lower()

    if cmd_input == "help":
        print("Comandos disponíveis:")
        print("  list update      - Atualiza e lista scripts .trtl na pasta scripts/")
        print("  load <arquivo>   - Carrega um script .trtl")
        print("  run              - Executa o script carregado")
        print("  new window       - Abre uma nova janela Turtle")
        print("  forward <valor>  - Move a tartaruga para frente")
        print("  left <angulo>    - Gira a tartaruga para a esquerda")
        print("  right <angulo>   - Gira a tartaruga para a direita")
        print("  exit             - Sai do programa")
        print("  pen_up           - Desativa a caneta")
        print("  pen_down         - Ativa a caneta")
    elif cmd_input == "exit":
        print("Saindo...")
        break

    elif cmd_input == "list" and len(parameters) > 1 and parameters[1] == "update":
        print("Procurando scripts válidos...")
        script_files = []
        for f in os.listdir("scripts"):
            path = os.path.join("scripts", f)
            if os.path.isfile(path) and f.endswith(".trtl"):
                script_files.append(f)
        print(f"Encontrados {len(script_files)} scripts válidos\n")
        for s in script_files:
            print(f"{Fore.GREEN}{s}{Style.RESET_ALL}")

    elif cmd_input == "load" and len(parameters) > 1:
        to_load = parameters[1]
        print("Procurando arquivo...")
        if to_load in script_files:
            print("Encontrado, carregando...")
            path = os.path.join("scripts", to_load)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                lines = content.splitlines()
                print(f"{Fore.GREEN}Concluído!{Style.RESET_ALL}")
            except OSError as e:
                print(f"{Fore.RED}[ERR] Erro ao abrir o arquivo: {e}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[ERR] Nenhum arquivo correspondente encontrado em scripts/{Style.RESET_ALL}")

    elif cmd_input == "run":
        if not lines:
            print(f"{Fore.RED}[ERR] Nenhum script carregado. Use 'load <arquivo>' primeiro.{Style.RESET_ALL}")
        else:
            try:
                for line in lines:
                    process_command(line)
            except turtle.Terminator:
                t = None
                screen = None
                print(f"{Fore.RED}[ERR] A janela Turtle foi fechada durante a execução. Use 'new window' e 'run' novamente.{Style.RESET_ALL}")

    else:
        # Tenta interpretar o que o usuário digitou como comando de turtle
        process_command(raw_input_cmd)
