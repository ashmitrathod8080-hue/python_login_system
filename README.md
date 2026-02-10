# Python Login System

A simple socket-based login system built with Python that authenticates users against a SQLite database.

## Features

- **Server-Client Architecture**: TCP socket-based communication
- **Secure Password Storage**: Passwords are hashed using SHA-256
- **SQLite Database**: Lightweight database for storing user credentials
- **Multi-threaded Server**: Handles multiple client connections simultaneously

## Project Structure

```
python_login_system/
├── server.py      # Main server that handles authentication
├── client.py      # Client application for login
├── sample.py      # Database initialization script
└── sample.db      # SQLite database (created on first run)
```

## Getting Started

### Prerequisites
- Python 3.6+
- No external dependencies (uses built-in libraries only)

### Setup

1. **Initialize the database** with test users:
   ```bash
   python3 sample.py
   ```

2. **Start the server** (in one terminal):
   ```bash
   python3 server.py
   ```
   The server will listen on `localhost:12345`

3. **Run the client** (in another terminal):
   ```bash
   python3 client.py
   ```

### Test Credentials

You can log in with any of these test accounts:

| Username | Password |
|----------|----------|
| ramesh21 | ramesh21 |
| gukesh77 | chesschuss69 |
| mukesh331 | footballisgreat123 |
| ninja41 | passwordninja |

## How It Works

1. The **server** accepts client connections on port 12345
2. It prompts the client for a username and password
3. The password is hashed with SHA-256 and compared against the database
4. Returns "Login successful!" or "Login failed!" based on the match

## Security Note

This is a learning project. For production use, implement proper security measures like:
- Use stronger hashing algorithms (bcrypt, argon2)
- Add SSL/TLS encryption
- Implement rate limiting and account lockout
- Use prepared statements (already done with parameterized queries)

