"""generate data the passengers"""
import json
import copy
from typing import List

document_infant = 9050

infant = {
        "document":"9050",
        "dateOfBirth": "2022-05-19",
        "gender": "MALE",
        "first": "infantrtestB",
        "last": "infanttestB"
}
passenger_base = {
        "name": "test0",
        "last": "last0",
        "type_document": "CC",
        "person_type":"ADT",
        "document_number": 0,
        "dateOfBirth": "1995-05-18",
        "gender": "F",
        "country": "COL",
        "expiration_date": None,
        "email": "test.test@test.com",
        "nacionality": "COL",
        "phone": "234523",
        "seat": None,
        "ssrs": None,
        "child": None,
        "infant": None
    }
data = {
    "emails":["jalvinrene@gmail.com"],
    "passengers": []
}
def get_infant(document, first, last):
    infant_copy = copy.copy(infant)
    infant_copy["document"] = document
    infant_copy["first"] = first
    infant_copy["document"] = last
    return infant_copy

    
def generate_data(num_passengers: int, infan_posicion: List[int]):
    """Genear data the passenger and infant

    Args:
        num_passengers (int): Number passenger to generate
        infan (int): Number passenger infant to generate
    """
    document_infant = 9050
    data_temp = []
    i =  0
    document = 900
    while i <= num_passengers:
        name = "test" + str(i)
        last_name = "test" + str(i)
        passenger = copy.copy(passenger_base)
        passenger["document_number"] = document
        passenger["name"] = name
        passenger["last"] = last_name
        if i in infan_posicion:
            document_infant +=1
            passenger["infant"] = get_infant(str(document_infant), "infante" + str(i),"infante"+str(i))

        document += 1
        data_temp.append(passenger)
        i +=1

    data["passengers"] = data_temp
    with open("data.json", "w") as fp:
        json.dump(data, fp)
        

generate_data(188,[1,20,30])
