import pandas as pd
from writeBodies import *
from helpers import callApi
from platformIdClass import *
from engine import *
from requests.exceptions import RequestException
from getRequestBody import *
from compareJson import *

engine = sqlalchemy.create_engine("postgresql://postgres:RB9j2ZPOb0hiICMr6f7q@34.93.223.34/staging")

def getCompanyId(org_id: int, integration: str):
    # Fetch company id
    query = f"""SELECT rootfi_company_id from "Connections" WHERE integration_type = '{integration}' and rootfi_organisation_id = {org_id} and status = 'HEALTHY'"""
    df = pd.read_sql(query, engine)
    if len(df) == 0:
        return None
    return df["rootfi_company_id"][0]

def runTestCase(run_for_datamodels, run_for_integrations, supported_fields, config):
    failed_for = []
    for datamodel in run_for_datamodels:
        for integration in run_for_integrations:
            print(f"running for {integration}: {datamodel}")
            # get company id
            company_id = getCompanyId(config["org_id"], integration)
            # get sample body
            try:
                sampleBody = WRITE_BODIES[datamodel]
            except KeyError as e:
                raise ValueError(f"❌ No sample body found for '{datamodel}'")
            # initialize the platform ids class
            platformIdClass = GetPlatformId(company_id, integration, datamodel)

            # get integration request body #
            requestData = getRequestObject(company_id, sampleBody, supported_fields, platformIdClass, datamodel)
            if requestData == {}: # no supported fields
                print(f"❌ No supported fields found for '{integration}': '{datamodel}'")
                continue
            # request body
            requestBody = {"company_id": int(company_id), "data": [requestData]}
            # make rootfi api call #
            try:
                responseData = callApi(
                    config["URL"] + "/accounting/" + datamodel.lower(),
                    data=requestBody,
                    reqHeaders=config["HEADERS"],
                )
                # compare data #
                try:
                    requestData = requestBody["data"][0]
                    returnedData = responseData["data"]["data"][0]
                    # print("requestData", requestData, "\n\nreturnedData", returnedData)
                    compare_json(requestData, returnedData, integration, datamodel)
                    print("✅ Test passed for: ", datamodel)
                except ValueError as e:
                    message = f"❌ Test failed for '{integration}': '{datamodel}'"
                    print(message, ", ", e)
                    failed_for.append(message)
            except RequestException as e:
                message = f"❌ API Call failed for '{integration}': '{datamodel}'\nmessage: {e}"
                print(message)
                failed_for.append(message)

    print(f"✅ Finished. {len(failed_for)} test cases failed!")
