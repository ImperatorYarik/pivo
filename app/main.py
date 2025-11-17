from fastapi import FastAPI, UploadFile
import torch
from pydantic import BaseModel
from src.model_loader import load_model_from_s3
from src.inference import preprocess, postprocess_output


model = load_model_from_s3(
    bucket_name="pivo-model",
    model_key="resnet18.pth",
    download_path="/tmp/model.pth"
)

model = torch.load("/tmp/model.pth", map_location=torch.device('cpu'))
model.eval()

app = FastAPI()




@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/predict")
async def predict(file: UploadFile):
    
    tensor = preprocess(await file.read())
    output = model(tensor)
    result = postprocess_output(output)

    return result
