from pymongo import MongoClient
from enum import Enum, auto, unique
import datetime
import json


client = MongoClient("mongodb://localhost:27017/")  # your connection string
db = client["OfficeForms"]
employee = db["employee"]

###########################################################################################################
# Employees table
###########################################################################################################

"""
Validation for Employee

{
  $jsonSchema: {
    required: [
      'empName',
      'empPassword'
    ],
    properties: {
      empName: {
        bsonType: 'string',
        description: 'The Name must be string and Name Mandatory'
      },
      empPassword: {
        bsonType: 'string',
        pattern: '^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,16}$',
        description: 'Minimum 8 and maximum 16 characters, at least one uppercase letter, one lowercase letter, one number and one special character:'
      },
      empFirstPointOfContact: {
        pattern: '^[a-z0-9]{24}$',
        description: 'Can be of type null or 24 charchter long mongo Object id'
      },
      empSecondPointOfContact: {
        pattern: '^[a-z0-9]{24}$',
        description: 'Can be of type null or 24 charchter long mongo Object id'
      },
      empPosition: {
        bsonType: 'string',
        'enum': [
          'Admin',
          'TechLead',
          'GeneralManger',
          'SeniorManger',
          'ProjectManager',
          'TeamLeader',
          'CloudArchitect',
          'Developer',
          'Tester',
          'TechSupport'
        ],
        description: 'can only be one of the enum values'
      }
    }
  }
}

"""

class Employee:
    @unique
    class Position(Enum):
        Admin = auto()
        TechLead = auto()
        GeneralManger = auto()
        SeniorManger = auto()
        ProjectManager = auto()
        TeamLeader = auto()
        CloudArchitect = auto()
        Developer = auto()
        Tester = auto()
        TechSupport = auto()

    

    def __init__(self , empPosition :str, empName :str, empPassword :str, empFirstPointOfContact = None, 
                    empSecondPointOfContact = None ) -> None:
        self.empId = 0
        self.empName = empName
        self.empPassword = empPassword
        self.empFirstPointOfContact = empFirstPointOfContact
        self.empSecondPointOfContact = empSecondPointOfContact
        self.empPosition = self.Position[empPosition]

    def createEmployee(self)->str:
        try:
            result = employee.insert_one({
                                        "empName" : self.empName,
                                        "empPassword" : self.empPassword,
                                        "empFirstPointOfContact" : self.empFirstPointOfContact,
                                        "empSecondPointOfContact" : self.empSecondPointOfContact,
                                        "empPosition":self.empPosition.name}).inserted_id
            
            return "Object Inserted successfully " + str(result)
        except Exception as e:
            return "Database instance creationn failed \n" + str(e)
