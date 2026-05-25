# =========================================
# EVENTHUB MANAGER
# COMMIT 5 COMPLETO
# Eventi + Cinema + Lavori + Inserimento lavori
# =========================================

# =========================================
# DATABASE EVENTI
# =========================================

eventi = {

    "Sportivi": {

        1: {
            "nome": "Torneo del Teatro",
            "posti": 6,
            "luogo": "COCIF STADIUM",
            "orario": "15:00"
        },

        2: {
            "nome": "Kart Racing Emilia Romagna",
            "posti": 7,
            "luogo": "Kartodromo Happy Valley",
            "orario": "10:30"
        },

        3: {
            "nome": "Street Basket Rimini",
            "posti": 5,
            "luogo": "Palazzetto dello sport Rimini",
            "orario": "18:00"
        },

        4: {
            "nome": "Beach Volley cup Cesenatico",
            "posti": 3,
            "luogo": "Bagno Roma, Cesenatico",
            "orario": "15:00"
        }
    },

    "Concerti": {

        1: {
            "nome": "Kanye West",
            "posti": 88,
            "luogo": "Reggio Emilia",
            "orario": "21:00"
        },

        2: {
            "nome": "Artie 5ive",
            "posti": 6,
            "luogo": "Bologna",
            "orario": "20:30"
        },

        3: {
            "nome": "Tonypitony",
            "posti": 69,
            "luogo": "Beky Bay, Bellaria Igea Marina",
            "orario": "22:00"
        }
    },

    "Feste e Sagre": {

        1: {
            "nome": "San Martino",
            "posti": 45,
            "luogo": "Santarcangelo",
            "orario": "09:00"
        },

        2: {
            "nome": "RiminiWellness",
            "posti": 30,
            "luogo": "Rimini",
            "orario": "11:00"
        },

        3: {
            "nome": "Sagra della Cozza",
            "posti": 15,
            "luogo": "Ravenna",
            "orario": "19:00"
        },

        4: {
            "nome": "Festa della Sburdela",
            "posti": 50,
            "luogo": "Riolo Terme",
            "orario": "10:00"
        },
    },

    "Raduni": {

        1: {
            "nome": "Motoraduno Nazionale",
            "posti": 25,
            "luogo": "Misano",
            "orario": "14:00"
        },

        2: {
            "nome": "Vespa Club Bellaria",
            "posti": 41,
            "luogo": "Bellaria",
            "orario": "10:30"
        },

        3: {
            "nome": "Raduno Auto Storiche",
            "posti": 55,
            "luogo": "Imola",
            "orario": "11:00"
        },

        4: {
            "nome": "Aprilia Scarabeo Club",
            "posti": 67,
            "luogo": "Gatteo",
            "orario": "10:30"
        }
    },

    "Cinema": {

        1: {
            "nome": "Dune Parte Due",
            "posti": 40,
            "luogo": "Cinema Moderno",
            "orario": "21:15"
        },

        2: {
            "nome": "Inside Out 2",
            "posti": 25,
            "luogo": "Cinema Centrale",
            "orario": "18:30"
        },

        3: {
            "nome": "Deadpool & Wolverine",
            "posti": 12,
            "luogo": "Multisala Europa",
            "orario": "22:00"
        }
    }

}

# =========================================
# DATABASE LAVORI
# =========================================

lavori = {

    "Spiaggia": {

        1: {
            "lavoro": "Bagnino",
            "stipendio": 90,
            "posti": 2
        },

        2: {
            "lavoro": "Deejay in Spiaggia",
            "stipendio": 120,
            "posti": 1
        },

        3: {
            "lavoro": "Barista",
            "stipendio": 80,
            "posti": 3
        }
    },

    "Eventi": {

        1: {
            "lavoro": "Bodyguard Concerti",
            "stipendio": 110,
            "posti": 4
        },

        2: {
            "lavoro": "Barman Festival",
            "stipendio": 95,
            "posti": 2
        }
    },

    "Estate": {

        1: {
            "lavoro": "Educatore Centro Estivo",
            "stipendio": 75,
            "posti": 5
        },

        2: {
            "lavoro": "Animatore Piscina",
            "stipendio": 70,
            "posti": 2
        }
    }

}

# =========================================
# VISUALIZZA EVENTI
# =========================================

def visualizza_eventi():

    print("\n================================")
    print("        EVENTI DISPONIBILI")
    print("================================")

    for categoria, lista_eventi in eventi.items():

        print(f"\n--- {categoria} ---")

        for numero, dati in lista_eventi.items():

            print(f"\n{numero}. {dati['nome']}")
            print(f"Luogo: {dati['luogo']}")
            print(f"Orario: {dati['orario']}")
            print(f"Posti disponibili: {dati['posti']}")

# =========================================
# ISCRIZIONE EVENTI
# =========================================

def iscrizione():

    categorie = list(eventi.keys())

    print("\nCategorie disponibili:\n")

    for i, categoria in enumerate(categorie, start=1):
        print(f"{i}. {categoria}")

    print("0. Torna alla Home")

    scelta_categoria = input("\nScegli una categoria: ")

    if scelta_categoria == "0":
        return

    categoria_scelta = categorie[int(scelta_categoria) - 1]

    while True:

        print(f"\n--- {categoria_scelta} ---")

        for numero, dati in eventi[categoria_scelta].items():

            print(f"\n{numero}. {dati['nome']}")
            print(f"Luogo: {dati['luogo']}")
            print(f"Orario: {dati['orario']}")
            print(f"Posti: {dati['posti']}")

        print("0. Torna alle categorie")

        scelta_evento = input("\nScegli un evento: ")

        if scelta_evento == "0":
            return

        evento = eventi[categoria_scelta][int(scelta_evento)]

        if evento["posti"] > 0:

            nome_utente = input("\nInserisci il tuo nome: ")

            evento["posti"] -= 1

            print("\n================================")
            print("    ISCRIZIONE COMPLETATA")
            print("================================")

            print(f"Utente: {nome_utente}")
            print(f"Evento: {evento['nome']}")

            return

        else:

            print("\nEvento al completo!")

# =========================================
# CREA EVENTO
# =========================================

def crea_evento():

    categorie = list(eventi.keys())

    print("\nCategorie disponibili:\n")

    for i, categoria in enumerate(categorie, start=1):
        print(f"{i}. {categoria}")

    print("0. Crea nuova categoria")
    print("99. Torna alla Home")

    scelta = input("\nScegli una categoria: ")

    if scelta == "99":
        return

    if scelta == "0":

        nuova_categoria = input(
            "\nInserisci nome nuova categoria: "
        )

        eventi[nuova_categoria] = {}

        categoria_scelta = nuova_categoria

    else:

        categoria_scelta = categorie[int(scelta) - 1]

    nome_evento = input("\nNome evento: ")
    luogo = input("Luogo evento: ")
    orario = input("Orario evento: ")
    posti = int(input("Posti disponibili: "))

    nuovo_id = len(eventi[categoria_scelta]) + 1

    eventi[categoria_scelta][nuovo_id] = {

        "nome": nome_evento,
        "posti": posti,
        "luogo": luogo,
        "orario": orario
    }

    print("\n================================")
    print("      EVENTO CREATO")
    print("================================")

# =========================================
# LAVORA AD UN EVENTO
# =========================================

def lavora_evento():

    while True:

        print("\n================================")
        print("      LAVORA AD UN EVENTO")
        print("================================")

        print("\n1. Trova un lavoro")
        print("2. Inserisci un lavoro")
        print("3. Torna alla Home")

        scelta_menu = input("\nSeleziona un'opzione: ")

        # =====================================
        # VISUALIZZA LAVORI
        # =====================================

        if scelta_menu == "1":

            categorie = list(lavori.keys())

            for i, categoria in enumerate(categorie, start=1):
                print(f"{i}. {categoria}")

            print("0. Torna indietro")

            scelta_categoria = input(
                "\nScegli categoria lavoro: "
            )

            if scelta_categoria == "0":
                continue

            categoria_scelta = categorie[
                int(scelta_categoria) - 1
            ]

            while True:

                print(f"\n--- {categoria_scelta} ---")

                for numero, dati in lavori[
                    categoria_scelta
                ].items():

                    print(f"\n{numero}. {dati['lavoro']}")

                    print(
                        f"Stipendio giornaliero: "
                        f"{dati['stipendio']}€"
                    )

                    print(
                        f"Posti rimasti: "
                        f"{dati['posti']}"
                    )

                print("0. Torna indietro")

                scelta = input(
                    "\nScegli un lavoro: "
                )

                if scelta == "0":
                    break

                lavoro = lavori[
                    categoria_scelta
                ][int(scelta)]

                if lavoro["posti"] > 0:

                    nome = input(
                        "\nInserisci il tuo nome: "
                    )

                    lavoro["posti"] -= 1

                    print("\n================================")
                    print("   ISCRIZIONE COMPLETATA")
                    print("================================")

                    print(f"Nome: {nome}")

                    print(
                        f"Lavoro: "
                        f"{lavoro['lavoro']}"
                    )

                    print(
                        f"Posti rimasti: "
                        f"{lavoro['posti']}"
                    )

                    break

                else:

                    print("\nPosti terminati!")

        # =====================================
        # INSERIMENTO LAVORO
        # =====================================

        elif scelta_menu == "2":

            print("\n================================")
            print("       INSERISCI LAVORO")
            print("================================")

            categorie = list(lavori.keys())

            print("\nCategorie disponibili:\n")

            for i, categoria in enumerate(categorie, start=1):
                print(f"{i}. {categoria}")

            print("0. Crea nuova categoria")

            scelta_categoria = input(
                "\nScegli una categoria: "
            )

            # nuova categoria
            if scelta_categoria == "0":

                nuova_categoria = input(
                    "\nInserisci nome nuova categoria: "
                )

                lavori[nuova_categoria] = {}

                categoria_scelta = nuova_categoria

            else:

                categoria_scelta = categorie[
                    int(scelta_categoria) - 1
                ]

            nome_lavoro = input(
                "\nInserisci nome lavoro: "
            )

            stipendio = int(input(
                "Inserisci stipendio giornaliero: "
            ))

            posti = int(input(
                "Inserisci posti disponibili: "
            ))

            nuovo_id = len(
                lavori[categoria_scelta]
            ) + 1

            lavori[categoria_scelta][nuovo_id] = {

                "lavoro": nome_lavoro,
                "stipendio": stipendio,
                "posti": posti
            }

            print("\n================================")
            print("    POSTO DI LAVORO INSERITO")
            print("================================")

            print(f"Categoria: {categoria_scelta}")
            print(f"Lavoro: {nome_lavoro}")
            print(f"Stipendio: {stipendio}€")
            print(f"Posti: {posti}")

        # =====================================
        # TORNA ALLA HOME
        # =====================================

        elif scelta_menu == "3":
            return

        # =====================================
        # ERRORE
        # =====================================

        else:
            print("\nOpzione non valida.")

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
    print("4. Lavora ad un evento")
    print("5. Esci")

    scelta = input("\nSeleziona un'opzione: ")

    if scelta == "1":
        iscrizione()

    elif scelta == "2":
        visualizza_eventi()

    elif scelta == "3":
        crea_evento()

    elif scelta == "4":
        lavora_evento()

    elif scelta == "5":

        print("\nChiusura programma...")
        break

    else:
        print("\nOpzione non valida.")