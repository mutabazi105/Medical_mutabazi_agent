import os
import json
from dotenv import load_dotenv
from src.agent import MedicalAgent

load_dotenv()

def main():
    print("\n🏥 Medical_Mutabazi Agent - Clinical Trial Matcher")
    print("=" * 50)
    
    agent = MedicalAgent()
    
    # Sample patient data
    patient_data = {
        "age": 45,
        "gender": "female",
        "conditions": ["Diabetes", "Hypertension"],
        "medications": ["Metformin", "Lisinopril"],
        "location": "Germany"
    }
    
    print("\n📋 Patient Profile:")
    print(f"   Age: {patient_data['age']}")
    print(f"   Gender: {patient_data['gender']}")
    print(f"   Conditions: {', '.join(patient_data['conditions'])}")
    print(f"   Location: {patient_data['location']}")
    
    print("\n🔍 Searching for matching clinical trials...")
    results = agent.find_trials(patient_data)
    
    if results:
        print(f"\n✅ Found {len(results)} matching trials:\n")
        for i, trial in enumerate(results[:5], 1):
            print(f"{i}. {trial['title']}")
            print(f"   📊 Match Score: {trial['score']}%")
            print(f"   📍 Location: {trial['location']}")
            print(f"   🏷️ Status: {trial['status']}")
            print(f"   🔗 NCT ID: {trial['nct_id']}")
            print()
    else:
        print("\n⚠️ No matching trials found. Try different conditions.\n")

if __name__ == "__main__":
    main()
