# ==============================
# EVENTHUB MANAGER
# Gestione completa categorie
# ==============================

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
        },

        4: {
            "nome": "Volley Summer Cup",
            "posti": 3
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

    # ==========================
    # FESTE E SAGRE
    # ==========================

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
            "nome": "Notte Bianca",
            "posti": 0
        },

        4: {
            "nome": "Festival del Cibo Locale",
            "posti": 18
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
        },

        3: {
            "nome": "Raduno Auto Storiche",
            "posti": 0
        },

        4: {
            "nome": "Community Anime Italia",
            "posti": 10
        }
    },

    # ==========================
    # WORKSHOP
    # ==========================

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

# ==============================
# MENU PRINCIPALE
# ==============================

print("================================")
print(" EVENTHUB MANAGER")
print("================================")

print("\nCategorie disponibili:\n")

categorie = list(eventi.keys())

for i, categoria in enumerate(categorie, start=1):
    print(f"{i}. {categoria}")

# ==============================
# SCELTA CATEGORIA
# ==============================

scelta_categoria = int(input("\nScegli una categoria: "))

categoria_scelta = categorie[scelta_categoria - 1]

print(f"\nHai scelto: {categoria_scelta}")

# ==============================
# SCELTA EVENTO
# ==============================

while True:

    print("\nEventi disponibili:\n")

    for numero, dati in eventi[categoria_scelta].items():

        print(
            f"{numero}. "
            f"{dati['nome']} "
            f"- Posti disponibili: {dati['posti']}"
        )

    scelta_evento = int(input("\nScegli un evento: "))

    evento = eventi[categoria_scelta][scelta_evento]

    # ==========================
    # CONTROLLO POSTI
    # ==========================

    if evento["posti"] > 0:

        print("\nPosti disponibili!")

        nome_utente = input("Inserisci il tuo nome: ")

        # Riduce i posti disponibili
        evento["posti"] -= 1

        print("\n========================")
        print("ISCRIZIONE COMPLETATA")
        print("========================")

        print(f"Utente: {nome_utente}")
        print(f"Evento: {evento['nome']}")
        print(f"Posti rimasti: {evento['posti']}")

        break

    else:

        print("\n========================")
        print("EVENTO AL COMPLETO")
        print("========================")

        print("Scegli un altro evento.")
