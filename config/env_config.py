import os

args = {
    "development": {
        "input1": {
            "baseUrl": "startup-sodas-plus-datahub-api-221-154-134-31.nip.io:10005",
            "accessToken": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJoV0NadE12M2s0eUJ2T012Ml85Y21SbTBHN0Zuc094czNGVkpuZGc3NmI4In0.eyJleHAiOjE2NDk4NTI5NTYsImlhdCI6MTY0OTg1MTE1NiwianRpIjoiMDFhZmE5NWMtY2NiNS00ZjdlLTk5MTctOTUwOWUxMGE3MmM3IiwiaXNzIjoiaHR0cHM6Ly9zdGFydHVwLXNzby5zb2Rhcy1wbHVzLmNvbS9hdXRoL3JlYWxtcy9tYXN0ZXItaSIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI2NTZlMTNkMS1jN2JkLTQ4ZjctYjc1MS0yMDZjNmUwYWE3MzYiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJwbGF0Zm9ybSIsInNlc3Npb25fc3RhdGUiOiI1ZDRlYjM1ZS0yOWQ3LTQ5NjQtOWM2Yi02MGNmZTYxYTgyMzkiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsIm9yZ19tZW1iZXIiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoicHJvZmlsZSBlbWFpbCIsImdyb3VwX21lbWJlcnNoaXAiOlsib2ZmbGluZV9hY2Nlc3MiLCJvcmdfbWVtYmVyIiwidW1hX2F1dGhvcml6YXRpb24iXSwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5hbWUiOiJ1c2VyIHVzZXIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ1c2VyIiwiZ2l2ZW5fbmFtZSI6InVzZXIiLCJmYW1pbHlfbmFtZSI6InVzZXIiLCJlbWFpbCI6InVzZXJAc29kYXMuZXRyaS5yZS5rciIsImdyb3VwIjpbIi9vcmdhbml6YXRpb24vZGVmYXVsdF9vcmcvcm9sZXMvb3JnX21lbWJlciJdfQ.Tg998_lXuAMW9NDObWlm7wr7XqcwozWLrB9XIruEBeQVeJVCEJPCuR0UeeQMLUBc6AYVvDdSaBl1M_3PTQVWzNmPr7NcitvF3XCzm0nEZ6X4t3Cc45XZCgkRMUgZ4OY72vvtPZMdwfN-0qKEi1MOgsSp6NaPn8wVaXy_IpuJNDyC-tQbusRNY0FXUNZ1Xzsi7vZfIsjjZmQVJclz0JqZzauGTZjSs81KXtVgBAIZ5LpvXULNx-azpIPJs5R3lThENJnhUepMdHtGRtYsgXzHY-kuXaPIJdiUXyKJz7a44g2dLlLbmJAry-MRzXUXrjIvmMNXkkDEdOtD0ehI_8F19Q",
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
            "accessToken": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJoV0NadE12M2s0eUJ2T012Ml85Y21SbTBHN0Zuc094czNGVkpuZGc3NmI4In0.eyJleHAiOjE2NDk4NTI5NTYsImlhdCI6MTY0OTg1MTE1NiwianRpIjoiMDFhZmE5NWMtY2NiNS00ZjdlLTk5MTctOTUwOWUxMGE3MmM3IiwiaXNzIjoiaHR0cHM6Ly9zdGFydHVwLXNzby5zb2Rhcy1wbHVzLmNvbS9hdXRoL3JlYWxtcy9tYXN0ZXItaSIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI2NTZlMTNkMS1jN2JkLTQ4ZjctYjc1MS0yMDZjNmUwYWE3MzYiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJwbGF0Zm9ybSIsInNlc3Npb25fc3RhdGUiOiI1ZDRlYjM1ZS0yOWQ3LTQ5NjQtOWM2Yi02MGNmZTYxYTgyMzkiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsIm9yZ19tZW1iZXIiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoicHJvZmlsZSBlbWFpbCIsImdyb3VwX21lbWJlcnNoaXAiOlsib2ZmbGluZV9hY2Nlc3MiLCJvcmdfbWVtYmVyIiwidW1hX2F1dGhvcml6YXRpb24iXSwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5hbWUiOiJ1c2VyIHVzZXIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ1c2VyIiwiZ2l2ZW5fbmFtZSI6InVzZXIiLCJmYW1pbHlfbmFtZSI6InVzZXIiLCJlbWFpbCI6InVzZXJAc29kYXMuZXRyaS5yZS5rciIsImdyb3VwIjpbIi9vcmdhbml6YXRpb24vZGVmYXVsdF9vcmcvcm9sZXMvb3JnX21lbWJlciJdfQ.Tg998_lXuAMW9NDObWlm7wr7XqcwozWLrB9XIruEBeQVeJVCEJPCuR0UeeQMLUBc6AYVvDdSaBl1M_3PTQVWzNmPr7NcitvF3XCzm0nEZ6X4t3Cc45XZCgkRMUgZ4OY72vvtPZMdwfN-0qKEi1MOgsSp6NaPn8wVaXy_IpuJNDyC-tQbusRNY0FXUNZ1Xzsi7vZfIsjjZmQVJclz0JqZzauGTZjSs81KXtVgBAIZ5LpvXULNx-azpIPJs5R3lThENJnhUepMdHtGRtYsgXzHY-kuXaPIJdiUXyKJz7a44g2dLlLbmJAry-MRzXUXrjIvmMNXkkDEdOtD0ehI_8F19Q",
            # "accessToken": "CURRENT_ACCESS_TOKEN",
            "storageId": "7528c8c0-4db1-11ec-b7b6-1dd8f39867c6",
            "bucketName": "test",
            "objectName": "c_covid.csv"
        }
    }
}
