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
      'empPassword',
      'empPosition'
    ],
    properties: {
      empName: {
        bsonType: 'string',
        uniqueItems: true,
        description: 'The Name must be string and Name Mandatory and Name must be unquie'
      },
      empPassword: {
        bsonType: 'string',
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
          'TechSupport',
          InvalidPosition
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
        InvalidPosition = auto()

    def __init__(self, empName: str, empPassword=None, empFirstPointOfContact=None,
                 empSecondPointOfContact=None, empPosition=Position.InvalidPosition.name) -> None:
        self.empId = 0
        self.empName = empName
        self.empPassword = empPassword
        self.empFirstPointOfContact = empFirstPointOfContact
        self.empSecondPointOfContact = empSecondPointOfContact
        self.empPosition = self.Position[empPosition]

    def createEmployee(self) -> str:
        try:
            result = employee.insert_one({
                "empName": self.empName,
                "empPassword": self.empPassword,
                "empFirstPointOfContact": self.empFirstPointOfContact,
                "empSecondPointOfContact": self.empSecondPointOfContact,
                "empPosition": self.empPosition.name}).inserted_id

            return {"MongoMessage": "Object Inserted successfully " + str(result),
                    "CreationStaus": True}
        except Exception as e:
            return {"MongoMessage": "Database instance creationn failed \n" + str(e),
                    "CreationStaus": False}

    def findOneEmployee(self) -> str:
        try:
            result = employee.find_one({"empName": self.empName})
            print(result)
            return result
        except Exception as e:
            print(e)
            return None
