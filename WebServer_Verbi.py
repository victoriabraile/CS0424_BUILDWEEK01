import requests


def main():

    host = input("Inserisci url dell'host: ")
    porta = input("Inserisci porta: ")

    if porta == "80":
        url = f"http://{host}:{porta}"
    elif porta == "443":
        url = f"https://{host}:{porta}"
    else:
        print("Controlla la porta inserita!")
        return


    print(f"Verifico: {url}")

    try:
        risposta = requests.options(url)
        if risposta.status_code == 200:
            if 'Allow' in risposta.headers:
                metodi = risposta.headers['Allow']
                print(f"Ecco i metodi abilitati: {metodi}")
            else:
                print("Allow non è presente nella risposta\n")
        else:
            print(f"Codice di stato: {risposta.status_code}")
    except requests.RequestException as e:
        print(f"Errore nella richiesta: {e}")



if __name__ == "__main__":
    main()
