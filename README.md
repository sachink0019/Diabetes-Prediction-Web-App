# Diabetes Prediction Web App

A machine learning web application that predicts diabetes risk based on user-provided health parameters. The project covers the complete pipeline — from model training to a containerized, cloud-deployed application.

**Live Demo:** http://13.53.174.221:8501

## Architecture

```
User → Streamlit Frontend → FastAPI REST API → ML Model → Prediction
```

The frontend and backend run as separate Docker containers, both hosted on a single AWS EC2 instance.

## Tech Stack

**Machine Learning**
- Python
- Pandas, NumPy
- Scikit-learn
- Support Vector Machine (SVM)
- Feature Scaling, Train/Test Split

**Backend**
- FastAPI
- Uvicorn
- REST API

**Frontend**
- Streamlit

**Deployment**
- Docker
- Docker Hub
- AWS EC2
- AWS Security Groups

## How It Works

1. User enters health parameters (glucose level, BMI, age, blood pressure, etc.) in the Streamlit frontend.
2. Frontend sends the data as a POST request to the FastAPI `/predict` endpoint.
3. The API passes the input to the trained ML model.
4. The model returns a prediction, which is sent back and displayed to the user.

## Docker Setup

The application is split into two containers:

| Service   | Technology | Port |
|-----------|-----------|------|
| Frontend  | Streamlit | 8501 |
| Backend   | FastAPI   | 8000 |

### Run locally with Docker

```bash
# Build images
docker build -t diabetes-frontend ./frontend
docker build -t diabetes-backend ./backend

# Run containers
docker run -d -p 8501:8501 diabetes-frontend
docker run -d -p 8000:8000 diabetes-backend
```

Or, if using Docker Compose:

```bash
docker-compose up --build
```

## AWS Deployment

The app is deployed on an AWS EC2 instance with:
- Docker containers running both frontend and backend
- Security Groups configured to allow public access on ports 8000 and 8501
- Port mapping for external access to the app

## Project Structure

```
.
├── backend/
│   ├── app.py
│   ├── model.pkl
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## What I Learned

- End-to-end ML model development
- Building REST APIs with FastAPI
- Connecting frontend and backend services
- Dockerizing multi-service applications
- Deploying applications on AWS EC2
- AWS networking and Security Groups
- Debugging real-world deployment and connectivity issues

## Future Improvements

- Add HTTPS using a domain and SSL certificate
- Use environment variables for configuration instead of hardcoded values
- Add input validation and error handling on the API
- Move deployment to AWS ECS/Elastic Beanstalk for better scalability
- Add CI/CD pipeline for automated builds and deployment

## Author

Feel free to connect or reach out if you have suggestions or feedback!
