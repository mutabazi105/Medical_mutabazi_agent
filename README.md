# 🏥 Medical_Mutabazi Agent

> **A2A Healthcare Agent for Clinical Trial Matching**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Overview

Medical_Mutabazi Agent is an intelligent healthcare agent that helps clinicians and researchers identify suitable clinical trials for patients. By analyzing patient conditions, demographics, and location, the agent returns ranked trial matches from ClinicalTrials.gov.

## 🎯 Problem Statement

Clinicians spend hours manually searching for appropriate clinical trials across multiple databases. Patients miss opportunities for cutting-edge treatments because matching is inefficient. **This agent automates the process.**

## 💡 Solution

- **Patient Analysis**: Parses patient medical data (age, conditions, location)
- **Trial Matching**: Searches ClinicalTrials.gov API for relevant trials
- **Smart Scoring**: Ranks trials by match score (recruiting status + location)
- **A2A Architecture**: Designed to work with other healthcare agents

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python 3.10+ |
| API | ClinicalTrials.gov API v2 |
| Libraries | requests, python-dotenv |
| Tools | Git, GitHub |

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Internet connection

### Installation

```bash
# Clone the repository
git clone https://github.com/mutabazi105/Medical_mutabazi_agent.git
cd Medical_mutabazi_agent

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
