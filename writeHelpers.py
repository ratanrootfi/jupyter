import pandas as pd
from writeBodies import *
from helpers import callApi
from platformIdClass import *
from engine import *
from requests import *
from getRequestBody import *
from compareJson import *

engine = sqlalchemy.create_engine(DATABASE_URL)

def getCompanyId(org_id: int, integration: str):
    # Fetch company id
    query = f"""SELECT rootfi_company_id from "Connections" WHERE integration_type = '{integration}' and rootfi_organisation_id = {org_id} and status = 'HEALTHY' order by rootfi_company_id desc limit 1"""
    df = pd.read_sql(query, engine)
    if len(df) == 0:
        raise ValueError(f"❌ No company id found for '{integration}'")
    company_id = df["rootfi_company_id"][0]
    # print(f"company_id: {company_id}")  
    return company_id

def runTestCase(run_for_datamodels, run_for_integrations, supported_fields, config):
    failed_for = 0
    new_dataframe = pd.DataFrame(columns=["integration", "datamodel", "status", "message"])

    def pushErrorToDataframe(message, integration, status, datamodel):
        new_dataframe.loc[len(new_dataframe)] = [integration, datamodel, status, message]


    for datamodel in run_for_datamodels:
        for integration in run_for_integrations:
            company_id = getCompanyId(config["org_id"], integration)
            # get company id
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
                pushErrorToDataframe("No supported fields found", integration,"❌ Failed!", datamodel)
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
                    returnedData = responseData["data"]['data'][0]['response']
                    compare_json(requestData, returnedData, integration, datamodel)
                    pushErrorToDataframe("", integration,"✅ Passed!", datamodel)
                except ValueError as e:
                    pushErrorToDataframe(e, integration,"❌ Failed!", datamodel)
                    failed_for += 1
            except exceptions.HTTPError as errh:
                pushErrorToDataframe(errh.response.json()['error']['platform_error'], integration,"❌ Failed!", datamodel)
                failed_for += 1
    # print("\n\n\n")
    print(f"✅ Finished. {failed_for} test cases failed!")
    return new_dataframe
