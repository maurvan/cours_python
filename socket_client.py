import socket
import random

# ip et port distant
serv_addr = ("192.168.2.225", 9001)

minimum = 1
maximum = 100000000001
total = 0

while True:
    # création du socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # établissement de la connexion
    client_socket.connect(serv_addr)

    # réception banner
    banner = client_socket.recv(1024)
    # print("Banner: ", banner.decode('utf-8'))

    # envoi de données
    guess = random.randint(minimum, maximum)
    print(f"Guessing: {guess}")
    client_socket.send(str(guess).encode('utf-8'))
    total += 1

    # reponse server
    response = client_socket.recv(1024)
    if response.decode('utf-8').strip() == "Too low":
        print(f"{guess} was too low")
        minimum = guess
        pass

    elif response.decode('utf-8').strip() == "Too high":
        print(f"{guess} was too high")
        maximum = guess
        pass

    else:
        print(f"YAY we won in {total} guesses!")
        print("Réponse: ", response.decode('utf-8').strip())
        client_socket.close()
        break

    # fermeture
    client_socket.close()