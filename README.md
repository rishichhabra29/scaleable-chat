                                          Readme for our PUBSUB Architecture
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









