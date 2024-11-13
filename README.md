# GitHub SSO Authentication with FastAPI

This application demonstrates how to set up a GitHub Single Sign-On (SSO) authentication flow using FastAPI and the `fastapi-sso` library. Users can log in with their GitHub accounts.

## Features

- **GitHub SSO Authentication**: Allows users to log in with GitHub credentials.
- **HTML Login Form**: Simple HTML form for initiating the GitHub login process.
- **Environment Variable Configuration**: Sensitive credentials are managed through environment variables using `dotenv`.

## Prerequisites

- Python 3.8 or higher
- GitHub account

## Setup

1. **Download the Project**:
   [Download the project here](https://github.com/your-repo-url/archive/refs/heads/main.zip)

2. **Install dependencies**:
   ```bash
   python3 -m venv venv 
   source venv/bin/activate
   pip install fastapi uvicorn python-dotenv fastapi-sso
   ```

3. **Configure GitHub OAuth App**:
   To enable GitHub SSO, you need to register your application with GitHub and obtain a `Client ID` and `Client Secret`. Follow the steps below to configure this:

### Creating a GitHub OAuth App

1. Go to [GitHub Developer Settings](https://github.com/settings/developers).
2. Click on **New OAuth App**.
3. Fill in the required fields:
   - **Application name**: (e.g., "FastAPI GitHub SSO")
   - **Homepage URL**: `http://127.0.0.1:5000`
   - **Authorization callback URL**: `http://127.0.0.1:5000/auth/callback`
4. Click **Register application**.
5. GitHub will provide you with a **Client ID** and **Client Secret** after registration. Copy these values as they are required to configure the app.

4. **Set Up Environment Variables**:
   - Create a `.env` file in the project directory:
     ```plaintext
     CLIENT_ID_GH=<your-client-id>
     CLIENT_SECRET_GH=<your-client-secret>
     ```
   - Replace `<your-client-id>` and `<your-client-secret>` with the values from your GitHub OAuth App.

5. **Run the Application**:
   Start the FastAPI application with `uvicorn`:
   ```bash
   uvicorn main:app --host 127.0.0.1 --port 5000 --reload
   ```

6. **Access the App**:
   Open your web browser and navigate to `http://127.0.0.1:5000`. You should see a login button to initiate the GitHub login process.

## Code Structure Overview

- **GitHub SSO Initialization**:
   - The `GithubSSO` instance is initialized with the `CLIENT_ID`, `CLIENT_SECRET`, and `redirect_uri`.
- **Authentication Endpoints**:
   - **`/auth/login`**: Initiates GitHub SSO login.
   - **`/auth/callback`**: Handles the callback from GitHub and verifies the user's identity.
- **HTML Login Form**: Simple form on the root (`/`) endpoint to trigger GitHub login.

## License

This project is open-source and available for modification and use according to your needs.
