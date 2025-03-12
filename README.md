# Money Making Machine

A simple **Streamlit** application that generates random money amounts and provides side hustle ideas and money-related quotes using a local API.

## Features

- 💰 Generate random money.
- 💡 Get side hustle ideas.
- 📝 Fetch money-related quotes.

## Installation

This project uses `uv` instead of `pip` for package management.


### Setup
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd <repo-folder>
   ```
2. Create a virtual environment:
   ```sh
   uv venv .venv
   ```
3. Activate the virtual environment:
   - **Windows:**
     ```sh
     .venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```sh
     source .venv/bin/activate
     ```
4. Install dependencies:
   ```sh
   uv pip install -r requirements.txt
   ```

## Usage
Run the Streamlit app with:
```sh
streamlit run app.py
```

## API Requirements
This app depends on a local API running at `http://127.0.0.1:8000`. Ensure your backend server is up before running the app.

### Expected API Endpoints
- **Side Hustle Ideas:** `GET http://127.0.0.1:8000/side_hustles?apiKey=12345`
- **Money Quotes:** `GET http://127.0.0.1:8000/money_quotes?apiKey=12345`

## Troubleshooting
- If the API calls fail, ensure the backend server is running.
- If `uv` is not found, reinstall it using the provided command.

## License
This project is open-source and available under the [MIT License](LICENSE).

