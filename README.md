                                          Readme for our Chat Application Architecture

Readme for PUBSUB Architecture

Table of Contents
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [API Usage](#api-usage)
- [Contributing](#contributing)
Technologies Used
- *Node.js*: JavaScript runtime for building the server.
- *Socket.IO*: Enables real-time, bidirectional communication between clients and
servers.
- *Redis*: Used as a message broker for Pub/Sub architecture.
- *Prisma*: An ORM for managing database interactions with PostgreSQL.
- *TypeScript*: For type safety and improved development experience.
Getting Started
To get started with the project, follow these steps:
1. Clone the repository:
git clone https://github.com/yourusername/repo.git
cd repo
2. Navigate to the server directory and install dependencies:
cd apps/server
npm install
3. Set up your PostgreSQL database and configure your .env file accordingly.
4. Navigate to the web directory and install dependencies:
cd ../web
npm install
5. Build and start the server:
npm run build
npm start
6. To start the development environment with automatic recompilation: npm run
dev
Project Structure
The project consists of the following main directories:
- apps/server: Contains the server-side code, including WebSocket handling, Redis
setup, and database interaction via Prisma.
- apps/web: Contains the front-end application code (if applicable).
Key Files
- *apps/server/src/services/prisma.ts*: Initializes the Prisma client for database
interaction.
- *apps/server/src/services/socket.ts*: Handles WebSocket connections and
message broadcasting using Redis.
- *apps/server/src/index.ts*: Entry point for the server, initializes the HTTP server
and SocketiO.
API Usage
WebSocket API
- *Connect*: Clients can connect to the WebSocket server to receive real-time
messages.
- *Message Event*: Emit a message using the event event:message: javascript
socket.emit("event:message", { message: "Hello, World!" });
- Messages published to Redis are automatically broadcast to all connected
clients.

 Readme for our Multiple Client Server Architecture

 Prerequisites
To run this application, you need:
● Python 3.x
● Basic knowledge of networking and socket programming.
● Required libraries (socket and threading) are part of the standard Python library,
so no external installations are needed.
How It Works
1. Server:
○ Manages client connections.
○ Handles incoming messages from each client.
○ Broadcasts messages to all connected clients.
○ Allows server-side input to send messages to clients.
2. Client:
○ Connects to the server.
○ Listens for incoming messages.
○ Allows users to send messages to the server.

Folder Structure
bash
Copy code
.
├── server.py # Server-side code
├── client.py # Client-side code
└── README.md # This README file

How to Run the Application
Step 1: Start the Server
1. Open a terminal/command prompt.
2. Navigate to the folder containing the server.py file.
Run the server using:
python server.py
3. The server will start and wait for incoming client connections. You will see a message
like:

Server started on localhost:1234

Step 2: Run Multiple Clients
1. Open a new terminal/command prompt.
2. Navigate to the folder containing the client.py file.
Run the client using:
python client.py
3. When the client successfully connects, it will display:
Connected to server

4. You can now start typing messages. Similarly, open more terminals to start additional
clients and connect them to the server.
Step 3: Communication
● Type messages in the client terminal and see them broadcasted to other clients.
● The server can also send messages to all clients by typing directly into the server
terminal.
Step 4: Closing Connections
● To exit a client, type exit. This will send a disconnection message and close the
connection.
● The server will continue running until you terminate it manually (Ctrl + C).
1.

Code Explanation
server.py:
● Sets up a server socket and listens for incoming connections.
● For each client, a new thread is created using handle_client to manage
communication.
● Broadcast functionality sends server messages to all connected clients.
● Clients are managed in a shared list (clients).
client.py:
● Connects to the server and starts a listener thread (receive_messages) to receive
messages.
● The main loop allows clients to input messages and send them to the server.
● The client can gracefully disconnect using the keyword exit.

  









