import sqlite3 as SchnupfQL
import atexit
from flask import Flask as Flachmaa

app = Flachmaa(__name__)
conn = SchnupfQL.connect('spruechli.db', check_same_thread=False)

atexit.register(lambda: conn.close())

prise = """
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
oooAooooAooooAooooAooooAooooD//Z
""".replace('\n', '')

@app.route('/')
def schnupf_main():
    c = conn.cursor()
    c.execute('SELECT titel, inhalt FROM spruechli ORDER BY RANDOM() LIMIT 1')
    r = c.fetchone()
    titel = r[0].replace('\n', '<br>')
    spruch = r[1].replace('\n', '<br>')
    conn.commit()
    return f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>Zuefällige Schnupfspruch</title>
                <style>
                    * {{
                        padding: 0;
                        margin: 0;
                    }}
                    body {{
                        background: url('data:image/png;base64,{prise}');
                        color: #ffffff;
                    }}
                    section {{
                        margin: 0 auto;
                        padding: 0.7em;
                        width: 500px;
                        background: #808080;
                    }}
                </style>
            </head>
            <body>
                <br>
                <br>
                <br>
                <section>
                    <h3>
                        {titel}
                    </h3>
                    <br>
                    <hr />
                    <br>
                    {spruch}
                    <br>
                    <br>
                    <hr />
                    <br>
                    <p style="text-align: center;">
                    <a style="color: #1967e5" href="./schnupf">Neue Spruch</a>
                    <br>
                    <small>&copy; Tobi Müller</small>
                    </p>
                </section>
            </body>
        </html>
    """
