import random
import socket

to_guess = random.randint(1, 100000000)

# création du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# liaison à l'ip
serv_addr = ('0.0.0.0', 9001)
server_socket.bind(serv_addr)

# écoute entrante de max 5 client
server_socket.listen(5)
print(f"Listening on {serv_addr[0]}:{serv_addr[1]}")
print(f"Correct guess is {to_guess}")

while True:
    print('Awaiting connection...')
    # Acceptation connexion
    client_socket, client_addr = server_socket.accept()
    print(f"New client found {client_addr[0]}:{client_addr[1]}")
    hello = "Hi welcome to the guessing game guess the number i'm thinking of between 1 and 100.000.000\n"
    client_socket.send(hello.encode('utf-8'))

    # traitement données
    data = client_socket.recv(1024)
    if data:
        print(f"Client says: {data.decode('utf-8').strip()}")
        try:
            guess = int(data.decode('utf-8').strip())
        except ValueError:
            response = "Invalid data only int is accepted"
            client_socket.send(response.encode('utf-8'))
            client_socket.close()
            continue

        if guess > to_guess:
            response = "Too high\n"

        elif guess < to_guess:
            response = "Too low\n"

        else:
            response = "Bingo ! A winner is you !\n Here is the password: 18574115dbcd47d71e7eb9da74e45bf2\n"

        client_socket.send(response.encode('utf-8'))

    client_socket.close()
