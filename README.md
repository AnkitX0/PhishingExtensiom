# Phishing URL Detection Browser Extension

An AI/ML-based cybersecurity project for detecting phishing websites from URL characteristics and providing understandable explanations to users through a browser extension.

The project combines classical machine learning, unsupervised attack-pattern analysis, character-level deep learning, FastAPI, and an LLM-based explanation layer into a single system.

---

## Overview

Phishing attacks use fraudulent websites and URLs to trick users into revealing sensitive information such as passwords, banking credentials, and personal data.

A major problem is that phishing websites are often designed to look legitimate. A user may recognize the brand, logo, and page layout without noticing that the actual URL is suspicious.

This project focuses on detecting phishing URLs before users interact with a potentially malicious website.

The system analyzes URL characteristics using machine learning models and is designed to provide a simple explanation of why a URL was considered suspicious.

The final application is intended to work as a Chrome browser extension connected to a FastAPI backend.

---

## Problem Statement

Build a browser extension and supporting web API that:

- Analyzes URLs in real time
- Classifies URLs as phishing or legitimate
- Identifies structural characteristics associated with phishing
- Explains the reason for a warning in plain language
- Helps non-technical users understand common phishing techniques

The project specifically targets a low false-positive rate because incorrectly blocking legitimate websites can reduce user trust in the security system.

The target specified for the project is:

**False Positive Rate < 0.5%**

---

## Project Objectives

The project is divided into four major modules.

### Module A — Classical Machine Learning

Train and compare:

- Random Forest
- XGBoost
- Support Vector Machine

using engineered URL features.

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- False Positive Rate
- Confusion Matrix

The objective is not simply to maximize accuracy. Since the system is intended for security use, false positives are especially important.

---

### Module B — Attack Pattern Analysis

This module focuses on understanding different structural patterns within phishing URLs.

Only phishing samples are considered for clustering.

The analysis uses unsupervised learning techniques to identify groups of URLs with similar characteristics.

The current approach includes:

- K-Means clustering
- DBSCAN
- PCA for visualization
- Cluster profiling

The goal is to investigate recurring patterns such as:

- IP-based URLs
- Domain spoofing
- Suspicious subdomains
- URL redirection
- Abnormal URL structures
- Webpage manipulation indicators

The cluster labels are interpreted from the feature profiles rather than being manually assigned before clustering.

---

### Module C — Character-Level Deep Learning

Traditional machine learning in Module A depends on engineered URL features.

Module C investigates whether a model can learn directly from raw URL strings.

The planned approach is a character-level:

- CNN
- or LSTM

The model receives the URL itself rather than the manually engineered feature vector.

The purpose is to compare:

**Feature-based machine learning**

against:

**End-to-end character-level learning**

This provides a second approach to the phishing detection problem and helps evaluate whether manual feature engineering provides a meaningful advantage.

---

### Module D — Explanation and Browser Interface

The final module converts the machine learning system into a user-facing application.

The planned architecture is:

```text
User visits website
        |
        v
Chrome Extension
        |
        v
FastAPI Backend
        |
        v
Feature Extraction
        |
        v
Machine Learning Model
        |
        v
Phishing / Legitimate
        |
        v
Explanation Layer
        |
        v
Chrome Extension Popup