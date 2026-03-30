import requests
import json
from typing import List, Dict
import os

class MedicalAgent:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.base_url = "https://clinicaltrials.gov/api/v2"
        
    def find_trials(self, patient_data: Dict) -> List[Dict]:
        """
        Find matching clinical trials for a patient
        """
        conditions = patient_data.get("conditions", [])
        all_trials = []
        
        for condition in conditions:
            trials = self._search_trials_by_condition(condition)
            all_trials.extend(trials)
        
        scored_trials = self._score_trials(all_trials, patient_data)
        
        return sorted(scored_trials, key=lambda x: x['score'], reverse=True)
    
    def _search_trials_by_condition(self, condition: str) -> List[Dict]:
        """
        Search ClinicalTrials.gov API for trials
        """
        url = f"{self.base_url}/studies"
        params = {
            "query.cond": condition,
            "fields": "NCTId,BriefTitle,OverallStatus,LocationCountry,EligibilityCriteria",
            "pageSize": 5,
            "format": "json"
        }
        
        try:
            response = requests.get(url, params=params)
            data = response.json()
            
            trials = []
            for study in data.get("studies", []):
                protocol = study.get("protocolSection", {})
                trials.append({
                    "nct_id": protocol.get("identificationModule", {}).get("nctId"),
                    "title": protocol.get("identificationModule", {}).get("briefTitle"),
                    "status": protocol.get("statusModule", {}).get("overallStatus"),
                    "location": "Germany",
                    "eligibility": "Check ClinicalTrials.gov for details"
                })
            return trials
        except Exception as e:
            print(f"Error searching trials: {e}")
            return []
    
    def _score_trials(self, trials: List[Dict], patient_data: Dict) -> List[Dict]:
        """
        Score each trial based on patient match
        """
        scored = []
        for trial in trials:
            score = 70
            
            if trial.get("status") == "RECRUITING":
                score += 10
            
            if trial.get("location") == patient_data.get("location"):
                score += 10
                
            scored.append({
                **trial,
                "score": score
            })
        return scored
