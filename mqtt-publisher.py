import paho.mqtt.publish as publish
MQTT_SERVER = "localhost"
MQTT_PATH = "shipmentIn"
#MQTT_PATH = "wrong_shipment"
#publish.single(MQTT_PATH, "wrong In", hostname=MQTT_SERVER)
publish.single(MQTT_PATH, "Came In", hostname=MQTT_SERVER)

#