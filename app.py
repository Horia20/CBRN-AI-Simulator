from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

from core.scenario_engine import ScenarioEngine
from core.decision_engine import DecisionEngine
from core.scoring_engine import ScoringEngine
from core.aar_engine import AAREngine

app = FastAPI()

engine = ScenarioEngine()
decision_engine = DecisionEngine()
scoring_engine = ScoringEngine()
aar_engine = AAREngine()

CURRENT_WORLD = engine.generate()


@app.get("/", response_class=HTMLResponse)
def home():

    w = CURRENT_WORLD

    return HTMLResponse(f"""
<!DOCTYPE html>
<html>

<head>

<title>CBRN Trainer V4.2</title>

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

button {{
    background:#2563eb;
    color:white;
    border:none;
    padding:12px;
    border-radius:10px;
    cursor:pointer;
}}

textarea {{
    width:100%;
    height:140px;
}}

</style>

</head>

<body>

<h1>CBRN Tactical Trainer V4.2</h1>

<form action="/new_scenario" method="post">

<button type="submit">
Generate New Scenario
</button>

</form>

<br>

<div class="card">

<h2>Scenario</h2>

<p><b>Name:</b> {w.scenario_name}</p>

<p><b>Type:</b> {w.scenario_type}</p>

<p><b>Difficulty:</b> {w.difficulty}</p>

</div>

<div class="card">

<h2>World State</h2>

<p>Population: {w.population}</p>

<p>Casualties: {w.casualties}</p>

<p>Contamination: {w.contamination}</p>

<p>Morale: {w.morale}</p>

<p>Communications: {w.communications}</p>

<p>Mission Progress: {w.mission_progress}</p>

</div>

<div class="card">

<form action="/evaluate" method="post">

<h2>Commander Decision</h2>

<textarea name="decision"></textarea>

<br><br>

<button type="submit">
Evaluate
</button>

</form>

</div>

</body>

</html>
""")


@app.post("/new_scenario", response_class=HTMLResponse)
def new_scenario():

    global CURRENT_WORLD

    CURRENT_WORLD = engine.generate()

    return home()


@app.post("/evaluate", response_class=HTMLResponse)
def evaluate(decision: str = Form(...)):

    global CURRENT_WORLD

    result = decision_engine.evaluate(
        CURRENT_WORLD,
        decision
    )

    score = scoring_engine.calculate(
        CURRENT_WORLD
    )

    readiness = scoring_engine.readiness_level(
        score
    )

    aar = aar_engine.generate(
        CURRENT_WORLD,
        score,
        readiness
    )

    cbrn_feedback = [
        "Contamination level assessed.",
        "Additional reconnaissance recommended.",
        "Protective measures should continue."
    ]

    medical_feedback = [
        "Casualty management is ongoing.",
        "Medical evacuation remains a priority."
    ]

    intel_feedback = [
        "Threat source not fully confirmed.",
        "Information gaps remain."
    ]

    ops_feedback = [
        "Command and control maintained.",
        "Resources remain available."
    ]

    red_team_feedback = [
        "Contamination could spread further.",
        "Secondary incidents remain possible."
    ]

    return HTMLResponse(f"""
<!DOCTYPE html>
<html>

<body style="
background:#0f172a;
color:white;
font-family:Arial;
padding:40px;">

<h1>Assessment</h1>

<h2>Score: {score}</h2>

<h2>Readiness</h2>

<p>{readiness}</p>

<h2>CBRN Officer</h2>

<ul>
{''.join(f'<li>{x}</li>' for x in cbrn_feedback)}
</ul>

<h2>Medical Officer</h2>

<ul>
{''.join(f'<li>{x}</li>' for x in medical_feedback)}
</ul>

<h2>Intelligence Officer</h2>

<ul>
{''.join(f'<li>{x}</li>' for x in intel_feedback)}
</ul>

<h2>Operations Officer</h2>

<ul>
{''.join(f'<li>{x}</li>' for x in ops_feedback)}
</ul>

<h2>Red Team</h2>

<ul>
{''.join(f'<li>{x}</li>' for x in red_team_feedback)}
</ul>

<h2>After Action Review</h2>

<pre>{aar}</pre>

<br><br>

<a href="/" style="color:cyan;">
Back
</a>

</body>

</html>
""")