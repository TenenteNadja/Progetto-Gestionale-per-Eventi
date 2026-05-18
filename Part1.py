# ==============================
# EVENTHUB - TIPOLOGIE EVENTI
# ==============================

# Dizionario principale contenente tutte le categorie

eventi = {

    "Sportivi": {
        1: "Torneo del Teatro",
        2: "Kart Racing Lombardia",
        3: "Street Basket Milano",
        4: "Volley Summer Cup"
    },

    "Concerti": {
        1: "Night Sound Festival",
        2: "Rock in Piazza",
        3: "Jazz sotto le Stelle"
    },

    "Fiere": {
        1: "Expo Tech Future",
        2: "Comics & Games",
        3: "Auto Moto Show"
    },

    "Feste": {
        1: "Sagra della Castagna",
        2: "Mercatini di Natale",
        3: "Notte Bianca"
    },

    "Raduni": {
        1: "Motoraduno Nazionale",
        2: "Cosplay Gathering",
        3: "Raduno Auto Storiche"
    }

}

# ==============================
# MENU CATEGORIE
# ==============================

print("=== EVENTHUB MANAGER ===\n")

print("Categorie disponibili:\n")

categorie = list(eventi.keys())

for i, categoria in enumerate(categorie, start=1):
    print(f"{i}. {categoria}")

# ==============================
# SCELTA UTENTE
# ==============================

scelta = int(input("\nScegli una categoria: "))

categoria_scelta = categorie[scelta - 1]

print(f"\nHai scelto: {categoria_scelta}")

# ==============================
# VISUALIZZAZIONE EVENTI
# ==============================

print("\nEventi disponibili:\n")

for numero, nome_evento in eventi[categoria_scelta].items():
    print(f"{numero}. {nome_evento}")