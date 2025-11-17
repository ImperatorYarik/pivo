from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictRequest(BaseModel):
    data: str


class PredictResponse(BaseModel):
    prediction: str


@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/predict")
async def predict(request: PredictRequest):
    # Add your prediction logic here
    prediction_result = f"Processed: {request.data}"
    return PredictResponse(prediction=prediction_result)