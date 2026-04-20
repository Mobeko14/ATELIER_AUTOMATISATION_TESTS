from flask import Flask, render_template
import requests
import time

app = Flask(__name__)

def run_tests():
    url = "https://api.agify.io?name=edouard"
    
    results = []

    # Test 1 : status
    r = requests.get(url)
    results.append({
        "test": "Status Code",
        "result": "OK" if r.status_code == 200 else "FAIL"
    })

    # Test 2 : contenu JSON
    data = r.json()
    results.append({
        "test": "JSON contains age",
        "result": "OK" if "age" in data else "FAIL"
    })

    # Test 3 : temps de réponse
    start = time.time()
    requests.get(url)
    duration = time.time() - start

    results.append({
        "test": "Response time < 1s",
        "result": "OK" if duration < 1 else "FAIL"
    })

    return results


@app.route("/")
def home():
    results = run_tests()
    return render_template("index.html", results=results)
