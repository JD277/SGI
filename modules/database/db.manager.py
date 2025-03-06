import firebase_admin
from firebase_admin import credentials,db

class DbManager():
    def __init__(self,credential,database_url):
        # Initialize Firebase with your account credentials
        cred = credentials.Certificate(credential)
        firebase_admin.initialize_app(cred,{
            'databaseURL': database_url
        })
    
    def write_record(self,data):
        """
        Write data of the report to the db
        Args:
            data: {
                    "city": city,
                    "date_of_record": date,
                    "date_of_failure": date,
                    "description": description,
                    "service": service,
                    "street": street,
                    "priority": priority,

                }
        """
        ref = db.reference('reports/')
        ref.push(data)

    def read_record(self):
        """
            Read all the rports from the database

            Return:
                a JSON object with all the records of the database
        """
        ref = db.reference("/reports")
        return ref.get()
    
    def update_recod(self,data,id):
        """
            Update one record by the given ID

            Args: 
                data: the data that will be updated
                id: the id of the record that will be updated
        """
        ref = db.reference(f'reports/{id}')
        ref.update(data)
    
    def delete_record(self,id):
        """
            Delete one record by the given ID

            Args:
                id: The id from the report that will be removed
        """
        ref = db.reference(f"reports/{id}")
        ref.delete()
     
    def get_report_by_id(self, id):
        """
            Get one report by ID

            Args:
                id: the id of the report that will be returned

            Return:
                a JSON object with the report data
        """
        ref = db.reference(f"reports/{id}")
        return ref.get()
    
    def get_report_by_city(self, city):
        """
            Get one report by city

            Args:
                city: the city of the report that will be returned

            Return:
                a JSON object with the report data
        """
        ref = db.reference(f"reports/")
        reports = ref.get()
        reports_by_city = []
        for report in reports:
            if reports[report]['city'] == city:
                reports_by_city.append(reports[report])
        return reports_by_city
    
    def get_report_by_type(self, type):
        """
            Get one report by type

            Args:
                type: the type of the report that will be returned

            Return:
                a JSON object with the report data
        """
        ref = db.reference(f"reports/")
        reports = ref.get()
        reports_by_type = []
        for report in reports:
            if reports[report]['type'] == type:
                reports_by_type.append(reports[report])
        return reports_by_type
    
    def get_report_by_priority(self, priority):
        """
            Get one report by priority

            Args:
                priority: the priority of the report that will be returned

            Return:
                a JSON object with the report data
        """
        ref = db.reference(f"reports/")
        reports = ref.get()
        reports_by_priority = []
        for report in reports:
            if reports[report]['priority'] == priority:
                reports_by_priority.append(reports[report])
        return reports_by_priority
    

    def get_report_by_date(self, date):
        """
            Get one report by date

            Args:
                date: the date of the report that will be returned

            Return:
                a JSON object with the report data
        """
        ref = db.reference(f"reports/")
        reports = ref.get()
        reports_by_date = []
        for report in reports:
            if reports[report]['date_of_record'] == date:
                reports_by_date.append(reports[report])
        return reports_by_date
    
    def get_report_by_date_of_failure(self, date):
        """
            Get one report by date of failure

            Args:
                date: the date of failure of the report that will be returned

            Return:
                a JSON object with the report data
        """
        ref = db.reference(f"reports/")
        reports = ref.get()
        reports_by_date_of_failure = []
        for report in reports:
            if reports[report]['date_of_failure'] == date:
                reports_by_date_of_failure.append(reports[report])
        return reports_by_date_of_failure
    
    def get_report_by_street(self, street):
        """
            Get one report by street

            Args:
                street: the street of the report that will be returned

            Return:
                a JSON object with the report data
        """
        ref = db.reference(f"reports/")
        reports = ref.get()
        reports_by_street = []
        for report in reports:
            if reports[report]['street'] == street:
                reports_by_street.append(reports[report])
        return reports_by_street
    
    def get_report_by_service(self, service):
        """
            Get one report by service

            Args:
                service: the service of the report that will be returned

            Return:
                a JSON object with the report data
        """
        ref = db.reference(f"reports/")
        reports = ref.get()
        reports_by_service = []
        for report in reports:
            if reports[report]['service'] == service:
                reports_by_service.append(reports[report])
        return reports_by_service
    
    # Get report by the given data