# =========================================
# EVENTHUB MANAGER
# COMMIT 7 COMPLETO
# - Admin Panel
# - Biglietti
# =========================================

# =========================================
# PASSWORD ADMIN
# =========================================

password_admin = "Sergio11"

# =========================================
# DATABASE UTENTI
# =========================================

utenti = []

# =========================================
# DATABASE BIGLIETTI (AGGIUNTO)
# =========================================

biglietti = []

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
# BIGLIETTO
# =========================================

def stampa_biglietto(nome_utente, evento):

    print("\n================================")
    print("          BIGLIETTO")
    print("================================")

    print(f"Utente: {nome_utente}")
    print(f"Evento: {evento['nome']}")
    print(f"Data: {evento['data']}")
    print(f"Luogo: {evento['luogo']}")
    print(f"Orario: {evento['orario']}")

    print("================================")

    # AGGIUNTA BIGLIETTO
    biglietti.append({
        "utente": nome_utente,
        "evento": evento.copy()
    })

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
# CERCA EVENTI
# =========================================

def cerca_evento():

    ricerca = input("\nInserisci nome evento: ").lower()

    risultati = []

    for categoria, lista_eventi in eventi.items():
        for numero, dati in lista_eventi.items():

            if ricerca in dati["nome"].lower():

                risultati.append({
                    "categoria": categoria,
                    "id": numero,
                    "evento": dati
                })

    if len(risultati) == 0:
        print("\nNessun evento trovato.")
        return

    print("\n================================")
    print("       RISULTATI RICERCA")
    print("================================")

    for i, risultato in enumerate(risultati, start=1):

        evento = risultato["evento"]

        print(f"\n{i}. {evento['nome']}")
        print(f"Categoria: {risultato['categoria']}")
        print(f"Data: {evento['data']}")
        print(f"Luogo: {evento['luogo']}")
        print(f"Posti: {evento['posti']}")

    scelta = int(input("\nScegli evento: "))

    evento_scelto = risultati[scelta - 1]
    evento = evento_scelto["evento"]

    if evento["posti"] > 0:

        nome = input("\nInserisci il tuo nome: ")

        utenti.append(nome)
        evento["posti"] -= 1

        print("\nISCRIZIONE COMPLETATA!")

        stampa_biglietto(nome, evento)

    else:
        print("\nEvento al completo!")

# =========================================
# ISCRIZIONE EVENTI
# =========================================

def iscrizione():

    while True:

        print("\n================================")
        print("       ISCRIZIONE EVENTI")
        print("================================")

        print("\n1. Scegli categoria")
        print("2. Cerca evento")
        print("3. Torna alla Home")

        scelta = input("\nSeleziona opzione: ")

        if scelta == "1":

            categorie = list(eventi.keys())

            for i, categoria in enumerate(categorie, start=1):
                print(f"{i}. {categoria}")

            print("0. Torna indietro")

            scelta_categoria = input("\nScegli categoria: ")

            if scelta_categoria == "0":
                continue

            categoria_scelta = categorie[int(scelta_categoria) - 1]

            while True:

                print(f"\n--- {categoria_scelta} ---")

                for numero, dati in eventi[categoria_scelta].items():

                    print(f"\n{numero}. {dati['nome']}")
                    print(f"Data: {dati['data']}")
                    print(f"Luogo: {dati['luogo']}")
                    print(f"Orario: {dati['orario']}")
                    print(f"Posti: {dati['posti']}")

                print("0. Torna indietro")

                scelta_evento = input("\nScegli evento: ")

                if scelta_evento == "0":
                    break

                evento = eventi[categoria_scelta][int(scelta_evento)]

                if evento["posti"] > 0:

                    nome = input("\nInserisci il tuo nome: ")

                    utenti.append(nome)
                    evento["posti"] -= 1

                    print("\nISCRIZIONE COMPLETATA!")

                    stampa_biglietto(nome, evento)

                    break

                else:
                    print("\nEvento al completo!")

        elif scelta == "2":
            cerca_evento()

        elif scelta == "3":
            return

        else:
            print("\nOpzione non valida.")

# =========================================
# CREA EVENTO
# =========================================

def crea_evento():

    categorie = list(eventi.keys())

    print("\nCategorie disponibili:\n")

    for i, categoria in enumerate(categorie, start=1):
        print(f"{i}. {categoria}")

    print("0. Crea nuova categoria")

    scelta = input("\nScegli categoria: ")

    if scelta == "0":
        nuova_categoria = input("\nNuova categoria: ")
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

    print("\nEVENTO CREATO!")

# =========================================
# LAVORA EVENTO
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

        if scelta_menu == "1":

            categorie = list(lavori.keys())

            for i, categoria in enumerate(categorie, start=1):
                print(f"{i}. {categoria}")

            print("0. Torna indietro")

            scelta_categoria = input("\nScegli categoria lavoro: ")

            if scelta_categoria == "0":
                continue

            categoria_scelta = categorie[int(scelta_categoria) - 1]

            while True:

                print(f"\n--- {categoria_scelta} ---")

                for numero, dati in lavori[categoria_scelta].items():

                    print(f"\n{numero}. {dati['lavoro']}")
                    print(f"Stipendio giornaliero: {dati['stipendio']}€")
                    print(f"Posti rimasti: {dati['posti']}")

                print("0. Torna indietro")

                scelta = input("\nScegli un lavoro: ")

                if scelta == "0":
                    break

                lavoro = lavori[categoria_scelta][int(scelta)]

                if lavoro["posti"] > 0:

                    nome = input("\nInserisci il tuo nome: ")
                    lavoro["posti"] -= 1

                    print("\n================================")
                    print("   ISCRIZIONE COMPLETATA")
                    print("================================")

                    print(f"Nome: {nome}")
                    print(f"Lavoro: {lavoro['lavoro']}")
                    print(f"Posti rimasti: {lavoro['posti']}")

                    break

                else:
                    print("\nPosti terminati!")

        elif scelta_menu == "2":

            print("\n================================")
            print("       INSERISCI LAVORO")
            print("================================")

            categorie = list(lavori.keys())

            print("\nCategorie disponibili:\n")

            for i, categoria in enumerate(categorie, start=1):
                print(f"{i}. {categoria}")

            print("0. Crea nuova categoria")

            scelta_categoria = input("\nScegli una categoria: ")

            if scelta_categoria == "0":
                nuova_categoria = input("\nInserisci nome nuova categoria: ")
                lavori[nuova_categoria] = {}
                categoria_scelta = nuova_categoria
            else:
                categoria_scelta = categorie[int(scelta_categoria) - 1]

            nome_lavoro = input("\nInserisci nome lavoro: ")
            stipendio = int(input("Inserisci stipendio giornaliero: "))
            posti = int(input("Inserisci posti disponibili: "))

            nuovo_id = len(lavori[categoria_scelta]) + 1

            lavori[categoria_scelta][nuovo_id] = {
                "lavoro": nome_lavoro,
                "stipendio": stipendio,
                "posti": posti
            }

            print("\n================================")
            print("    POSTO DI LAVORO INSERITO")
            print("================================")

        elif scelta_menu == "3":
            return

        else:
            print("\nOpzione non valida.")

# =========================================
# ADMIN PANEL
# =========================================

def admin_panel():

    password = input("\nInserisci password admin: ")

    if password != password_admin:
        print("\nPassword errata!")
        return

    while True:

        print("\n================================")
        print("          ADMIN PANEL")
        print("================================")

        print("\n1. Visualizza utenti")
        print("2. Elimina utente")
        print("3. Modifica utente")
        print("4. Torna alla Home")
        print("5. Gestione eventi")

        scelta = input("\nSeleziona opzione: ")

        if scelta == "1":

            if len(utenti) == 0:
                print("\nNessun utente.")
            else:
                for i, utente in enumerate(utenti, start=1):
                    print(f"{i}. {utente}")

        elif scelta == "2":

            if len(utenti) == 0:
                print("\nNessun utente.")
                continue

            for i, utente in enumerate(utenti, start=1):
                print(f"{i}. {utente}")

            scelta_utente = int(input("\nUtente da eliminare: "))
            utenti.pop(scelta_utente - 1)

        elif scelta == "3":

            if len(utenti) == 0:
                print("\nNessun utente.")
                continue

            for i, utente in enumerate(utenti, start=1):
                print(f"{i}. {utente}")

            scelta_utente = int(input("\nUtente da modificare: "))
            nuovo_nome = input("Nuovo nome: ")
            utenti[scelta_utente - 1] = nuovo_nome

        elif scelta == "4":
            return

        elif scelta == "5":

            while True:

                print("\n================================")
                print("      GESTIONE EVENTI ADMIN")
                print("================================")

                print("\n1. Visualizza eventi")
                print("2. Modifica evento")
                print("3. Elimina evento")
                print("4. Torna indietro")

                scelta_ev = input("\nSeleziona opzione: ")

                if scelta_ev == "1":

                    for categoria, lista in eventi.items():
                        print(f"\n--- {categoria} ---")
                        for num, ev in lista.items():
                            print(f"\n{num}. {ev['nome']}")
                            print(f"Data: {ev['data']}")
                            print(f"Luogo: {ev['luogo']}")
                            print(f"Orario: {ev['orario']}")
                            print(f"Posti: {ev['posti']}")

                elif scelta_ev == "2":

                    cat_list = list(eventi.keys())

                    for i, c in enumerate(cat_list, start=1):
                        print(f"{i}. {c}")

                    c_scelta = int(input("\nCategoria: ")) - 1
                    categoria = cat_list[c_scelta]

                    ev_list = list(eventi[categoria].keys())

                    for i, e in enumerate(ev_list, start=1):
                        print(f"{i}. {eventi[categoria][e]['nome']}")

                    e_scelta = int(input("\nEvento da modificare: ")) - 1
                    ev_id = ev_list[e_scelta]

                    print("\nLascia vuoto per non modificare")

                    nuovo_nome = input("Nuovo nome: ")
                    nuovo_luogo = input("Nuovo luogo: ")
                    nuovo_data = input("Nuova data: ")
                    nuovo_orario = input("Nuovo orario: ")
                    nuovi_posti = input("Nuovi posti: ")

                    if nuovo_nome:
                        eventi[categoria][ev_id]["nome"] = nuovo_nome
                    if nuovo_luogo:
                        eventi[categoria][ev_id]["luogo"] = nuovo_luogo
                    if nuovo_data:
                        eventi[categoria][ev_id]["data"] = nuovo_data
                    if nuovo_orario:
                        eventi[categoria][ev_id]["orario"] = nuovo_orario
                    if nuovi_posti:
                        eventi[categoria][ev_id]["posti"] = int(nuovi_posti)

                elif scelta_ev == "3":

                    cat_list = list(eventi.keys())

                    for i, c in enumerate(cat_list, start=1):
                        print(f"{i}. {c}")

                    c_scelta = int(input("\nCategoria: ")) - 1
                    categoria = cat_list[c_scelta]

                    ev_list = list(eventi[categoria].keys())

                    for i, e in enumerate(ev_list, start=1):
                        print(f"{i}. {eventi[categoria][e]['nome']}")

                    e_scelta = int(input("\nEvento da eliminare: ")) - 1
                    ev_id = ev_list[e_scelta]

                    eventi[categoria].pop(ev_id)

                elif scelta_ev == "4":
                    break

                else:
                    print("\nOpzione non valida.")

# =========================================
# VISUALIZZA BIGLIETTI (AGGIUNTO)
# =========================================

def visualizza_biglietti():

    print("\n================================")
    print("        BIGLIETTI EMESSI")
    print("================================")

    if len(biglietti) == 0:
        print("\nNessun biglietto presente.")
        return

    for i, biglietto in enumerate(biglietti, start=1):

        evento = biglietto["evento"]

        print(f"\n{i}. Utente: {biglietto['utente']}")
        print(f"Evento: {evento['nome']}")
        print(f"Data: {evento['data']}")
        print(f"Luogo: {evento['luogo']}")
        print(f"Orario: {evento['orario']}")

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
    print("6. Admin Panel")
    print("7. Esci")
    print("8. Visualizza biglietti")

    scelta = input("\nSeleziona opzione: ")

    if scelta == "1":
        iscrizione()
    elif scelta == "2":
        visualizza_eventi()
    elif scelta == "3":
        crea_evento()
    elif scelta == "4":
        lavora_evento()
    elif scelta == "5":
        calendario_eventi()
    elif scelta == "6":
        admin_panel()
    elif scelta == "7":
        print("\nChiusura programma...")
        break
    elif scelta == "8":
        visualizza_biglietti()
    else:
        print("\nOpzione non valida.")