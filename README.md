# Pivo

This project is a practical, production-like example of deploying a machine learning model as a microservice using **FastAPI**, **Docker**, **Kubernetes**, **MinIO**, **Prometheus**, and **Grafana**.

It is designed as a beginner–friendly introduction to **MLOps** and **Kubernetes-based ML deployments**.

---

# 📌 Project Overview

The goal of this project is to create a small machine learning inference system that demonstrates how real companies deploy ML models:

1. A lightweight ML model is stored in **MinIO** (S3-compatible storage).
2. A **FastAPI** microservice downloads the model at startup.
3. The service loads the model (e.g., PyTorch / TensorFlow / scikit-learn).
4. The app exposes a `/predict` API endpoint.
5. The service is packaged as a **Docker** image.
6. The image is deployed to a **Kubernetes cluster**.
7. An **Ingress** exposes the service to the outside world.
8. **Prometheus** collects inference metrics.
9. **Grafana** visualizes latency, request count, and errors.
10. Horizontal Pod Autoscaler (**HPA**) scales the service based on CPU or custom metrics.

This stack reproduces the core of an **MLOps production environment**.

---

# 🧠 Architecture
```

               +------------------------+
               |     MinIO (S3 Storage) |
               |  model.pth, versions   |
               +-----------+------------+
                           |
                       (download)
                           |
               +-----------v------------+
               |   FastAPI Microservice |
               |   Loads & serves model |
               +-----------+------------+
                           |
                       (Dockerize)
                           |
               +-----------v------------+
               |   Kubernetes Cluster   |
               | Deploy → Scale → Serve |
               +-----------+------------+
                           |
          +----------------+----------------+
          |                                 |
      Prometheus                         Grafana
 (metrics scraping)               (monitoring UI)
```


---

# 🏗️ Components

### **1. Model Storage (MinIO)**
- Stores the ML model file (e.g., `model-v1.pth`)
- Allows versioning: `model-v2.pth`
- App downloads the model at startup using MinIO client SDK

---

### **2. FastAPI Microservice**
Runs inside Docker and Kubernetes.

Endpoints:
- `POST /predict` – run inference  
- `GET /health` – health check  

Responsibilities:
- Connect to MinIO  
- Download model file  
- Load model into memory  
- Perform prediction  
- Expose Prometheus metrics  

---

### **3. Docker**
The entire app (FastAPI + model loader + dependencies) is packaged into a Docker image.

This image is deployed to Kubernetes and updated automatically.

---

### **4. Kubernetes**
Key manifests:
- **Deployment** – runs pod(s) for inference  
- **Service** – cluster-internal networking  
- **Ingress** – expose `/predict` to the outside  
- **ConfigMap/Secrets** – MinIO credentials  
- **HPA** – autoscaling based on load  

---

### **5. Monitoring**
**Prometheus**
- Scrapes `/metrics` endpoint from the FastAPI app  
- Tracks latency, error rate, request count  

**Grafana**
- Dashboards for model performance and traffic  

---

# 📂 Project Structure (suggested)

```
├── app/
│ ├── main.py # FastAPI application
│ ├── model_loader.py # Downloads + loads model
│ ├── inference.py # Prediction logic
│ ├── requirements.txt
│ └── Dockerfile
│
├── k8s/ (Will be helm)
│ ├── deployment.yaml
│ ├── service.yaml
│ ├── ingress.yaml
│ ├── hpa.yaml
│ ├── configmap.yaml
│ └── secret.yaml
│
├── minio/
│ └── docker-compose.yaml # Local MinIO setup
│
├── README.md
└── LICENSE
```
