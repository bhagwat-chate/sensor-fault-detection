# Sensor-Fault-Detection

### Problem Statement
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class
indicates that the failure was caused by something else.

### Solution Proposed 
In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.
## Tech Stack Used
1. Python 
2. FastAPI 
3. Machine learning algorithms
4. Docker
5. MongoDB

## Infrastructure Required.

1. AWS S3
2. AWS EC2
3. AWS ECR
4. Git Actions
5. Terraform

## How to run?
Before we run the project, make sure that you are having MongoDB in your local system, with Compass since we are using MongoDB for data storage. You also need AWS account to access the service like S3, ECR and EC2 instances.

## Data Collections
![1 Data Collections](https://user-images.githubusercontent.com/57287835/216497337-0fabf7ef-f98e-4dd8-970d-aeb6068c4ecc.png)

## Project Archietecture
![2 Project Archietecture](https://user-images.githubusercontent.com/57287835/216497385-51377479-f27a-4817-ae59-105e8f165dbc.png)

## High Level Code Flow
![0_Sensor Training Pipeline](https://user-images.githubusercontent.com/57287835/217145452-034e077f-7b9f-40eb-b2c4-bc0a59c0e6f9.png)

## Deployment Archietecture
![3 Deployment Archietecture](https://user-images.githubusercontent.com/57287835/216497409-1cdadabd-136f-4399-a768-26ce92ce18f7.png)

### Step 1: Clone the repository
```bash
git clone https://github.com/bhagwat-chate/sensor-fault-detection.git
```

### Step 2- Create a conda environment after opening the repository
```bash
conda create -n sensor python=3.7.6 -y
```
```bash
conda activate sensor
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 - Export the environment variable
```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

export MONGODB_URL="mongodb+srv://<username>:<password>@cluster0.q06oiaw.mongodb.net/?retryWrites=true&w=majority"
```
### Step 5 - Run the application server
```bash
python app.py
```
### Step 6. Train application
```bash
http://localhost:8080/train
```

### Step 7. Prediction application
```bash
http://localhost:8080/predict
```
## Run locally

1. Check if the Dockerfile is available in the project directory

2. Build the Docker image
```
docker build --build-arg AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> --build-arg AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> --build-arg AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION> --build-arg MONGODB_URL=<MONGODB_URL> . 
```

3. Run the Docker image
```
docker run -d -p 8080:8080 <IMAGE_NAME>
```
To run the project  first execute the below commmand.
MONGO DB URL: 
```
MONGO_DB_URL=mongodb+srv://<username>:<password>@Project0.7eh1w4s.mongodb.net/admin?authSource=admin&replicaSet=atlas-okvkrd-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true
```
windows user

```
MONGO_DB_URL=mongodb+srv://<username>:<password>@Project0.7eh1w4s.mongodb.net/admin?authSource=admin&replicaSet=atlas-okvkrd-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true
```

Linux user

```
export MONGO_DB_URL=mongodb+srv://<username>:<password>@Project0.7eh1w4s.mongodb.net/admin?authSource=admin&replicaSet=atlas-okvkrd-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true
```

Run the project
```
python main.py
```
