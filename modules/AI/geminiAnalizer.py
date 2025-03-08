import pandas as pd
import google.generativeai as genai
from typing import  Dict, Optional
class DataAnalyst:
    """
    Data analysis class using Google Generative AI for Firebase report data
    
    Args:
        api_key: Google Generative AI API key
    """
    def __init__(self, api_key: str = "AIzaSyCTHoF8MX96j6309uMcNTS1ApRcMgf8mzE"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        self.data = []  # Original data
        self.filtered_data = []  # Filtered data subset
        self.date_column = None  # To store date column name

    def analyze(self,df,prompt) -> Dict:
        """
        Generate AI-powered analysis of filtered data
        
        Returns:
            Dictionary containing analysis results and metadata
        """ 
        
        # Convert to DataFrame for analysis
        sample_data = df.head().to_string()
        
        
        response = self.model.generate_content([sample_data,prompt, "Siempre responde en español"])
        
        return response.text
    
# analyst = DataAnalyst(api_key="API_KEY")
# db_manager = DbManager("./modules/database/estructuras.json", "https://estructuras-9be66-default-rtdb.firebaseio.com/")
# data = db_manager.get_report_by_city("Barcelona")
# analyst.load_data(data)
# print(analyst.analyze())
