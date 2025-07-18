import paho.mqtt.client as mqtt
import ssl
import os
from dotenv import load_dotenv

load_dotenv()

MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", "8883"))
MQTT_USERNAME = os.getenv("MQTT_USERNAME", "esp32cam")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD", "password")
TOPIC_PREFIX = os.getenv("TOPIC_PREFIX", "esp32cam")

client = mqtt.Client()

def connect_mqtt():
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    client.tls_set(cert_reqs=ssl.CERT_NONE)
    client.tls_insecure_set(True)
    client.connect(MQTT_BROKER, MQTT_PORT)
    client.loop_start()

connect_mqtt()

def publish_capture_command(device_id: str):
    topic = f"{device_id}/capture"  # Gunakan device_id
    message = "capture"
    
    if not client.is_connected():
        print("🔁 MQTT reconnecting...")
        connect_mqtt()

    result = client.publish(topic, message)
    status = result[0]
    if status == 0:
        print(f"📤 Perintah capture dikirim ke {topic}")
    else:
        raise Exception("❌ Gagal publish ke MQTT")
