import network
import click

ADDRESS ="10.0.0.188"
PORT=1111

print("z ; a ; s ; q ; f ; r ; c ")
    
continuer = True
while continuer:

    socket = network.newClientSocket()
    socket.connect((ADDRESS,PORT))

    lettre = click.getchar()
    socket.send(lettre.encode())

    reponse = socket.recv(4096)
    print(reponse)
    if lettre == "c":
        continuer = False