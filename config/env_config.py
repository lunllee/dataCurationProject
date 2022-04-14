import os

args = {
    "development": {
        "input1": {
            "baseUrl": "startup-sodas-plus-datahub-api-221-154-134-31.nip.io:10005",
            "accessToken": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJoV0NadE12M2s0eUJ2T012Ml85Y21SbTBHN0Zuc094czNGVkpuZGc3NmI4In0.eyJleHAiOjE2NDk5MDA2NTIsImlhdCI6MTY0OTg5ODg1MiwianRpIjoiOWMyNGUzN2EtOTVmMy00NDkyLTk4Y2MtZmZkMjEzYmJmZTlkIiwiaXNzIjoiaHR0cHM6Ly9zdGFydHVwLXNzby5zb2Rhcy1wbHVzLmNvbS9hdXRoL3JlYWxtcy9tYXN0ZXItaSIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI2NTZlMTNkMS1jN2JkLTQ4ZjctYjc1MS0yMDZjNmUwYWE3MzYiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJwbGF0Zm9ybSIsInNlc3Npb25fc3RhdGUiOiI3ZGE3MTg4My1hMTBkLTQ5NDgtOGIzYS0zNGYyZjc1YTlkODkiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsIm9yZ19tZW1iZXIiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoicHJvZmlsZSBlbWFpbCIsImdyb3VwX21lbWJlcnNoaXAiOlsib2ZmbGluZV9hY2Nlc3MiLCJvcmdfbWVtYmVyIiwidW1hX2F1dGhvcml6YXRpb24iXSwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5hbWUiOiJ1c2VyIHVzZXIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ1c2VyIiwiZ2l2ZW5fbmFtZSI6InVzZXIiLCJmYW1pbHlfbmFtZSI6InVzZXIiLCJlbWFpbCI6InVzZXJAc29kYXMuZXRyaS5yZS5rciIsImdyb3VwIjpbIi9vcmdhbml6YXRpb24vZGVmYXVsdF9vcmcvcm9sZXMvb3JnX21lbWJlciJdfQ.F4bOcZ3U6DNmw3M3-SrNFgxFi99Qa9kqeleTQpPyy9ddcJAHEG8L4ulG4hhgnPJPcUXw87Z-NI9ZZdCgRi6cfRULrjn6sTGa1Zibypo6A87VO1RAVVCX8iybyKQR51cS35GwmZrbtWjNq0LR5VZS-tELw6NH3c35vrh7G4C5qi6A9hxegzoxg_JT7LIzEB-qto7oQuLktanzAOSzSZLI3B9wSH6nsIDAwnqlz4NAAwMv6RrUn8oWZqwPJcQcv_1TDTD6jvNv26y_H-oLqIDbh5ylPUHlKDvTgnS-9ov_GQTDkW86rG0piuqD5RjwT047HDj8bJRQrTIkqy7gBH-DHg",
            "datasetId": r"8fd2d3e0-352a-11ec-8bab-6194bb3a1754",
            "distributionId": r"cf1fbe80-352c-11ec-8bab-6194bb3a1754",
            "fileName": r"covid.csv",
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
            "accessToken": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJoV0NadE12M2s0eUJ2T012Ml85Y21SbTBHN0Zuc094czNGVkpuZGc3NmI4In0.eyJleHAiOjE2NDk5MDA2NTIsImlhdCI6MTY0OTg5ODg1MiwianRpIjoiOWMyNGUzN2EtOTVmMy00NDkyLTk4Y2MtZmZkMjEzYmJmZTlkIiwiaXNzIjoiaHR0cHM6Ly9zdGFydHVwLXNzby5zb2Rhcy1wbHVzLmNvbS9hdXRoL3JlYWxtcy9tYXN0ZXItaSIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI2NTZlMTNkMS1jN2JkLTQ4ZjctYjc1MS0yMDZjNmUwYWE3MzYiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJwbGF0Zm9ybSIsInNlc3Npb25fc3RhdGUiOiI3ZGE3MTg4My1hMTBkLTQ5NDgtOGIzYS0zNGYyZjc1YTlkODkiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsIm9yZ19tZW1iZXIiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoicHJvZmlsZSBlbWFpbCIsImdyb3VwX21lbWJlcnNoaXAiOlsib2ZmbGluZV9hY2Nlc3MiLCJvcmdfbWVtYmVyIiwidW1hX2F1dGhvcml6YXRpb24iXSwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5hbWUiOiJ1c2VyIHVzZXIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ1c2VyIiwiZ2l2ZW5fbmFtZSI6InVzZXIiLCJmYW1pbHlfbmFtZSI6InVzZXIiLCJlbWFpbCI6InVzZXJAc29kYXMuZXRyaS5yZS5rciIsImdyb3VwIjpbIi9vcmdhbml6YXRpb24vZGVmYXVsdF9vcmcvcm9sZXMvb3JnX21lbWJlciJdfQ.F4bOcZ3U6DNmw3M3-SrNFgxFi99Qa9kqeleTQpPyy9ddcJAHEG8L4ulG4hhgnPJPcUXw87Z-NI9ZZdCgRi6cfRULrjn6sTGa1Zibypo6A87VO1RAVVCX8iybyKQR51cS35GwmZrbtWjNq0LR5VZS-tELw6NH3c35vrh7G4C5qi6A9hxegzoxg_JT7LIzEB-qto7oQuLktanzAOSzSZLI3B9wSH6nsIDAwnqlz4NAAwMv6RrUn8oWZqwPJcQcv_1TDTD6jvNv26y_H-oLqIDbh5ylPUHlKDvTgnS-9ov_GQTDkW86rG0piuqD5RjwT047HDj8bJRQrTIkqy7gBH-DHg",
            # "accessToken": "CURRENT_ACCESS_TOKEN",
            "storageId": "7528c8c0-4db1-11ec-b7b6-1dd8f39867c6",
            "bucketName": "test",
            "objectName": "c_covid.csv"
        }
    }
}
