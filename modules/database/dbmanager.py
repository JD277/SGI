import firebase_admin
from firebase_admin import credentials, db
import time
class DbManager:
    def __init__(self, credential="modules/database/estructuras.json'", database_url="https://estructuras-9be66-default-rtdb.firebaseio.com/"):
        """
        Initialize Firebase connection

        Args:
            credential: Path to Firebase service account key
            database_url: Firebase Realtime Database URL
        """
        if not firebase_admin._apps:
            cred = credentials.Certificate(credential)
            firebase_admin.initialize_app(
                cred,
                {'databaseURL': database_url}
            )
    def unix_to_string_time(self,ts):
        try:
            return time.strftime(
                "%Y-%m-%d %H:%M:%S",
                time.gmtime(ts)  # UTC
            )
        except Exception as e:
            return f"Error: {e}"

    def write_record(self, data):
        """
        Write report data to the database

        Args:
            data: Dictionary containing report information:
                {
                    "city": str,
                    "date_of_record": str,
                    "date_of_failure": str,
                    "description": str,
                    "service": str,
                    "street": str,
                    "priority": str
                }
        """
        ref = db.reference('reports/')
        data['status'] = "nuevo"
        ref.push(data)

    def read_record(self):
        """
        Read all reports from the database

        Returns:
            Dictionary containing all reports with their unique IDs as keys
        """
        ref = db.reference("/reports")
        return ref.get()
    
    def update_record(self, data, id):
        """
        Update an existing report

        Args:
            data: Dictionary containing updated fields
            id: Unique ID of the report to update
        """
        ref = db.reference(f'reports/{id}')
        ref.update(data)
    
    def delete_record(self, id):
        """
        Delete a report by ID

        Args:
            id: Unique ID of the report to delete
        """
        ref = db.reference(f"reports/{id}")
        ref.delete()
    
    def get_report_by_id(self, id):
        """
        Get a report by its unique ID

        Args:
            id: Unique ID of the report

        Returns:
            Dictionary containing the report data, or None if not found
        """
        ref = db.reference(f"reports/{id}")
        result = ref.get()
        return result
    
    def get_report_by_city(self, city):
        """
        Get reports filtered by city

        Args:
            city: City name to filter by

        Returns:
            List of reports matching the city
        """
        ref = db.reference(f"reports/")
        reports = ref.get() or {}
        return [v for v in reports.values() if v.get('city') == city]
    
    def get_report_by_service(self, service):
        """
        Get reports filtered by service type

        Args:
            service: Service type to filter by

        Returns:
            List of reports matching the service
        """
        ref = db.reference(f"reports/")
        reports = ref.get() or {}
        if reports == {}:
            return []
        reports_list = [v for v in reports.values() if v.get('service') == service]

        return reports_list
    
    def get_report_by_priority(self, priority):
        """
        Get reports filtered by priority level

        Args:
            priority: Priority level to filter by

        Returns:
            List of reports matching the priority
        """
        ref = db.reference(f"reports/")
        reports = ref.get() or {}
        return [v for v in reports.values() if v.get('priority') == priority]
    
    def get_report_by_date(self, date):
        """
        Get reports filtered by record date

        Args:
            date: Record date to filter by (YYYY-MM-DD format)

        Returns:
            List of reports matching the date
        """
        ref = db.reference(f"reports/")
        reports = ref.get() or {}
        return [v for v in reports.values() if v.get('date_of_record') == date]
    
    def get_report_by_date_of_failure(self, date):
        """
        Get reports filtered by failure date

        Args:
            date: Failure date to filter by (YYYY-MM-DD format)

        Returns:
            List of reports matching the failure date
        """
        ref = db.reference(f"reports/")
        reports = ref.get() or {}
        return [v for v in reports.values() if v.get('date_of_failure') == date]
    
    def get_report_by_street(self, street):
        """
        Get reports filtered by street name

        Args:
            street: Street name to filter by

        Returns:
            List of reports matching the street
        """
        ref = db.reference(f"reports/")
        reports = ref.get() or {}
        return [v for v in reports.values() if v.get('street') == street]
    
    def search_records(self, **kwargs):
        """
        Search using Firebase native queries (efficient for large datasets)
        
        Args:
            **kwargs: Supported filters:
                city: Exact match (case-insensitive)
                service: Exact match (case-insensitive)
                priority: Exact match (case-sensitive)
                date_of_record: Exact match (YYYY-MM-DD)
        
        Returns:
            List of matching reports with IDs
        """
        base_ref = db.reference('reports')
        query = base_ref
        
        # Apply filters
        if 'city' in kwargs:
            city = kwargs['city'].lower()
            query = query.order_by_child('city_lower').equal_to(city)
        
        if 'service' in kwargs:
            service = kwargs['service'].lower()
            query = query.order_by_child('service_lower').equal_to(service)
        
        if 'priority' in kwargs:
            query = query.order_by_child('priority').equal_to(kwargs['priority'])
        
        if 'date_of_record' in kwargs:
            query = query.order_by_child('date_of_record').equal_to(kwargs['date_of_record'])
        
        # Execute query
        results = query.get() or {}
        
        # Add IDs to results
        return [
            {**value, 'id': key} 
            for key, value in results.items()
        ]
    def mark_report_completed(self, report_id: str):
        """
        Mark a report as completed with a completion timestamp

        Args:
            report_id: Unique ID of the report to mark as completed

        Returns:
            True if successful, False otherwise
        """
        try:
            report_ref = self.ref.child(report_id)
            report_ref.update({
                'status': 'completed',
                'completed_at': db.ServerValue.TIMESTAMP  # Firebase server timestamp
            })
            return True
        except Exception as e:
            print(f"Error marking report {report_id} as completed: {e}")
            return False
        
    def get_completed_reports(self):
        """
        Get all completed reports

        Returns:
            List of completed reports with their IDs
        """
        try:
            query = self.ref.order_by_child('status').equal_to('completed')
            results = query.get() or {}
            return [
                {**report_data, 'id': report_id}
                for report_id, report_data in results.items()
            ]
        except Exception as e:
            print(f"Error retrieving completed reports: {e}")
            return []
        
