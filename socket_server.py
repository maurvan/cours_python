import socket

# création du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# liaison à l'ip
serv_addr = ("0.0.0.0", 9001)
server_socket.bind(serv_addr)

# écoute entrante de max 5 clients
server_socket.listen(5)
print(f"Listening on {serv_addr[0]}:{serv_addr[1]}")

while True:
    print("Awaiting connection...")

    # Acceptation connexion
    client_socket, client_addr = server_socket.accept()
    print(f"New client found {client_addr[0]}:{client_addr[1]}")

    # traitement données
    data = client_socket.recv(1024)
    if data:
        print(f"Client says: {data.decode('utf-8')}")
        if data.decode('utf-8') == "chaussette\n":
            print("Going away now")
            response = "Master gave Dobby a sock, Dobby is a free elf!"
            client_socket.send(response.encode("utf-8"))
            client_socket.close()
            break

    # Réponse
    response = "Thank you, bye"
    client_socket.send(response.encode("utf-8"))

    # Fin de comm
    client_socket.close()
