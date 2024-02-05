import webbrowser
from time import sleep
import pyautogui
import sys
import os


def clear_terminal():
    """Limpa o terminal."""
    if sys.platform.startswith("win"):
        # Para Windows
        _ = os.system("cls")
    else:
        # Para Linux e macOS
        _ = os.system("clear")


time_jogo_iniciar = 60
quantidade_clicks_tempo = 100


def checar_time(timer):
    minutos = 0
    segundos = 0

    if timer >= 60:
        minutos += timer // 60
        segundos = timer % 60
        timer = 0
        if segundos == 0:
            return f"{minutos} minuto(s)"
        else:
            return f"{minutos} minuto(s) e {segundos} segundo(s)"
    else:
        segundos = timer % 60
        return f"{segundos} segundo(s)"


def carregamento(titulo, timer, inicializador=False):
    frames = ["/", "-", "\\", "|", "/", "-", "\\", "|"]
    if inicializador is True:
        print(f"Iniciando Programa em {checar_time(timer)}")
        print(
            f"Enquanto o programa carrega, você tem um tempo para ajustar o jogo de sua maneira"
        )
        print()
        for time in range(1, timer + 1):
            for caracter in frames:
                print(f"\r{titulo}{caracter}..{checar_time(time)}", end="", flush=True)
                sleep(0.1)
        print()
    else:
        for time in range(1, timer + 1):
            for caracter in frames:
                print(f"\r{titulo}{caracter}..{checar_time(time)}", end="", flush=True)
                sleep(0.1)
        print()


def clicar_play(x, y):
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()


def art_ASCII_capivara():
    frames = [
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠻⡧⠭⠿⠿⠿⠿⣿⣿⣿",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀⠤⣤⡤⠀⠀⢀⣠⣽⣿",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⢿⣿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠈⠀⢹⣿",
        "⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿",
        "⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿",
        "⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿",
        "⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣣⣿⣿⣿⣿⣿⣿⣿",
        "⣿⣿⣿⡀⠀⠀⠀⠀⣀⣀⠀⠀⢀⡀⠀⠀⣷⠀⠀⠀⢰⠟⢋⣿⣿⣿⣿⣿⣿⣿",
        "⣿⣿⠟⠀⠀⠀⢀⡾⠋⠉⠻⣿⣿⣶⣶⣶⣿⡄⠀⢀⡏⠀⢸⣿⣿⣿⣿⣿⣿⣿",
        "⣿⣿⡀⠀⣠⣴⣿⣷⣤⠀⠀⣿⣿⣿⣿⣿⣿⣇⠀⢸⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿",
        "⣿⣿⡇⠀⣿⣿⣿⣿⣿⣧⣀⣹⣿⣿⣿⣿⣿⣿⠀⢸⣿⣀⣸⣿⣿⣿⣿⣿⣿⣿",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿",
    ]

    for frame in frames:
        print(f"{frame}")
        sleep(0.1)


def procurar_capivara_coords(x, y, time_start):
    print()
    print(f"Procurando a capivara em {checar_time(time_start)} não mova o mouse")
    for tempo in range(time_start, 0, -1):
        print(tempo)
        sleep(1)
    pyautogui.moveTo(x, y, duration=0.5)
    print(
        "Encontrei a capivara, apartir daqui\nVoce pode movimentar o mouse se quiser,\nMas lembre-se que estara clicando automaticamente"
    )
    print("Para parar o programa, vá ate o terminal e use CTRL C")
    sleep(10)


def atacar_capivara(x, y, quantidade_clicks_tempo, time_start):
    procurar_capivara_coords(x, y, time_start)
    clicks_total = 0
    clear_terminal()
    art_ASCII_capivara()
    for click in range(quantidade_clicks_tempo * 10):
        pyautogui.click()
        clicks_total += 1
    print(f"Clicks no total: {clicks_total}")


# Vai descer a barra de rolagem
def descer_barra_rolagem(x, y):
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()


# Vai upar o nivel da capivara x vezes (isso vai depender de quanto de dinheiro vai possuir) escolha os vetores x, y para o nivel que deseja upar
def upar_capivara_farm(time):
    print("Agora é hora de você upar a capivara")
    print(f"Você tem {checar_time(time)}")
    for tempo in range(time, 0, -1):
        print(tempo)
        sleep(1)


def verificar_site_aberto_no_navegador(url):
    try:
        # Abre a URL no navegador padrão
        webbrowser.open(url, new=2)
        print(f"Abrindo o site {url} no navegador.")
    except Exception as e:
        print(f"Erro ao abrir o site {url} no navegador: {e}")


def inicio():
    # webbrowser.open_new("https://games.crazygames.com/en_US/capybara-clicker/index.html?v=1.267")
    verificar_site_aberto_no_navegador(
        "https://games.crazygames.com/en_US/capybara-clicker/index.html?v=1.267"
    )
    sleep(5)
    # Dar play coloque as coordenadas x, y de acordo com sua janela web (use mouseinfo para captar os eixos x, y)
    clicar_play(1400, 663)
    # Esperar o jogo carregar
    carregamento("Carregando", time_jogo_iniciar, inicializador=True)
    # Econtrar a posiçao capivara e clicar ate 500 clicks
    print("Tudo certo, jogo começando..")
    sleep(1)
    while True:
        try:
            # Clicar na capivara. Coloque as coordenadas x, y de acordo com sua janela web (use mouseinfo para captar os eixos x, y)
            # Defina quantos clicks vai dar ate parar para upar e quantos segundos de intervalo antes de começar a clicar
            atacar_capivara(1258, 525, quantidade_clicks_tempo, 5)
            upar_capivara_farm(20)
            clear_terminal()
        except KeyboardInterrupt:
            exit()
