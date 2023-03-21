import requests
from database import *


def trigger():
    print("start")
    for para in con_data():
        res = requests.post(url=URL, json=para)
        print("Status:" + str(res.status_code), "\tPatientId:" + str(para[0]["patientId"]), "\tVisitId:" + str(para[0]["visitId"]), "\tResponse:" + res.text)

    print("end")

