from flask import Flask
import json

app = Flask(__name__)


# End point of API
@app.get("/")
def home():
    return "Hello, from Flask."

# @app.post("/")
# @app.put("/")
# @app.patch("/")
# @app.delete("/")

@app.get("/test")
def test():
    return "This is another endpoint."

# This is a JSON implementation
@app.get("/api/about")
def about():
    name = {"name": "Derrick"}
    return json.dumps(name)

app.run(debug=True)