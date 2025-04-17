# ML Deployment Project (Exercise 1-4)

This repository contains materials for the MLOps Course(CPE393) **Exercise 1-4** which focusing on deploying machine learning models as APIs. However, the Exercise 5 https://github.com/KwinyarutP/house_prediction-MLOps5

## Overview

This project demonstrates how to create, package and deploy machine learning models as REST APIs. It covers the entire MLOps workflow from model training to deployment and testing.

## 📁 Repository Structure
- `train.py`: Script to train the model and export it as `model.pkl`.
- `app/`: Contains the FastAPI application to serve the model.
- `Dockerfile`: Instructions for containerizing the app.
- `requirements.txt`: Python dependencies.
- `pic_ans/`: Contains screenshots showing the API request running successfully in Exercise 1-4.

## API Screenshots

The `pic_ans/` folder contains screenshots demonstrating successful API requests and responses in Exercise 1-4. These images provide visual verification that the API is functioning correctly with various test cases.

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/KwinyarutP/mldeployment-cpe393-MLOps1-4.git
   cd mldeployment-cpe393-MLOps1-4
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Training the Model

To train the model and generate the `model.pkl` file:

```
python train.py
```

## Running the API

### With Docker

Build the Docker image:
```
docker build -t ml-deployment .
```

Run the container:
```
docker run -p 9000:9000 ml-deployment
```

## API Usage

Once the API is running, you can access the interactive Swagger UI documentation at `http://localhost:9000/predict`.
