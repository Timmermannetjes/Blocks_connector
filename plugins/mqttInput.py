import sys
sys.path.append(".")

import os
from helper_methods import helpers

SERVICE_NAME = "mqtt"

def invoke(services):
    if(SERVICE_NAME in services.keys()):
            print("Loading {name} plugin".format(name=SERVICE_NAME))
            return getConfigSection()

    host = os.environ.get('INFLUXDB_HOST') or "http://{service}:8086".format(service=SERVICE_NAME)
    organization = os.environ.get('INFLUXDB_ORG')
    database = os.environ.get('INFLUXDB_DB') or "balena"
    timeout = os.environ.get('INFLUXDB_TIMEOUT') or "1s"
def getConfigSection():
    username = os.environ.get('MQTT_USERNAME')
    password = os.environ.get('MQTT_PASSWORD')
    output = """


[[inputs.mqtt_consumer]]
servers = ["mqtt://mqtt:1883"]
username = "{username}"
password = "{password}"
topics = [
    "sensors/#",
    "balena/#"
]

data_format = "json"
"""

    stringFields = os.environ.get('MQTT_INPUT_STRINGS_FIELDS')
    if(stringFields is not None):
      stringFieldsSection = helpers.formatStringField(stringFields)
      output = output + stringFieldsSection

    return output
