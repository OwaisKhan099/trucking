from django.test import TestCase
import requests
# Create your tests here.
from datetime import timedelta, datetime, timezone
from .models import EldData, HOSViolation
class ELDDataModelTest(TestCase):
    def setUp(self):
        # # self.driverIds = EldData.objects.values_list('driverId', flat=True)
        # self.driverIds = EldData.objects.values_list('driverId', flat=True)
        #
        # self.check = "jjj"
        # print(self.driverIds)
        self.data = requests.get("http://127.0.0.1:8000/elddata/")

    def test_detect_hos_violations(self):
        # print(self.data.json())
        driving_time = timedelta()
        on_duty_time = timedelta()
        eld_records = self.data.json()
        #print(str(ll[0]).replace(" - ","").split("  "), len(list(eld_records)))
        for i, record in enumerate(eld_records):
            driving_time = timedelta()
            on_duty_time = timedelta()
            print(record)
            #record_ = str(ll[i]).replace(" - ","").split("  ")
            timestamp = record["timestamp"].replace("T"," ")
            date_format = '%Y-%m-%d %H:%M:%S%z'
            date_str = record["timestamp"]
            date_obj = datetime.strptime(timestamp, date_format)

            if record["status"] == 'DRIVING':

                    driving_time += (datetime.now(timezone.utc)- date_obj)



            elif record["status"] == 'On_DUTY':

                    on_duty_time += (datetime.now(timezone.utc)- date_obj)

            elif  record["status"] == 'Off_DUTY':

                print({"violation_type":'No Violation', "description":'Currently driver is off line. So, there is not any violation possible right now'})
            else:
                print({"violation_type":'', "description":'Enter either On_DUTY or DRIVING'})

            if driving_time > timedelta(hours=11):
                print({"violation_type": '11-hour driving limit', "description": 'Exceeded 11-hour driving limit'})

            #
            # Check for 14-hour on-duty limit violation
            elif on_duty_time > timedelta(hours=14):
                print("7")
                print({"violation_type": '14-hour on-duty limit', "description": 'Exceeded 14-hour on-duty limit'})


            elif driving_time or on_duty_time:
                print({"violation_type": 'No violation', "description": 'You are neither exceeding 14 hours duty or 11 hours driving time limit'})

            #
            # HOSViolation.objects.bulk_create(violations)
            # return violations
            #
