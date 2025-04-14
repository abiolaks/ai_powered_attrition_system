# src/explain.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()


class AttritionExplainer:
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        self.api_url = (
            "https://api.deepseek.com/v1/chat/completions"  # Verify actual API endpoint
        )

    def explain_prediction(self, features: dict) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        prompt = f"""
        Explain this employee attrition prediction in HR-friendly terms.
        Focus on these key factors:
        - Salary: ${features.get('salary', 0):,.2f}
        - Engagement: {features.get('engagement_score', 0)}/5
        - Tenure: {features.get('tenure', 0)} years
        - Overtime: {features.get('overtime_hours', 0)} hours/month
        
        Provide 3 actionable recommendations to reduce attrition risk.
        """

        payload = {
            "model": "deepseek-chat",  # Confirm exact model name
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error generating explanation: {str(e)}"


# Example usage
if __name__ == "__main__":
    explainer = AttritionExplainer()

    # Mock employee data (replace with actual features)
    sample_employee = {
        "salary": 65000,
        "engagement_score": 2.3,
        "tenure": 1.5,
        "overtime_hours": 12,
    }

    explanation = explainer.explain_prediction(sample_employee)
    print("📊 Attrition Risk Explanation:")
    print(explanation)
