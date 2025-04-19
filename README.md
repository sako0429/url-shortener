# URL Shortener

This is a simple URL shortener app built with **FastAPI**. It allows users to shorten URLs and store them in a JSON file. The project is version-controlled with GitHub and can be deployed to Render or other cloud platforms.

## Features

- Shorten long URLs into short codes
- Redirect short codes back to original URLs
- Data is saved in a `data.json` file
- Easy deployment to cloud services

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/url-shortener.git
    cd url-shortener
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app locally:**

    ```bash
    uvicorn main:app --reload
    ```

    The app will be running at `http://localhost:8000`.

4. **Use the /shorten endpoint** to shorten URLs:
    - Send a POST request with the long URL (e.g., `long_url=https://example.com`).
    - Receive a short URL in return.

    Example: `http://localhost:8000/shorten/`

5. **Redirect using the short URL**:
    - Access the short URL (e.g., `http://localhost:8000/abc123`).

---

## Deploying to Render

### Step 1: Sign up for a free Render account at [https://render.com](https://render.com).

### Step 2: Create a new **Web Service** from your GitHub repository:
1. Select your GitHub repository.
2. Set the environment to **Python**.
3. Set the build command to **`pip install -r requirements.txt`**.
4. Set the start command to **`uvicorn main:app --host 0.0.0.0 --port 80`**.

### Step 3: Deploy and access your URL shortener service on the Render domain.

---

## Contributing

Feel free to fork and submit pull requests for any improvements.
