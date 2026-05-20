# =========================================
# EVENTHUB MANAGER
# Terzo Commit
# Menu iniziale + visualizzazione eventi
# =========================================

eventi = {

    # ==========================
    # SPORTIVI
    # ==========================

    "Sportivi": {

        1: {
            "nome": "Torneo del Teatro",
            "posti": 2
        },

        2: {
            "nome": "Kart Racing Lombardia",
            "posti": 0
        },

        3: {
            "nome": "Street Basket Milano",
            "posti": 5
        }
    },

    # ==========================
    # CONCERTI
    # ==========================

    "Concerti": {

        1: {
            "nome": "Night Sound Festival",
            "posti": 10
        },

        2: {
            "nome": "Jazz sotto le Stelle",
            "posti": 0
        }
    },

    # ==========================
    # FIERE
    # ==========================

    "Fiere": {

        1: {
            "nome": "Expo Tech Future",
            "posti": 20
        },

        2: {
            "nome": "Comics & Games",
            "posti": 8
        }
    },

    # ==========================
    # FESTE
    # ==========================

    "Feste": {

        1: {
            "nome": "Sagra della Castagna",
            "posti": 30
        },

        2: {
            "nome": "Mercatini di Natale",
            "posti": 50
        }
    },

    # ==========================
    # RADUNI
    # ==========================

    "Raduni": {

        1: {
            "nome": "Motoraduno Nazionale",
            "posti": 25
        },

        2: {
            "nome": "Cosplay Gathering",
            "posti": 7
        }
    }

}

# =========================================
# FUNZIONE VISUALIZZA EVENTI
# =========================================

def visualizza_eventi():

    print("\n================================")
    print(" EVENTI DISPONIBILI")
    print("================================")

    for categoria, lista_eventi in eventi.items():

        print(f"\n--- {categoria} ---")

        for numero, dati in lista_eventi.items():

            print(
                f"{numero}. "
                f"{dati['nome']} "
                f"- Posti disponibili: {dati['posti']}"
            )

# =========================================
# FUNZIONE ISCRIZIONE
# =========================================

def iscrizione():

    print("\n================================")
    print(" ISCRIZIONE")
    print("================================")

    # Lista categorie
    categorie = list(eventi.keys())

    print("\nCategorie disponibili:\n")

    for i, categoria in enumerate(categorie, start=1):
        print(f"{i}. {categoria}")

    # Scelta categoria
    scelta_categoria = int(input("\nScegli una categoria: "))

    categoria_scelta = categorie[scelta_categoria - 1]

    # Ciclo scelta evento
    while True:

        print(f"\nEventi categoria {categoria_scelta}:\n")

        for numero, dati in eventi[categoria_scelta].items():

            print(
                f"{numero}. "
                f"{dati['nome']} "
                f"- Posti disponibili: {dati['posti']}"
            )

        # Scelta evento
        scelta_evento = int(input("\nScegli un evento: "))

        evento = eventi[categoria_scelta][scelta_evento]

        # Controllo posti
        if evento["posti"] > 0:

            nome_utente = input("\nInserisci il tuo nome: ")

            # Riduzione posti
            evento["posti"] -= 1

            print("\n================================")
            print(" ISCRIZIONE COMPLETATA")
            print("================================")

            print(f"Utente: {nome_utente}")
            print(f"Evento: {evento['nome']}")
            print(f"Posti rimasti: {evento['posti']}")

            # ritorno automatico al menu
            return

        else:

            print("\n================================")
            print(" EVENTO AL COMPLETO")
            print("================================")

            print("Scegli un altro evento.")

# =========================================
# MENU PRINCIPALE
# =========================================

while True:

    print("\n================================")
    print(" EVENTHUB MANAGER")
    print("================================")

    print("\n1. Iscriviti ad un evento")
    print("2. Visualizza eventi")
    print("3. Esci")

    scelta = input("\nSeleziona un'opzione: ")

    # =====================================
    # ISCRIZIONE
    # =====================================

    if scelta == "1":
        iscrizione()

    # =====================================
    # VISUALIZZA EVENTI
    # =====================================

    elif scelta == "2":
        visualizza_eventi()

    # =====================================
    # USCITA
    # =====================================

    elif scelta == "3":

        print("\nChiusura programma...")
        break

    # =====================================
    # ERRORE
    # =====================================

    else:
        print("\nOpzione non valida.")
