# 🩺 End-to-End Chest Cancer Classification Project

https://github.com/rdx7211/End-to-End-Chest-cancer-classification-project-/releases/download/v1.0/demo.mp4

> 🎥 *Watch the project demo above to see the full workflow in action!*

---

## 🚀 Overview

This project builds a complete **end-to-end machine learning pipeline** for **Chest Cancer Classification**, covering data ingestion, training, evaluation, experiment tracking, and CI/CD deployment using **AWS** and **GitHub Actions**.

It demonstrates:
- ML pipeline orchestration with **DVC**
- Experiment tracking with **MLflow**
- Model versioning and storage with **DagsHub**
- Containerization with **Docker**
- Continuous Integration & Deployment using **GitHub Actions**
- Cloud deployment on **AWS EC2 + ECR**

---

## ⚙️ Workflows

1. Update `config.yaml`  
2. Update `secrets.yaml` *(Optional)*  
3. Update `params.yaml`  
4. Define entities  
5. Configure pipeline manager inside `src/config`  
6. Build pipeline components  
7. Create pipeline orchestration  
8. Integrate with `main.py`  
9. Define `dvc.yaml` for pipeline stages  

---

## 🧠 MLflow Integration

**Documentation:** [MLflow Docs](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/rdx7211/End-to-End-Chest-cancer-classification-project-.mlflow \
MLFLOW_TRACKING_USERNAME=rdx7211 \
MLFLOW_TRACKING_PASSWORD=19af403ab4cc565a02c2cbe41ce92e9618b03138 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/rdx7211/End-to-End-Chest-cancer-classification-project-.mlflow

export MLFLOW_TRACKING_USERNAME=rdx7211

export MLFLOW_TRACKING_PASSWORD=19af403ab4cc565a02c2cbe41ce92e9618b03138

```



### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag


## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 268995414581.dkr.ecr.ap-south-1.amazonaws.com/chest_cancer

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app