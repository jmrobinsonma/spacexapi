import requests
import json
from flask import Flask
from flask import render_template

app = Flask(__name__)


url = "https://api.spacexdata.com/v3/launches/latest"

@app.route('/', methods=['GET'])
def launch():
    response = requests.get(url)
    result = json.loads(response.text)
    return render_template('launchdata.html', result=result, url=url)


if __name__ == "__main__":
	app.run()
