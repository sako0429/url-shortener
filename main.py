from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import RedirectResponse
import string, random, json, os

app = FastAPI()
DATA_FILE = "data.json"

# Load saved URLs or initialize
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        url_map = json.load(f)
else:
    url_map = {}

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(url_map, f)

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.post("/shorten/")
def shorten_url(long_url: str = Form(...)):
    code = generate_code()
    while code in url_map:
        code = generate_code()
    url_map[code] = long_url
    save_data()
    return {"short_url": f"http://localhost:8000/{code}"}

@app.get("/{code}")
def redirect(code: str):
    long_url = url_map.get(code)
    if not long_url:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return RedirectResponse(url=long_url)
