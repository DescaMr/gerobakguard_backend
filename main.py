from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mqtt_handler import publish_capture_command  # pastikan fungsi ini ada

app = FastAPI()

# Model permintaan (request) untuk endpoint /capture
class CaptureRequest(BaseModel):
    device_id: str  # nama topik/device_id, misal "esp32cam"

@app.post("/capture")
async def capture_photo(req: CaptureRequest):
    try:
        publish_capture_command(device_id=req.device_id)
        return {"message": f"📸 Perintah capture dikirim ke {req.device_id}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

