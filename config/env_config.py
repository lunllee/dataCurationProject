import os

args = {
    "development": {
        "input1": {
            "baseUrl": "...",
            "accessToken": "...",
            "dataset_id": r"8fd2d3e0-352a-11ec-8bab-6194bb3a1754",
            "distribution_id": r"cf1fbe80-352c-11ec-8bab-6194bb3a1754",
            "file_name": r"covid.csv",
            "params": [
                [
                    {
                        "id": "...",
                        "name": "cp_Date_reported",
                        "order": 1,
                        "command": "cp",
                        "addedFlag": "ADDED",
                        "columnType": "...",
                        "selectedColumn": [
                            "Date_reported"
                        ]
                    },
                    {
                        "id": "...",
                        "name": "cp_Country_code",
                        "order": 1,
                        "command": "cp",
                        "addedFlag": "ADDED",
                        "columnType": "...",
                        "selectedColumn": [
                            "Country_code"
                        ]
                    },
                    {
                        "id": "...",
                        "name": "cp_Country",
                        "order": 1,
                        "command": "cp",
                        "addedFlag": "ADDED",
                        "columnType": "...",
                        "selectedColumn": [
                            "Country"
                        ]
                    },
                    {
                        "id": "...",
                        "name": "cp_New_deaths",
                        "order": 1,
                        "command": "cp",
                        "addedFlag": "ADDED",
                        "columnType": "...",
                        "selectedColumn": [
                            "New_deaths"
                        ]
                    }
                ]
            ]
        },
        "output1": {
            "baseUrl": "startup-sodas-plus-datahub-api-129-254-221-92.nip.io:20005",
            "accessToken": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJoV0NadE12M2s0eUJ2T012Ml85Y21SbTBHN0Zuc094czNGVkpuZGc3NmI4In0.eyJleHAiOjE2NDk3NjMyNzAsImlhdCI6MTY0OTc2MTQ3MCwianRpIjoiMjljY2YwMmItZjU0ZS00ZjQ3LWI3YTEtNzI4ZDJkNzBhZjAyIiwiaXNzIjoiaHR0cHM6Ly9zdGFydHVwLXNzby5zb2Rhcy1wbHVzLmNvbS9hdXRoL3JlYWxtcy9tYXN0ZXItaSIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI2NTZlMTNkMS1jN2JkLTQ4ZjctYjc1MS0yMDZjNmUwYWE3MzYiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJwbGF0Zm9ybSIsInNlc3Npb25fc3RhdGUiOiIxZGFlODVhYi1hYTE1LTQxNDQtYjA2Ny00YTYwMWM3ODBlN2EiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsIm9yZ19tZW1iZXIiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoicHJvZmlsZSBlbWFpbCIsImdyb3VwX21lbWJlcnNoaXAiOlsib2ZmbGluZV9hY2Nlc3MiLCJvcmdfbWVtYmVyIiwidW1hX2F1dGhvcml6YXRpb24iXSwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5hbWUiOiJ1c2VyIHVzZXIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ1c2VyIiwiZ2l2ZW5fbmFtZSI6InVzZXIiLCJmYW1pbHlfbmFtZSI6InVzZXIiLCJlbWFpbCI6InVzZXJAc29kYXMuZXRyaS5yZS5rciIsImdyb3VwIjpbIi9vcmdhbml6YXRpb24vZGVmYXVsdF9vcmcvcm9sZXMvb3JnX21lbWJlciJdfQ.ai_i--E1ljRQVWyTvIIxWiU-yJZVvaOF3-r5nrj7liLHrpJlB8HQJL30UCIp4-QJCE9DNI0ZrZtm-aPs9LRT_e1pjDLy0d8BdX9UcAKHSCV1UEPO_rpiD0mlwD5QUpOIlOLdUtp-KFlZ9iZ0JNJW5jKNr2Ud7Ur4rgOYktA1EiAw1xcvS9wsootXQL5wwUH1bakqeXZBo9Lm4FnX9okD5vZgqMTL39KSG1-6dVs8jPqKrQsvOEqvTzls8MtlYenaBKyH6KAw6qD_NxOqCO30g27EVtj0jSIdG3l3utWigz6DKs5XrQ-HBM4FIcGRAQpnuUqUSujQCQtXCftO9l5-5Q",
            # "accessToken": "CURRENT_ACCESS_TOKEN",
            "storageId": "7528c8c0-4db1-11ec-b7b6-1dd8f39867c6",
            "bucketName": "test",
            "objectName": "c_covid.csv"
        }
    }
}
