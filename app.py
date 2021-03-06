from flask import Flask, jsonify
from flask_simple_geoip import SimpleGeoIP

import os

app = Flask(__name__)

# The API key is obtained from the GEOIPIFY_API_KEY environment variable.
# Alternatively it can be set as follows:
# app.config.update(GEOIPIFY_API_KEY='YOUR_API_KEY')

# Initialize the extension
simple_geoip = SimpleGeoIP(app)


@app.route('/')
def test():
    # Retrieve geoip data for the given requester
    geoip_data = simple_geoip.get_geoip_data()

    return jsonify(data=geoip_data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))