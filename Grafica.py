# =========================================
# EVENTHUB MANAGER - PYGAME FULL EDITION
# VERSIONE GRAFICA COMPLETA
# =========================================

import pygame
import sys

pygame.init()

# =========================================
# FINESTRA
# =========================================

WIDTH = 1400
HEIGHT = 850

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("EVENTHUB MANAGER")

# =========================================
# COLORI
# =========================================

WHITE = (255, 255, 255)
BLACK = (25, 25, 25)
BLUE = (52, 152, 219)
LIGHT_BLUE = (93, 173, 226)
GREEN = (46, 204, 113)
RED = (231, 76, 60)
GRAY = (230, 230, 230)
DARK = (40, 40, 40)
YELLOW = (241, 196, 15)

# =========================================
# FONT
# =========================================

title_font = pygame.font.SysFont("Arial", 42, bold=True)
menu_font = pygame.font.SysFont("Arial", 28)
small_font = pygame.font.SysFont("Arial", 22)

# =========================================
# PASSWORD ADMIN
# =========================================

password_admin = "Sergio11"

# =========================================
# DATABASE
# =========================================

utenti = []
biglietti = []

# =========================================
# EVENTI
# LAVORI
# =========================================

lavori = {

    "Spiaggia": {
        1: {"lavoro": "Bagnino", "stipendio": 90, "posti": 2},
        2: {"lavoro": "Deejay in Spiaggia", "stipendio": 120, "posti": 1},
        3: {"lavoro": "Barista", "stipendio": 80, "posti": 3}
    },

    "Eventi": {
        1: {"lavoro": "Bodyguard Concerti", "stipendio": 110, "posti": 4},
        2: {"lavoro": "Barman Festival", "stipendio": 95, "posti": 2}
    },

    "Estate": {
        1: {"lavoro": "Educatore Centro Estivo", "stipendio": 75, "posti": 5},
        2: {"lavoro": "Animatore Piscina", "stipendio": 70, "posti": 2}
    },

    "Cerimonie": {
        1: {"lavoro": "Fotografo Matrimoni", "stipendio": 150, "posti": 2},
        2: {"lavoro": "Fotografo Cresime", "stipendio": 100, "posti": 3}
    }

}

# =========================================
# INPUT BOX
# =========================================

class InputBox:

    def __init__(self, x, y, w, h):

        self.rect = pygame.Rect(x, y, w, h)
        self.color = BLUE
        self.text = ""
        self.active = False

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            self.active = self.rect.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN and self.active:

            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]

            elif event.key == pygame.K_RETURN:
                pass

            else:
                self.text += event.unicode

    def draw(self, screen):

        pygame.draw.rect(screen, WHITE, self.rect)
        pygame.draw.rect(screen, self.color, self.rect, 2)

        txt_surface = menu_font.render(self.text, True, BLACK)
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))


# =========================================
# FUNZIONI GRAFICHE
# =========================================

def text(texto, font, color, x, y):

    render = font.render(texto, True, color)
    screen.blit(render, (x, y))


def bottone(nome, x, y, w, h, colore):

    rect = pygame.Rect(x, y, w, h)

    mouse = pygame.mouse.get_pos()

    if rect.collidepoint(mouse):
        pygame.draw.rect(screen, LIGHT_BLUE, rect, border_radius=12)
    else:
        pygame.draw.rect(screen, colore, rect, border_radius=12)

    txt = menu_font.render(nome, True, WHITE)

    screen.blit(txt, (x + 15, y + 12))

    return rect


# =========================================
# BIGLIETTO
# =========================================

def stampa_biglietto(nome_utente, evento):

    biglietti.append({
        "utente": nome_utente,
        "evento": evento.copy()
    })


# =========================================
# VISUALIZZA EVENTI
# =========================================

def visualizza_eventi():

    running = True

    while running:

        screen.fill(WHITE)

        text("EVENTI DISPONIBILI", title_font, BLUE, 420, 20)

        y = 100

        for categoria, lista_eventi in eventi.items():

            text(categoria, menu_font, RED, 50, y)

            y += 40

            for numero, dati in lista_eventi.items():

                pygame.draw.rect(screen, GRAY, (50, y, 1250, 80),
                                 border_radius=10)

                text(f"{numero}. {dati['nome']}",
                     menu_font,
                     BLACK,
                     70,
                     y + 5)

                text(f"Data: {dati['data']}",
                     small_font,
                     BLACK,
                     70,
                     y + 35)

                text(f"Luogo: {dati['luogo']}",
                     small_font,
                     BLACK,
                     350,
                     y + 35)

                text(f"Orario: {dati['orario']}",
                     small_font,
                     BLACK,
                     700,
                     y + 35)

                text(f"Posti: {dati['posti']}",
                     small_font,
                     BLACK,
                     1050,
                     y + 35)

                y += 100

        back = bottone("TORNA", 20, 770, 180, 50, RED)

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if back.collidepoint(event.pos):
                    running = False


# =========================================
# ISCRIZIONE EVENTI
# =========================================

def iscrizione():

    categorie = list(eventi.keys())

    running = True

    while running:

        screen.fill(WHITE)

        text("ISCRIZIONE EVENTI", title_font, BLUE, 420, 20)

        pulsanti = []

        y = 120

        for categoria in categorie:

            btn = bottone(categoria, 450, y, 450, 60, GREEN)

            pulsanti.append((btn, categoria))

            y += 90

        back = bottone("TORNA", 20, 770, 180, 50, RED)

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if back.collidepoint(event.pos):
                    running = False

                for btn, categoria in pulsanti:

                    if btn.collidepoint(event.pos):

                        scegli_evento(categoria)


# =========================================
# SCELTA EVENTO
# =========================================

def scegli_evento(categoria):

    input_nome = InputBox(500, 700, 300, 45)

    running = True

    while running:

        screen.fill((245, 245, 245))

        text(categoria, title_font, BLUE, 520, 20)

        y = 120

        pulsanti = []

        for numero, dati in eventi[categoria].items():

            pygame.draw.rect(screen, GRAY, (80, y, 1200, 100),
                             border_radius=12)

            text(dati["nome"], menu_font, BLACK, 100, y + 5)

            text(f"Data: {dati['data']}",
                 small_font,
                 BLACK,
                 100,
                 y + 40)

            text(f"Luogo: {dati['luogo']}",
                 small_font,
                 BLACK,
                 350,
                 y + 40)

            text(f"Orario: {dati['orario']}",
                 small_font,
                 BLACK,
                 750,
                 y + 40)

            text(f"Posti: {dati['posti']}",
                 small_font,
                 BLACK,
                 1050,
                 y + 40)

            btn = bottone("ISCRIVITI", 1080, y + 10, 170, 45, GREEN)

            pulsanti.append((btn, dati))

            y += 130

        text("Inserisci nome:", small_font, BLACK, 300, 710)

        input_nome.draw(screen)

        back = bottone("INDIETRO", 20, 770, 180, 50, RED)

        pygame.display.update()

        for event in pygame.event.get():

            input_nome.handle_event(event)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if back.collidepoint(event.pos):
                    running = False

                for btn, evento in pulsanti:

                    if btn.collidepoint(event.pos):

                        if input_nome.text != "":

                            if evento["posti"] > 0:

                                utenti.append(input_nome.text)

                                evento["posti"] -= 1

                                stampa_biglietto(
                                    input_nome.text,
                                    evento
                                )


# =========================================
# BIGLIETTI
# =========================================

def visualizza_biglietti():

    running = True

    while running:

        screen.fill(WHITE)

        text("BIGLIETTI EMESSI", title_font, BLUE, 430, 20)

        y = 100

        if len(biglietti) == 0:

            text("Nessun biglietto presente",
                 menu_font,
                 RED,
                 450,
                 300)

        else:

            for biglietto in biglietti:

                evento = biglietto["evento"]

                pygame.draw.rect(screen, GRAY,
                                 (70, y, 1200, 100),
                                 border_radius=12)

                text(f"Utente: {biglietto['utente']}",
                     menu_font,
                     BLACK,
                     100,
                     y + 10)

                text(f"Evento: {evento['nome']}",
                     small_font,
                     BLACK,
                     100,
                     y + 45)

                text(f"{evento['data']} - {evento['orario']}",
                     small_font,
                     BLACK,
                     600,
                     y + 45)

                y += 130

        back = bottone("TORNA", 20, 770, 180, 50, RED)

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if back.collidepoint(event.pos):
                    running = False


# =========================================
# CREA EVENTO
# =========================================

def crea_evento():

    categoria = InputBox(450, 150, 400, 45)
    nome = InputBox(450, 230, 400, 45)
    luogo = InputBox(450, 310, 400, 45)
    data = InputBox(450, 390, 400, 45)
    orario = InputBox(450, 470, 400, 45)
    posti = InputBox(450, 550, 400, 45)

    running = True

    while running:

        screen.fill(WHITE)

        text("CREA EVENTO", title_font, BLUE, 500, 30)

        text("Categoria", small_font, BLACK, 300, 160)
        text("Nome Evento", small_font, BLACK, 300, 240)
        text("Luogo", small_font, BLACK, 300, 320)
        text("Data", small_font, BLACK, 300, 400)
        text("Orario", small_font, BLACK, 300, 480)
        text("Posti", small_font, BLACK, 300, 560)

        categoria.draw(screen)
        nome.draw(screen)
        luogo.draw(screen)
        data.draw(screen)
        orario.draw(screen)
        posti.draw(screen)

        crea = bottone("CREA EVENTO",
                        500,
                        650,
                        250,
                        60,
                        GREEN)

        back = bottone("TORNA", 20, 770, 180, 50, RED)

        pygame.display.update()

        for event in pygame.event.get():

            categoria.handle_event(event)
            nome.handle_event(event)
            luogo.handle_event(event)
            data.handle_event(event)
            orario.handle_event(event)
            posti.handle_event(event)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if back.collidepoint(event.pos):
                    running = False

                if crea.collidepoint(event.pos):

                    cat = categoria.text

                    if cat not in eventi:
                        eventi[cat] = {}

                    nuovo_id = len(eventi[cat]) + 1

                    eventi[cat][nuovo_id] = {
                        "nome": nome.text,
                        "posti": int(posti.text),
                        "luogo": luogo.text,
                        "orario": orario.text,
                        "data": data.text
                    }


# =========================================
# LAVORA EVENTO
# =========================================

def lavora_evento():

    running = True

    while running:

        screen.fill(WHITE)

        text("LAVORA AD UN EVENTO",
             title_font,
             BLUE,
             380,
             30)

        y = 130

        for categoria, lavori_cat in lavori.items():

            text(categoria, menu_font, RED, 70, y)

            y += 40

            for num, dati in lavori_cat.items():

                pygame.draw.rect(screen,
                                 GRAY,
                                 (70, y, 1200, 80),
                                 border_radius=10)

                text(dati["lavoro"],
                     menu_font,
                     BLACK,
                     90,
                     y + 10)

                text(f"Stipendio: {dati['stipendio']}€",
                     small_font,
                     BLACK,
                     500,
                     y + 20)

                text(f"Posti: {dati['posti']}",
                     small_font,
                     BLACK,
                     900,
                     y + 20)

                y += 100

        back = bottone("TORNA", 20, 770, 180, 50, RED)

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if back.collidepoint(event.pos):
                    running = False


# =========================================
# ADMIN PANEL
# =========================================

def admin_panel():

    password_box = InputBox(500, 300, 300, 50)

    running = True

    while running:

        screen.fill(WHITE)

        text("ADMIN PANEL", title_font, BLUE, 500, 120)

        text("Password Admin", menu_font, BLACK, 480, 250)

        password_box.draw(screen)

        login = bottone("ENTRA", 550, 400, 180, 50, GREEN)

        back = bottone("TORNA", 20, 770, 180, 50, RED)

        pygame.display.update()

        for event in pygame.event.get():

            password_box.handle_event(event)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if back.collidepoint(event.pos):
                    return

                if login.collidepoint(event.pos):

                    if password_box.text == password_admin:

                        admin_gestione()


# =========================================
# GESTIONE ADMIN
# =========================================

def admin_gestione():

    running = True

    while running:

        screen.fill(WHITE)

        text("GESTIONE EVENTI", title_font, BLUE, 450, 20)

        y = 120

        pulsanti_remove = []

        for categoria, lista in eventi.items():

            text(categoria, menu_font, RED, 70, y)

            y += 40

            for num, ev in lista.items():

                pygame.draw.rect(screen,
                                 GRAY,
                                 (70, y, 1200, 80),
                                 border_radius=10)

                text(ev["nome"], menu_font, BLACK, 90, y + 10)

                text(ev["data"], small_font, BLACK, 90, y + 45)

                remove_btn = bottone("ELIMINA",
                                     1050,
                                     y + 15,
                                     160,
                                     40,
                                     RED)

                pulsanti_remove.append(
                    (remove_btn, categoria, num)
                )

                y += 100

        back = bottone("TORNA", 20, 770, 180, 50, RED)

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if back.collidepoint(event.pos):
                    running = False

                for btn, categoria, num in pulsanti_remove:

                    if btn.collidepoint(event.pos):

                        eventi[categoria].pop(num)
                        break


# =========================================
# MENU PRINCIPALE
# =========================================

running = True

while running:

    screen.fill((240, 245, 255))

    text("EVENTHUB MANAGER",
         title_font,
         BLUE,
         420,
         40)

    btn1 = bottone("1. Iscriviti Evento",
                   430,
                   150,
                   500,
                   60,
                   BLUE)

    btn2 = bottone("2. Visualizza Eventi",
                   430,
                   240,
                   500,
                   60,
                   BLUE)

    btn3 = bottone("3. Crea Evento",
                   430,
                   330,
                   500,
                   60,
                   GREEN)

    btn4 = bottone("4. Lavora Evento",
                   430,
                   420,
                   500,
                   60,
                   YELLOW)

    btn5 = bottone("5. Biglietti",
                   430,
                   510,
                   500,
                   60,
                   BLUE)

    btn6 = bottone("6. Admin Panel",
                   430,
                   600,
                   500,
                   60,
                   RED)

    btn7 = bottone("7. Esci",
                   430,
                   690,
                   500,
                   60,
                   DARK)

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if btn1.collidepoint(event.pos):
                iscrizione()

            elif btn2.collidepoint(event.pos):
                visualizza_eventi()

            elif btn3.collidepoint(event.pos):
                crea_evento()

            elif btn4.collidepoint(event.pos):
                lavora_evento()

            elif btn5.collidepoint(event.pos):
                visualizza_biglietti()

            elif btn6.collidepoint(event.pos):
                admin_panel()

            elif btn7.collidepoint(event.pos):
                running = False

pygame.quit()
sys.exit()