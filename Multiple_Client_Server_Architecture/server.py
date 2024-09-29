import socket
import threading

clients = []  # List to keep track of connected clients

# Function to handle communication with a single client
def handle_client(conn, addr):
    print(f"{addr} has connected.")
    conn.send("Welcome to the server!".encode())  # Send welcome message to client

    while True:
        try:
            incoming_message = conn.recv(1024).decode()
            if not incoming_message:  # Client disconnected
                print(f"Client {addr} has disconnected.")
                break
            print(f"Client {addr}: {incoming_message}")
        except:
            print(f"Error with client {addr}. Closing connection.")
            break

    # Remove client from list and close the connection
    clients.remove(conn)
    conn.close()

# Function for the server to broadcast messages to all clients
def broadcast_message():
    while True:
        message = input("Server: ")  # Server can type a message to all clients
        for client in clients:
            try:
                client.send(f"Server: {message}".encode())
            except:
                print("Failed to send message to a client.")

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'  # Server running locally
    port = 1234
    s.bind((host, port))
    s.listen(2)  # Listen for up to 5 clients
    print(f"Server started on {host}:{port}")

    # Start a thread to handle server-side messaging to all clients
    threading.Thread(target=broadcast_message).start()

    while True:
        conn, addr = s.accept()  # Accept incoming client connections
        clients.append(conn)  # Add the client to the list of connected clients
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()
