from torchvision import transforms
import torch
from torchvision.models import ResNet18_Weights
from PIL import Image
import io

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])


def prepare_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    return preprocess(image).unsqueeze(0) 




def postprocess_output(output_tensor):
    probabilities = torch.nn.functional.softmax(output_tensor[0], dim=0)
    top_prob, top_class_id = torch.max(probabilities, dim=0)

    class_name = ResNet18_Weights.DEFAULT.meta["categories"][top_class_id]

    return {
        "class_id": int(top_class_id),
        "class_name": class_name,
        "confidence": float(top_prob)
    }