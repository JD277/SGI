import pandas as pd
import google.generativeai as genai
from typing import List, Dict, Optional, Union
import os
from database.dbmanager import DbManager
class DataAnalyst:
    """
    Data analysis class using Google Generative AI for Firebase report data
    
    Args:
        api_key: Google Generative AI API key
    """
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        self.data = []  # Original data
        self.filtered_data = []  # Filtered data subset
        self.date_column = None  # To store date column name

    def load_data(self, data):
        """
        Load data from DbManager's getter methods
        
        Args:
            data: Data from DbManager (list of dicts or Firebase dict response)
            
        Example input formats:
            1. List of reports: [{"id": "123", "city": "..."}, ...]
            2. Firebase dict: {"report1": {...}, "report2": {...}}
        """
        if isinstance(data, dict):
            # Convert Firebase-style dict to list with IDs
            self.data = [
                {"id": k, **v} 
                for k, v in data.items()
            ]
        else:
            self.data = data
        self.filtered_data = self.data  # Reset filter

    def filter_data(
        self,
        date_column: str = "date_of_record",
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        **filters
    ):
        """
        Filter data by date range and/or field values
        
        Args:
            date_column: Name of date field (default: "date_of_record")
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
            filters: Field-value pairs to match (e.g., city="Barcelona")
        """
        self.date_column = date_column  # Store date column name
        
        # Convert date strings to timestamps
        start_ts = pd.to_datetime(start_date).timestamp() if start_date else None
        end_ts = pd.to_datetime(end_date).timestamp() if end_date else None

        # Filter logic
        self.filtered_data = [
            item for item in self.data
            if (start_ts is None or item.get(self.date_column, 0) >= start_ts)
            and (end_ts is None or item.get(self.date_column, 0) <= end_ts)
            and all(item.get(k) == v for k, v in filters.items())
        ]

    def analyze(self) -> Dict:
        """
        Generate AI-powered analysis of filtered data
        
        Returns:
            Dictionary containing analysis results and metadata
        """
        if not self.filtered_data:
            return {"error": "No data to analyze"}
        
        # Convert to DataFrame for analysis
        df = pd.DataFrame(self.filtered_data)
        sample_data = df.head().to_string()
        
        prompt = f"""
        Analyze this infrastructure report data:
        {sample_data}
        
        Provide:
        1. Summary statistics
        2. Pattern identification
        3. Anomaly suggestions
        4. Visualization recommendations
        5. Actionable insights
        6. Respond in Spanish
        """
        
        response = self.model.generate_content(prompt)
        
        # Time range analysis with validation
        time_range = None
        if self.date_column and self.date_column in df.columns:
            time_range = {
                "start": df[self.date_column].min(),
                "end": df[self.date_column].max()
            }

        return {
            "analysis": response.text,
            "record_count": len(df),
            "time_range": time_range
        }
    
# analyst = DataAnalyst(api_key="API_KEY")
# db_manager = DbManager("./modules/database/estructuras.json", "https://estructuras-9be66-default-rtdb.firebaseio.com/")
# data = db_manager.get_report_by_city("Barcelona")
# analyst.load_data(data)
# print(analyst.analyze())
