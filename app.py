from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():

    return """
    <!DOCTYPE html>

    <html>

    <head>

        <title>CBRN Tactical Trainer</title>

        <style>

            body{
                background:#0f172a;
                color:white;
                font-family:Arial;
                margin:40px;
            }

            .card{

                background:#1e293b;

                padding:20px;

                border-radius:12px;

                margin-bottom:20px;
            }

            button{

                background:#2563eb;

                color:white;

                border:none;

                padding:12px;

                border-radius:10px;
            }

        </style>

    </head>

    <body>

        <h1>CBRN Tactical Trainer</h1>

        <div class="card">

            <h2>Scenario</h2>

            <p>Threat: Nuclear Fallout</p>

            <p>Wind: NW 15 km/h</p>

            <p>Casualties: 30</p>

            <p>Civilians: 6000</p>

        </div>

        <div class="card">

            <h2>Map</h2>

            <pre>

🟥 HOT ZONE

██████

🟨 WARM ZONE

██████████

🟩 SAFE ZONE

████████████████

            </pre>

        </div>

        <div class="card">

            <h2>Commander Decision</h2>

            <textarea
            style="width:100%;height:150px;">
            </textarea>

            <br><br>

            <button>
            Execute
            </button>

        </div>

    </body>

    </html>
    """
