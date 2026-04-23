# 🚀 AI Ops Kubernetes Agent  
### Intelligent Kubernetes Monitoring & Root Cause Analysis System

---

### TEAM : DUAL 404

## 📌 Project Overview

AI Ops Kubernetes Agent is an intelligent DevOps automation system designed to monitor Kubernetes clusters, detect failures, and automatically identify root causes using log analysis and system metrics.

This project reduces manual debugging time by enabling **AI-assisted troubleshooting**, **natural language queries**, and **real-time cluster insights** through an interactive dashboard.

The system simulates real-world AI-Ops workflows used in modern cloud infrastructure.

---

## 🎯 Problem Statement

Managing Kubernetes clusters manually is complex and time-consuming.  
When pods fail or consume excessive resources, developers often spend hours analyzing logs and diagnosing issues.

There is a need for:

- Automated failure detection  
- Intelligent root cause identification  
- Simplified debugging workflows  
- User-friendly cluster monitoring  

This project addresses these challenges using AI-powered reasoning and Kubernetes monitoring tools.

---

## 💡 Proposed Solution

The AI Ops Kubernetes Agent continuously monitors cluster health and identifies issues such as:

- Pod failures  
- CrashLoopBackOff errors  
- High memory usage  
- Application startup failures  

It supports **natural language queries**, allowing users to interact with the system like:

text
pod status  
why pods failing  
root cause  
memory usage  
logs pod crashloop-test

---

## Key Features

✅ Kubernetes Cluster Monitoring

✅ Automated Root Cause Analysis

✅ CrashLoopBackOff Detection

✅ Memory Usage Monitoring

✅ Natural Language Query Interface

✅ Log-Based Failure Detection

✅ Interactive CLI Assistant

✅ Streamlit Dashboard Visualization

✅ Real-Time Pod Health Insights

---

## 🏗️ System Architecture

This diagram shows the interaction between the AI agent, Kubernetes cluster, and monitoring tools.
<img width="1408" height="768" alt="image" src="https://github.com/user-attachments/assets/2b2bdf33-b769-42c0-bd0f-536602e528d2" />

---

## ⚙️ Technology Stack

Backend	: Python

Container Platform :	Docker

Orchestration :	Kubernetes

Local Cluster :	Minikube

Monitoring :	kubectl

UI Dashboard :	Streamlit

AI Logic :	Python Rule-Based Reasoning

Logging :	Custom Logger

Deployment :	Kubernetes YAML

---

## 📁 Project Structure

## 📁 Project Structure

```
H2H-DUAL-404-AI-Ops-Kubernetes-Agent/

├── agent/                         # Core AI Agent System  
│   ├── memory/                   # Conversation Memory  
│   │   └── memory_manager.py  
│   │
│   ├── prompts/                  # AI Prompt Templates  
│   │   ├── diagnosis_prompt.py  
│   │   └── recommendation_prompt.py  
│   │
│   ├── reasoning/                # Root Cause & Analysis Engines  
│   │   ├── root_cause_engine.py  
│   │   ├── explanation_engine.py  
│   │   ├── recommendation_engine.py  
│   │   ├── risk_engine.py  
│   │   ├── history_engine.py  
│   │   └── health_summary.py  
│   │
│   ├── tools/                    # Kubernetes Tools  
│   │   ├── kubectl_tool.py  
│   │   ├── log_tool.py  
│   │   └── metrics_tool.py  
│   │
│   ├── utils/                    # Logging Utilities  
│   │   └── tool_logger.py  
│   │
│   ├── agent_core.py             # Main AI Assistant Logic  
│   └── nl_query_engine.py        # Natural Language Query Engine  
│
├── kubernetes/                  # Kubernetes Configurations  
│   ├── deployments/  
│   │   ├── backend-deployment.yaml  
│   │   ├── frontend-deployment.yaml  
│   │   └── database-deployment.yaml  
│   │
│   ├── services/  
│   │   ├── backend-service.yaml  
│   │   ├── frontend-service.yaml  
│   │   └── database-service.yaml  
│   │
│   └── faults/                   # Fault Simulation Pods  
│       ├── crashloop.yaml  
│       ├── misconfigured.yaml  
│       ├── pending_pod.yaml  
│       └── resource_limit.yaml  
│
├── microservices/               # Application Microservices  
│   ├── backend/  
│   │   ├── app.py  
│   │   ├── Dockerfile  
│   │   └── requirements.txt  
│   │
│   ├── frontend/  
│   │   ├── app.py  
│   │   ├── Dockerfile  
│   │   └── requirements.txt  
│   │
│   └── database/  
│       └── init.sql  
│
├── ui/                          # User Interface  
│   └── dashboard.py  
│
├── data/  
│   └── history.json             # AI Memory History  
│
├── logs/  
│   └── agent_logs.txt  
│
├── tests/                       # Unit Tests  
│   ├── test_kubernetes.py  
│   ├── test_memory.py  
│   └── test_root_cause.py  
│
├── screenshots/                 # Project Screenshots  
│
├── main.py                      # Application Entry Point  
├── requirements.txt             # Global Dependencies  
├── README.md                    # Project Documentation  
├── project_brief.txt            # Hackathon Submission Brief  
├── architecture.png             # System Architecture Diagram  
├── tool_logs.txt  
└── .gitignore
```
---

## 🚀 How to Run the Project

Step 1 — Start Kubernetes
minikube start

Step 2 — Deploy Microservices
kubectl apply -f microservices/

Check pods:
kubectl get pods

Step 3 — Run AI Agent
python main.py

Step 4 — Use AI Commands
Try:
pod status
failing pods
why pods failing
root cause
memory usage
logs pod crashloop-test

Step 5 — Launch Dashboard
streamlit run ui/dashboard.py

Open:
http://localhost:8501

---

## Eample output

🚀 AI Ops Kubernetes Agent Starting...


🔍 Checking Cluster Health...

📊 Cluster Summary
-------------------
Total Pods   : 5
Running Pods : 3
Failing Pods : 2

🧠 Running Root Cause Analysis...

🚨 Detected Issues
-------------------
⚠️ Pod crash-demo failing — logs unavailable.
⚠️ Pod crashloop-test-7d5897df7-j4frc failing — logs unavailable.
⚠️ Pod database-deployment-54bdcbc4d8-k5jzh using high memory (435Mi)

🤖 AI Ops Assistant Ready!
Type 'exit' to quit.

Ask AI Ops > why pods failing

 
 🔎 Failure Reasons:

⚠️ crash-demo failing — application startup error detected
⚠️ crashloop-test-7d5897df7-j4frc failing — container crashing repeatedly (CrashLoopBackOff)
 

Ask AI Ops > root cause

 
 🚨 Root Cause Analysis:

⚠️ Pod crash-demo failing — logs unavailable.
⚠️ Pod crashloop-test-7d5897df7-j4frc failing — logs unavailable.
⚠️ Pod database-deployment-54bdcbc4d8-k5jzh using high memory (435Mi)
 

Ask AI Ops > exit
👋 Exiting AI Ops Assistant...


---


## Screenshots 

### Kubernetes Pods Running
<img width="1110" height="158" alt="image" src="https://github.com/user-attachments/assets/b8a76403-ba73-4d8c-a39f-7c72607ba340" />


### Cluster Health Output
<img width="877" height="555" alt="image" src="https://github.com/user-attachments/assets/b53b5bc4-be85-4a18-afb5-bbfdb7092af4" />


### Root Cause Detection
<img width="870" height="190" alt="image" src="https://github.com/user-attachments/assets/448919ee-8d62-43be-b53d-081e48da759f" />


### AI Query Response
<img width="1176" height="267" alt="image" src="https://github.com/user-attachments/assets/8ade05cf-1e30-4ae0-86b2-877dd41f75da" />


### Streamlit Dashboard
<img width="1883" height="838" alt="image" src="https://github.com/user-attachments/assets/87bc1777-52d7-4dd5-8d1f-f94a09d17297" />


----

## 🔍 Real-World Applications

This system can be used in:
* Cloud Infrastructure Monitoring
* DevOps Automation
* Kubernetes Troubleshooting
* Production System Diagnostics
* AI-Ops Platforms

---

## 🎯 Future Enhancements

* Integration with Prometheus
* AI-based anomaly prediction
* Slack/Email alert notifications
* Auto-healing Kubernetes services
* Cloud deployment support

---

## 👩‍💻 Team Information

Team Name: DUAL 404

Project Name: AI Ops Kubernetes Agent

Team Members: 
* Nethravathi D
* Neethu Chauhan

---

## 🏆 Conclusion

AI Ops Kubernetes Agent demonstrates how intelligent automation can simplify complex DevOps workflows.

By combining Kubernetes monitoring with AI-powered reasoning, the system significantly reduces debugging time and improves system reliability.

This project showcases a scalable approach to modern AI-driven infrastructure management.
