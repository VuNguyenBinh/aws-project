# 🔄 CI/CD Pipeline with GitLab, AWS, and SonarQube

A fully automated CI/CD pipeline designed to streamline software delivery, enforce code quality, and provide continuous feedback to developers through AWS cloud services and SonarQube analysis.

---

## 📌 Overview

This project implements an end-to-end CI/CD pipeline that integrates GitLab with AWS CodePipeline, CodeBuild, SonarScanner, SonarQube (EC2), API Gateway, Lambda, and Amazon SNS.

Whenever code is committed to the **main branch**, CodePipeline automatically executes the predefined stages.  
CodeBuild runs SonarScanner to analyze the codebase, and the results are submitted to SonarQube hosted on EC2.

After finishing analysis, SonarQube triggers a webhook that hits AWS API Gateway.  
The request is then forwarded to a Lambda function that processes the scan report and sends an SNS notification to the developer’s email.  

The pipeline forms a **closed-loop feedback system** that helps developers quickly detect:
- Security vulnerabilities  
- Code smells  
- Bugs  
- Violations of coding standards  

This greatly enhances software quality and accelerates development.

---

## 🛠 Tools Used

### **1. GitLab**
- Source code hosting and version control.
- Triggers pipeline when new commits are pushed to **main**.

### **2. AWS CodePipeline**
- Central automation engine.
- Orchestrates the entire CI/CD workflow.

### **3. AWS CodeBuild**
- Runs build tasks and executes **SonarScanner**.
- Sends scan results to SonarQube.

### **4. SonarQube on EC2**
- Receives code analysis from SonarScanner.
- Detects bugs, code smells, and vulnerabilities.
- Sends webhook notifications after each analysis.

### **5. AWS API Gateway**
- Receives webhook payload from SonarQube.
- Acts as the trigger point for Lambda.

### **6. AWS Lambda**
- Processes SonarQube scan results.
- Extracts critical errors and formats the final message.

### **7. Amazon SNS**
- Sends email alerts to developers.
- Notifies immediately when SonarQube detects issues.

### **8. Gmail**
- Endpoint for receiving SNS email alerts.

---

## 🔁 Pipeline Operation Procedure

### **1. Developer Pushes Code**
- Developer commits and pushes to the **main** branch on GitLab.

### **2. CodePipeline Auto-Trigger**
- CodePipeline detects the commit event.
- Begins executing the configured pipeline stages.

### **3. CodeBuild Executes Build + SonarScan**
- Source code is built.
- SonarScanner analyzes code quality.
- Results are sent to SonarQube (EC2).

### **4. SonarQube Processes Results**
- SonarQube evaluates issues:
  - Vulnerabilities  
  - Bugs  
  - Code smells  
  - Maintainability  
  - Security hotspots  
- Sends webhook notification when analysis is complete.

### **5. API Gateway Receives Webhook**
- SonarQube ⮕ API Gateway (POST request)
- API Gateway forwards data to Lambda.

### **6. Lambda Handles Scan Result**
- Parses JSON payload.
- Extracts important metrics.
- Generates a summary message.
- Publishes message to SNS topic.

### **7. SNS Sends Email to Developer**
- Developer receives immediate notification including:
  - Type of issues  
  - Severity  
  - File location (if applicable)  
  - Summary of analysis  

### **8. Developer Fixes Code**
- Developer updates code and pushes again.
- The pipeline repeats — forming a ***closed-loop continuous improvement cycle***.

---

## 🖼 CI/CD Pipeline Diagram
![CI/CD Pipeline Architecture](https://raw.githubusercontent.com/<user>/<repo>/main/cicd-diagram.png)

