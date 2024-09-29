import socket
import threading

# Function to continuously receive messages from the server
def receive_messages(s):
    while True:
        try:
            incoming_message = s.recv(1024).decode()
            if not incoming_message:  # If no message, connection was closed
                print("Connection closed by the server.")
                break
            print(f"Server: {incoming_message}")
        except:
            print("Error receiving message from the server.")
            break

def start_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'  # Connect to the local server
    port = 1234
    try:
        s.connect((host, port))
        print("Connected to server")
    except Exception as e:
        print("Connection to server failed:", e)
        return

    # Start a thread to continuously listen for messages from the server
    threading.Thread(target=receive_messages, args=(s,)).start()

    # Main loop to send messages from the client
    while True:
        try:
            message = input("You: ")
            if message.lower() == "exit":
                s.send("Goodbye!".encode())
                break
            s.send(message.encode())
        except:
            print("Error sending message to the server.")
            break

    s.close()
    print("Connection closed.")

if __name__ == "__main__":
    start_client()
