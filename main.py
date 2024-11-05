from fastapi import FastAPI
from app.api.v1.qr import router as qr_router

app = FastAPI(title="QR Code Generator API")

# Include the router
app.include_router(qr_router, prefix="/api/v1/qr", tags=["QR"])

# Run the app with: uvicorn main:app --reload
