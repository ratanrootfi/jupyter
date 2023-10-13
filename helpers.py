import requests
from requests.exceptions import RequestException, HTTPError
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine(
    "postgresql://postgres:RB9j2ZPOb0hiICMr6f7q@34.93.223.34/staging"
)


def callApi(endpoint: str, data={}, reqHeaders: dict = {}, reqParams: dict = {}):
    try:
        response = requests.post(
            endpoint, json=data, headers=reqHeaders, params=reqParams
        )
        response.raise_for_status()
        data = response.json()
        return data
    except HTTPError as e:
        raise
    except RequestException:
        raise


def getLastJobStatus(integration: str, company_id: int, job_type: str):
    query = f"""
                SELECT * FROM "Jobs" WHERE integration_type = '{integration}' 
                AND rootfi_company_id = {company_id} AND config_mode = '{job_type}' 
                ORDER BY rootfi_created_at DESC LIMIT 1
            """
    df = pd.read_sql(query, engine)
    return {"error_code": df["error_code"][0], "status": df["status"][0]}


def checkErrorResponse(e, rootfi_company_id, expected_status, expected_code):
    try:
        status, code = e.response.status_code, e.response.json()["error"]["code"]
        # Check Response
        assert status == expected_status
        assert code == expected_code
        # Check Job
        jobData = getLastJobStatus("ROOTFI_SANDBOX", rootfi_company_id, "CREATE")
        assert expected_code == jobData["error_code"]
        return "✅ success"
    except AssertionError:
        return "❌ failed"
