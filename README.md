# Server Purchase App

This project is a simple web application that allows users to sign up, log in, and view a marketplace to purchase CPU/GPU servers. The application uses `Streamlit` for the frontend and `SQLite` for the backend database.

## Features

- User Authentication (Sign Up, Login)
- Marketplace to view and purchase CPU/GPU resources
- User-specific marketplace information

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python (>=3.10.0, <3.11)
- Poetry (for dependency management)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/server-purchase-app.git
    cd server-purchase-app
    ```

2. Install dependencies:
    ```bash
    poetry install
    ```

3. Run the application:
    ```bash
    poetry run streamlit run main.py
    ```

### Usage

Once the application is running, open your web browser and navigate to the URL provided by Streamlit.

- **Sign Up**: Create a new user account.
- **Login**: Log in using your credentials.
- **Marketplace**: View and purchase CPU/GPU resources.

## Project Structure

- `main.py`: The entry point of the application, contains the Streamlit frontend logic.
- `database.py`: Contains functions for database operations (creating tables, adding users, verifying users).
- `pyproject.toml`: Project configuration and dependencies.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code adheres to the existing style and includes tests for any new functionality.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Replit](https://replit.com/) for providing an excellent online IDE and platform.
- [Streamlit](https://streamlit.io/) for the amazing web application framework.