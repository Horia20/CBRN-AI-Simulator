from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

SCENARIOS = [
    "Nuclear Fallout",
    "Dirty Bomb",
    "Sarin Release",
    "Anthrax Outbreak",
    "Chlorine Release"
]

def generate_scenario():
    return {
        "threat": random.choice(SCENARIOS),
        "wind": random.randint(5, 30),
        "casualties": random.randint(10, 500),
        "population": random.randint(1000, 10000)
    }

CURRENT_SCENARIO = generate_scenario()

@app.get("/", response_class=HTMLResponse)
def home():

    return f"""
    <html>
    <head>
    <title>CBRN Tactical Trainer V2</title>

    <style>

    body {{
        background:#0f172a;
        color:white;
        font-family:Arial;
        margin:40px;
    }}

    .card {{
        background:#1e293b;
        padding:20px;
        border-radius:12px;
        margin-bottom:20px;
    }}

    textarea {{
        width:100%;
        height:150px;
    }}

    button {{
        background:#2563eb;
        color:white;
        border:none;
        padding:12px;
        border-radius:10px;
    }}

    </style>
    </head>

    <body>

    <h1>CBRN Tactical Trainer V2</h1>

    <div class="card">
    <h2>Scenario</h2>

    <p><b>Threat:</b> {CURRENT_SCENARIO["threat"]}</p>
    <p><b>Wind:</b> {CURRENT_SCENARIO["wind"]} km/h</p>
    <p><b>Casualties:</b> {CURRENT_SCENARIO["casualties"]}</p>
    <p><b>Population:</b> {CURRENT_SCENARIO["population"]}</p>

    </div>

    <div class="card">

    <h2>Commander Decision</h2>

    <form action="/evaluate" method="post">

    <textarea name="decision"></textarea>

    <br><br>

    <button type="submit">
    Evaluate Decision
    </button>

    </form>

    </div>

    </body>
    </html>
    """

@app.post("/evaluate", response_class=HTMLResponse)
def evaluate(decision: str = Form(...)):

    text = decision.lower()

    score = 0

    if "evac" in text:
        score += 25

    if "cbrn" in text:
        score += 25

    if "decont" in text:
        score += 25

    if "medical" in text:
        score += 25

    cbrn = []
    medical = []
    ops = []

    if "cbrn" not in text:
        cbrn.append("Missing CBRN reconnaissance.")

    if "decont" not in text:
        cbrn.append("No decontamination plan.")

    if "medical" not in text:
        medical.append("Medical support not mentioned.")

    if "evac" not in text:
        medical.append("Evacuation plan missing.")

    if "cordon" not in text:
        ops.append("No security perimeter established.")

    if "reserve" not in text:
        ops.append("No reserve force identified.")

    return f"""
    <html>
    <body style="background:#0f172a;color:white;font-family:Arial;padding:40px;">

    <h1>Decision Assessment</h1>

    <h2>Score: {score}/100</h2>

    <h2>CBRN Officer</h2>
    <ul>
    {''.join(f'<li>{x}</li>' for x in cbrn)}
    </ul>

    <h2>Medical Officer</h2>
    <ul>
    {''.join(f'<li>{x}</li>' for x in medical)}
    </ul>

    <h2>Operations Officer</h2>
    <ul>
    {''.join(f'<li>{x}</li>' for x in ops)}
    </ul>

    <br>

    <a href="/" style="color:cyan;">
    Back
    </a>

    </body>
    </html>
    """
