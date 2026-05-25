# =========================================
# EVENTHUB MANAGER
# COMMIT 6
# Calendario Eventi + Date + Cerimonie
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
            "orario": "15:00",
            "data": "12/06/2026"
        },

        2: {
            "nome": "Kart Racing Emilia Romagna",
            "posti": 7,
            "luogo": "Kartodromo Happy Valley",
            "orario": "10:30",
            "data": "15/06/2026"
        },

        3: {
            "nome": "Street Basket Rimini",
            "posti": 5,
            "luogo": "Palazzetto dello sport Rimini",
            "orario": "18:00",
            "data": "20/06/2026"
        },

        4: {
            "nome": "Beach Volley cup Cesenatico",
            "posti": 3,
            "luogo": "Bagno Roma, Cesenatico",
            "orario": "15:00",
            "data": "25/06/2026"
        }
    },

    "Concerti": {

        1: {
            "nome": "Kanye West",
            "posti": 88,
            "luogo": "Reggio Emilia",
            "orario": "21:00",
            "data": "30/06/2026"
        },

        2: {
            "nome": "Artie 5ive",
            "posti": 6,
            "luogo": "Bologna",
            "orario": "20:30",
            "data": "10/07/2026"
        },

        3: {
            "nome": "Tonypitony",
            "posti": 69,
            "luogo": "Beky Bay, Bellaria Igea Marina",
            "orario": "22:00",
            "data": "15/07/2026"
        }
    },

    "Feste e Sagre": {

        1: {
            "nome": "San Martino",
            "posti": 45,
            "luogo": "Santarcangelo",
            "orario": "09:00",
            "data": "11/11/2026"
        },

        2: {
            "nome": "RiminiWellness",
            "posti": 30,
            "luogo": "Rimini",
            "orario": "11:00",
            "data": "01/06/2026"
        },

        3: {
            "nome": "Sagra della Cozza",
            "posti": 15,
            "luogo": "Ravenna",
            "orario": "19:00",
            "data": "18/08/2026"
        },

        4: {
            "nome": "Festa della Sburdela",
            "posti": 50,
            "luogo": "Riolo Terme",
            "orario": "10:00",
            "data": "03/09/2026"
        }
    },

    "Raduni": {

        1: {
            "nome": "Motoraduno Nazionale",
            "posti": 25,
            "luogo": "Misano",
            "orario": "14:00",
            "data": "05/07/2026"
        },

        2: {
            "nome": "Vespa Club Bellaria",
            "posti": 41,
            "luogo": "Bellaria",
            "orario": "10:30",
            "data": "08/07/2026"
        },

        3: {
            "nome": "Raduno Auto Storiche",
            "posti": 55,
            "luogo": "Imola",
            "orario": "11:00",
            "data": "12/07/2026"
        },

        4: {
            "nome": "Aprilia Scarabeo Club",
            "posti": 67,
            "luogo": "Gatteo",
            "orario": "10:30",
            "data": "16/07/2026"
        }
    },

    "Cinema": {

        1: {
            "nome": "Dune Parte Due",
            "posti": 40,
            "luogo": "Cinema Moderno",
            "orario": "21:15",
            "data": "02/06/2026"
        },

        2: {
            "nome": "Inside Out 2",
            "posti": 25,
            "luogo": "Cinema Centrale",
            "orario": "18:30",
            "data": "05/06/2026"
        },

        3: {
            "nome": "Deadpool & Wolverine",
            "posti": 12,
            "luogo": "Multisala Europa",
            "orario": "22:00",
            "data": "09/06/2026"
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
    },

    "Cerimonie": {

        1: {
            "lavoro": "Fotografo Matrimoni",
            "stipendio": 150,
            "posti": 2
        },

        2: {
            "lavoro": "Fotografo Cresime",
            "stipendio": 100,
            "posti": 3
        },

        3: {
            "lavoro": "DJ Matrimoni",
            "stipendio": 180,
            "posti": 1
        },

        4: {
            "lavoro": "Cameriere Cerimonie",
            "stipendio": 85,
            "posti": 5
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
            print(f"Data: {dati['data']}")
            print(f"Luogo: {dati['luogo']}")
            print(f"Orario: {dati['orario']}")
            print(f"Posti disponibili: {dati['posti']}")

# =========================================
# CALENDARIO EVENTI
# =========================================

def calendario_eventi():

    lista_eventi = []

    for categoria, eventi_categoria in eventi.items():

        for numero, dati in eventi_categoria.items():

            lista_eventi.append({
                "categoria": categoria,
                "nome": dati["nome"],
                "data": dati["data"],
                "luogo": dati["luogo"],
                "orario": dati["orario"]
            })

    lista_eventi.sort(key=lambda x: (
        x["data"][6:10],
        x["data"][3:5],
        x["data"][0:2]
    ))

    print("\n================================")
    print("      CALENDARIO EVENTI")
    print("================================")

    for evento in lista_eventi:

        print(f"\n{evento['data']} - {evento['nome']}")
        print(f"Categoria: {evento['categoria']}")
        print(f"Luogo: {evento['luogo']}")
        print(f"Orario: {evento['orario']}")

# =========================================
# CREA EVENTO
# =========================================

def crea_evento():

    categorie = list(eventi.keys())

    print("\nCategorie disponibili:\n")

    for i, categoria in enumerate(categorie, start=1):
        print(f"{i}. {categoria}")

    print("0. Crea nuova categoria")

    scelta = input("\nScegli una categoria: ")

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
    data = input("Data evento (gg/mm/aaaa): ")
    orario = input("Orario evento: ")
    posti = int(input("Posti disponibili: "))

    nuovo_id = len(eventi[categoria_scelta]) + 1

    eventi[categoria_scelta][nuovo_id] = {

        "nome": nome_evento,
        "posti": posti,
        "luogo": luogo,
        "orario": orario,
        "data": data
    }

    print("\n================================")
    print("      EVENTO CREATO")
    print("================================")

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
    print("5. Calendario eventi")
    print("6. Esci")

    scelta = input("\nSeleziona un'opzione: ")

    if scelta == "2":
        visualizza_eventi()

    elif scelta == "3":
        crea_evento()

    elif scelta == "5":
        calendario_eventi()

    elif scelta == "6":

        print("\nChiusura programma...")
        break

    else:
        print("\nFunzione disponibile nel codice completo.")