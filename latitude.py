import requests
import streamlit as st

class AI:
    def __init__(self):
        self.api_url = "https://gateway.latitude.so/api/v2/projects/11398/versions/live/documents/run"
        self.api_key = st.secrets['LATITUDE']
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

    def get_audience_understand(self, transcript, customer):
        data = {
            "path": "AudienceUnderstandPrompt",
            "stream": False,
            "parameters": {
                "InterviewTranscript": transcript,
                "CustomerName": customer
            }
        }
        response = requests.post(self.api_url, headers=self.headers, json=data)
        return response.json().get("response").get("text")
    
    def get_audience_believe(self, transcript, products, customer):
        data = {
            "path": "BelieveUsPrompt",
            "stream": False,
            "parameters": {
                "InterviewTranscript": transcript,
                "products": products,
                "CustomerName": customer
            }
        }
        response = requests.post(self.api_url, headers=self.headers, json=data)
        return response.json().get("response").get("text")

    def get_products(self, transcript, products, customer):
        data = {
            "path": "ProductsPrompt",
            "stream": False,
            "parameters": {
                "InterviewTranscript": transcript,
                "products": products,
                "CustomerName": customer
            }
        }
        response = requests.post(self.api_url, headers=self.headers, json=data)
        return response.json().get("response").get("text")
    