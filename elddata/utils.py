from datetime import timedelta, datetime, timezone
from .models import EldData, HOSViolation

def detect_hos_violations(driverId):
    eld_records = EldData.objects.filter(driverId=driverId).order_by("-timestamp")
    #eld_records = EldData.objects.filter(driverId=driverId).un

    driving_time = timedelta()
    on_duty_time = timedelta()
    violations = []
    ll = list(eld_records)
    #print(datetime.now(), type(driving_time))

    #print(str(ll[0]).replace(" - ","").split("  "), len(list(eld_records)))
    for i, record in enumerate(eld_records):
        record_ = str(ll[i]).replace(" - ","").split("  ")
        print(record_)
        date_format = '%Y-%m-%d %H:%M:%S%z'
        date_str = record_[3]
        date_obj = datetime.strptime(record_[3], date_format)

        print(date_obj, record_[3], )
        if record_[2] == 'DRIVING':

                driving_time += (datetime.now(timezone.utc)- date_obj)
                print("1")


        elif record.status == 'On_DUTY':

                on_duty_time += (datetime.now(timezone.utc)- date_obj)

        else:
            violations.append(HOSViolation(
                driverId=driverId,
                violation_time=record.timestamp,
                violation_type='',
                description='Enter either On_DUTY or DRIVING'
            ))
        if driving_time > timedelta(hours=11):
            print("6")
            violations.append(HOSViolation(
                driverId=driverId,
                violation_time=record.timestamp,
                violation_type='11-hour driving limit',
                description='Exceeded 11-hour driving limit'
            ))

        # Check for 14-hour on-duty limit violation
        elif on_duty_time > timedelta(hours=14):
            print("7")
            violations.append(HOSViolation(
                driverId=driverId,
                violation_time=record.timestamp,
                violation_type='14-hour on-duty limit',
                description='Exceeded 14-hour on-duty limit'
            ))
        else:
            violations.append(HOSViolation(
                driverId=driverId,
                violation_time=record.timestamp,
                violation_type=' No violation',
                description='You are neither exceeding 14 hours duty or 11 hours driving time limit'
            ))

        HOSViolation.objects.bulk_create(violations)
        return violations

