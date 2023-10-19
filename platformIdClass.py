import pandas as pd
from writeBodies import *
from engine import *
from writeBodies import DEFAULT_DATAMODEL_CONFIG
from json import loads, dumps
from platformIdFetchConditions import CUSTOM_TABLE_FETCH_CONDITIONS, PLATFORM_ID_FETCH_CONDITIONS

#TODO: make supported for nested fields -- done
# PLATFORM_ID_FETCH_CONDITIONS 
    
class GetPlatformId:
    def __init__(self, company_id: int, integration: str, datamodel: str):
        self.company_id = company_id
        self.integration = integration
        self.datamodel = datamodel
        self.datamodel_config = DEFAULT_DATAMODEL_CONFIG[datamodel] if datamodel in DEFAULT_DATAMODEL_CONFIG.keys() else {}

    def generateConditionQuery(self, field: str):
        all_conditions = {}
        try:
            all_conditions = PLATFORM_ID_FETCH_CONDITIONS[self.datamodel][field][self.integration]
        except KeyError:
            all_conditions = {}
        if len(all_conditions.keys()) == 0:
            return ""  # no condition required

        condition_query = ""
        for i in all_conditions.keys():
            condition_query += f" and {i} = '{all_conditions[i]}'"
        return condition_query

    def getIntegration(self):
        return self.integration

    def getDatamodel(self):
        return self.datamodel

    def fetchData(self,fetch_from_table:str,condition:str):
        # makes the query, executes it and returns the platform id
        # if self.getIntegration() == "SAGE_CLOUD_ACCOUNTING" and fetch_from_table == "accounts" and self.getDatamodel() in ["INVOICE_PAYMENTS", "BILL_PAYMENTS"]:
        #     # to do make this dynamic
        #     fetch_from_table = "bank_accounts"
        
        query = f"""SELECT platform_id from {fetch_from_table} WHERE rootfi_company_id = {self.company_id} {condition} LIMIT 1"""
        return returnPlatformId(query)

    def getParentAccountId(self):
        sub_category = self.datamodel_config["sub_category"][self.integration]  ## these are not PLATFORM_ID_FETCH_CONDITIONS but default set values we make accounts for
        condition = self.generateConditionQuery("parent_account_id")
        query = f"SELECT platform_id FROM accounts WHERE rootfi_company_id = '{self.company_id}' and sub_category = '{sub_category}' {condition} LIMIT 1"
        return returnPlatformId(query)

    def getId(self,fetch_from_table:str,field:str):

        try:
            fetch_from_table = CUSTOM_TABLE_FETCH_CONDITIONS[self.datamodel][field][self.integration]
        except KeyError:
            pass
        print("field: ",field, "fetch_from_table: ",fetch_from_table)
        condition = self.generateConditionQuery(field)
        return self.fetchData(fetch_from_table,condition)

    def getFromAccountId(self):
        condition = self.generateConditionQuery("from_account_id")
        return self.fetchData("accounts",condition)

    def getVoucherRelatedDatamodelData(self, datamodel: str,voucher_related_datamodels:dict):
        contacts_condition = " and contacts.status = 'ACTIVE'" if self.integration != "MS_DYNAMICS_365" else ""
        query = f"SELECT {voucher_related_datamodels[datamodel]}.* from {voucher_related_datamodels[datamodel]} INNER JOIN contacts ON {voucher_related_datamodels[datamodel]}.contact_id = contacts.platform_id WHERE {voucher_related_datamodels[datamodel]}.rootfi_company_id = {self.company_id} {contacts_condition} {' and '+ voucher_related_datamodels[datamodel]+'.amount_due > 1' if datamodel in ['INVOICE_PAYMENTS', 'BILL_PAYMENTS'] else ''} LIMIT 1"
        print("query", query)
        df_json = queryAndReturnDict(query)["0"]  # convert dataframe to json
        df_json[f"{voucher_related_datamodels[datamodel][:-1]}_id"] = df_json["platform_id"]  # add platform id as voucher id
        print("voucher data", df_json)
        return df_json


def queryAndReturnDict(query):
    df = pd.read_sql(query, engine)
    df_json = loads(df.to_json(orient="index"))  # convert dataframe to json
    return df_json


# TODO:
# common query functions - done
# common loop for voucher based datamodels -- done