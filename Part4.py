# =========================================
# EVENTHUB MANAGER
# Quarto Commit COMPLETO
# Tutte le categorie + creazione eventi
# =========================================

eventi = {

    # =====================================
    # SPORTIVI
    # =====================================

    "Sportivi": {

        1: {
            "nome": "Torneo del Teatro",
            "posti": 6
        },

        2: {
            "nome": "Kart Racing Emilia Romagna",
            "posti": 7
        },

        3: {
            "nome": "Street Basket Rimini",
            "posti": 0
        },

        4: {
            "nome": "Volley Summer Cup, Cesenatico",
            "posti": 3
        }
    },

    # =====================================
    # CONCERTI
    # =====================================

    "Concerti": {

        1: {
            "nome": "Night Sound Festival",
            "posti": 10
        },

        2: {
            "nome": "Rock in Piazza",
            "posti": 6
        },

        3: {
            "nome": "Jazz sotto le Stelle",
            "posti": 0
        },

        4: {
            "nome": "Winter DJ Experience",
            "posti": 12
        }
    },

    # =====================================
    # FIERE
    # =====================================

    "Fiere": {

        1: {
            "nome": "Expo Tech Future",
            "posti": 20
        },

        2: {
            "nome": "Comics & Games",
            "posti": 8
        },

        3: {
            "nome": "Auto Moto Show",
            "posti": 15
        },

        4: {
            "nome": "Green Energy Expo",
            "posti": 5
        }
    },

    # =====================================
    # FESTE E SAGRE
    # =====================================

    "Feste": {

        1: {
            "nome": "Sagra della Castagna",
            "posti": 30
        },

        2: {
            "nome": "Mercatini di Natale",
            "posti": 50
        },

        3: {
            "nome": "Notte Rosa",
            "posti": 0
        },

        4: {
            "nome": "Festival della piadina",
            "posti": 18
        }
    },

    # =====================================
    # RADUNI
    # =====================================

    "Raduni": {

        1: {
            "nome": "Motoraduno Nazionale",
            "posti": 25
        },

        2: {
            "nome": "Raduno vespa d'epoca",
            "posti": 7
        },

        3: {
            "nome": "Raduno Auto Storiche",
            "posti": 15
        },

        4: {
            "nome": "Aprilia Scarabeo club",
            "posti": 10
        }
    },

    # =====================================
    # WORKSHOP
    # =====================================

    "Workshop": {

        1: {
            "nome": "Python Dev Conference",
            "posti": 14
        },

        2: {
            "nome": "AI Innovation Summit",
            "posti": 9
        },

        3: {
            "nome": "Workshop Cybersecurity",
            "posti": 0
        },

        4: {
            "nome": "Startup Networking Day",
            "posti": 4
        }
    }

}

# =========================================
# FUNZIONE VISUALIZZA EVENTI
# =========================================

def visualizza_eventi():

    print("\n================================")
    print("        EVENTI DISPONIBILI")
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

    while True:

        print("\n================================")
        print("         ISCRIZIONE")
        print("================================")

        categorie = list(eventi.keys())

        print("\nCategorie disponibili:\n")

        for i, categoria in enumerate(categorie, start=1):
            print(f"{i}. {categoria}")

        print("0. Torna alla Home")

        scelta_categoria = input("\nScegli una categoria: ")

        # ritorno home
        if scelta_categoria == "0":
            return

        categoria_scelta = categorie[int(scelta_categoria) - 1]

        while True:

            print(f"\nEventi categoria {categoria_scelta}:\n")

            for numero, dati in eventi[categoria_scelta].items():

                print(
                    f"{numero}. "
                    f"{dati['nome']} "
                    f"- Posti disponibili: {dati['posti']}"
                )

            print("0. Torna alle categorie")

            scelta_evento = input("\nScegli un evento: ")

            # ritorno categorie
            if scelta_evento == "0":
                break

            evento = eventi[categoria_scelta][int(scelta_evento)]

            # controllo posti
            if evento["posti"] > 0:

                nome_utente = input("\nInserisci il tuo nome: ")

                evento["posti"] -= 1

                print("\n================================")
                print("    ISCRIZIONE COMPLETATA")
                print("================================")

                print(f"Utente: {nome_utente}")
                print(f"Evento: {evento['nome']}")
                print(f"Posti rimasti: {evento['posti']}")

                # ritorno automatico home
                return

            else:

                print("\n================================")
                print("      EVENTO AL COMPLETO")
                print("================================")

                print("Scegli un altro evento.")

# =========================================
# FUNZIONE CREAZIONE EVENTO
# =========================================

def crea_evento():

    print("\n================================")
    print("       CREA NUOVO EVENTO")
    print("================================")

    categorie = list(eventi.keys())

    print("\nCategorie disponibili:\n")

    for i, categoria in enumerate(categorie, start=1):
        print(f"{i}. {categoria}")

    print("0. Crea nuova categoria")
    print("99. Torna alla Home")

    scelta = input("\nScegli una categoria: ")

    # =====================================
    # RITORNO HOME
    # =====================================

    if scelta == "99":
        return

    # =====================================
    # CREAZIONE NUOVA CATEGORIA
    # =====================================

    if scelta == "0":

        nuova_categoria = input(
            "\nCategoria non presente.\n"
            "Inserisci il nome della nuova categoria: "
        )

        eventi[nuova_categoria] = {}

        print(f"\nCategoria '{nuova_categoria}' creata!")

        categoria_scelta = nuova_categoria

    else:

        categoria_scelta = categorie[int(scelta) - 1]

    # =====================================
    # CREAZIONE EVENTO
    # =====================================

    nome_evento = input("\nInserisci il nome dell'evento: ")

    posti = int(input("Inserisci i posti disponibili: "))

    nuovo_id = len(eventi[categoria_scelta]) + 1

    eventi[categoria_scelta][nuovo_id] = {
        "nome": nome_evento,
        "posti": posti
    }

    print("\n================================")
    print("      EVENTO CREATO")
    print("================================")

    print(f"Categoria: {categoria_scelta}")
    print(f"Evento: {nome_evento}")
    print(f"Posti disponibili: {posti}")

# =========================================
# MENU PRINCIPALE
# =========================================

while True:

    print("\n================================")
    print("        EVENTHUB MANAGER")
    print("================================")

    print("\n1. Iscriviti ad un evento")
    print("2. Visualizza eventi")
    print("3. Crea un evento")
    print("4. Esci")

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
    # CREA EVENTO
    # =====================================

    elif scelta == "3":
        crea_evento()

    # =====================================
    # USCITA
    # =====================================

    elif scelta == "4":

        print("\nChiusura programma...")
        break

    # =====================================
    # ERRORE
    # =====================================

    else:
        print("\nOpzione non valida.")

