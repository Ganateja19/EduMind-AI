# Deployment Guide

# Deployment Guide

This guide explains how to deploy the Machine Learning Project to production.

> [!IMPORTANT]
> **Before you start:** matches the code you have running locally, you **MUST** save/commit your changes.
> 1. The `artifacts/` folder (containing `model.pkl` and `preprocessor.pkl`) must be included in your upload/repository.
> 2. The new `templates/home.html` and fixed `app.py` must be included.

You can choose between:
1.  **Render.com** (Easiest & Free)
2.  **Docker** (Recommended for portability)
3.  **Azure Web Apps**
4.  **AWS Elastic Beanstalk**

## 1. Render.com (Quickest Method)
Render is a cloud platform that connects to your GitHub and deploys automatically.

1.  **Push your code to GitHub**.
2.  Go to [dashboard.render.com](https://dashboard.render.com).
3.  Click **New +** -> **Web Service**.
4.  Connect your GitHub repository.
5.  Settings:
    - **Runtime**: Python 3
    - **Build Command**: `pip install -r requirements.txt`
    - **Start Command**: `gunicorn app:app` (or `python app.py`)
6.  Click **Create Web Service**.

## 2. Docker (Recommended)

Docker allows you to package the application and its dependencies into a single container that runs anywhere.

### Prerequisites
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop).

### Build and Run Locally
1.  Open a terminal in the project root.
2.  Build the Docker image:
    ```bash
    docker build -t mlproject .
    ```
3.  Run the container:
    ```bash
    docker run -p 5000:5000 mlproject
    ```
4.  Open your browser to `http://localhost:5000`.

## 2. Azure Web App

The project includes a GitHub Actions workflow (`.github/workflows/main_studentssperformance3.yml`) for continuous deployment to Azure.

### Setup Steps
1.  **Create an Azure Web App**:
    - Go to the [Azure Portal](https://portal.azure.com).
    - Create a new "Web App".
    - Runtime stack: **Python 3.8** (or 3.9).
    - OS: **Linux**.

2.  **Get Publish Profile**:
    - Go to your Web App resource.
    - Click **"Get publish profile"** in the Overview tab.
    - Save the downloaded file.

3.  **Configure GitHub Secrets**:
    - In your GitHub repository, go to **Settings > Secrets and variables > Actions**.
    - Create a new repository secret named `AZUREAPPSERVICE_PUBLISHPROFILE_DA91177C75E346B4BD3AD2EF1D318517` (matching the name in the workflow file, or update the workflow file to use a simpler name like `AZURE_WEBAPP_PUBLISH_PROFILE`).
    - Paste the content of the publish profile file into the secret value.

4.  **Trigger Deployment**:
    - Push changes to the `main` branch.
    - The GitHub Action will build and deploy the app efficiently.

## 3. AWS Elastic Beanstalk

The project contains an `.ebextensions` folder, making it ready for AWS Elastic Beanstalk.

### Setup Steps
1.  **Install EB CLI**:
    - `pip install awsebcli`

2.  **Initialize Application**:
    ```bash
    eb init -p python-3.8 mlproject-env
    ```

3.  **Create Environment & Deploy**:
    ```bash
    eb create mlproject-env
    ```

4.  **Open Application**:
    ```bash
    eb open
    ```

## 4. Manual Local Execution

If you cannot use Docker, you can run it with Python directly (requires Python installed).

1.  Create a virtual environment:
    ```bash
    python -m venv venv
    ```
2.  Activate it:
    - Windows: `venv\Scripts\activate`
    - Mac/Linux: `source venv/bin/activate`
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Run the app:
    ```bash
    python app.py
    ```
