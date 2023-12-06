from writeBodies import *
from datetime import datetime, timedelta


VOUCHER_RELATED_DATAMODELS = {
    "INVOICE_PAYMENTS": "invoices",
    "INVOICE_CREDIT_NOTES": "invoices",
    "BILL_PAYMENTS": "bills",
    "BILL_CREDIT_NOTES": "bills",
    "PURCHASE_ORDERS": "bills",
    "SALES_ORDERS": "invoices",
}
NESTED_DATA_FIELDS = ["line_items", "journal_lines"]

KEYS_TO_NEVER_OMIT = ["contact_type","line_items","journal_lines"]

def handleDates(key, voucher_data):
    if (key == "delivery_date" or key == "payment_date"):
        # no delivery date in bill and invoice so use posted date for purchase orders and sales orders
        # payments and credit notes dates should be one day after the invoice or bill date
        voucherDate = voucher_data["posted_date"]  
        newDate = datetime.fromtimestamp(voucherDate / 1000.0) + timedelta(days=1)
    else:
        # posted date is the voucher date
        voucherDate = voucher_data[key]  # 2023-03-19 00:00:00+00
        newDate = datetime.fromtimestamp(voucherDate / 1000.0) 
    return str(newDate).split(" ")[0]

def handleLines(company_id, writeBodies, supported_fields, platformIdClass, key):
    lines = []
        
    for k in writeBodies["LINE_ITEMS" if key == "line_items" else "JOURNAL_LINES"]:
        # if key == "line_items":
        #     del k['account_id']
        tempLine = getRequestObject(
            company_id,
            k,
            supported_fields,
            platformIdClass,
            key,
        )
        lines.append(tempLine)
    return lines

def handleDefaultValues(config, platformIdClass, key,replaceIds,datamodel):
    # replace specific field values from default_datamodel_config in writeBodies.py
    if platformIdClass.getIntegration() not in config[key].keys():
        raise ValueError(f"integration not found in default_datamodel_config for {key} ❌")
    
    default_value = config[key][platformIdClass.getIntegration()]
    if isinstance(default_value, dict):
        default_values_data = {}
        for each_key in default_value.keys():
            if "id" in each_key:
                default_values_data[each_key] = replaceIds(datamodel,each_key,platformIdClass,key) # replace ids in nested fields rawdata, invoice item, bill item
            else:
                default_values_data[each_key] = default_value[each_key] # use default values default_datamodel_config in writeBodies.py
        default_value = default_values_data

    return default_value

def replaceIds(datamodel:str,column: str,platformIdClass,parent_field:str=None): # parent field is only for json nested fields like invoice item, bill item
    if datamodel in NESTED_DATA_FIELDS:
        field = datamodel+"."+column
    elif parent_field:
        field = parent_field+"."+column
    else:
        field = column
    if column == "currency_id":
        if platformIdClass.getIntegration() in ["WAFEQ","NETSUITE"]:
            return "INR" if platformIdClass.getIntegration() == "WAFEQ" else "1"
        return platformIdClass.getId("currencies",field)
    elif column == "parent_account_id":
        return platformIdClass.getParentAccountId()
    elif column == "contact_id":
        return platformIdClass.getId("contacts",field)
    elif column == "sales_order_ids":
        return platformIdClass.getId("sales_orders",field)
    elif column == "tax_id":
        return platformIdClass.getId("tax_rates",field)
    elif column == "item_id":
        return platformIdClass.getId("items",field)
    elif column == "account_id" or "account_id" in column:
        return platformIdClass.getId("accounts",field)
    elif column == "from_account_id":
        return platformIdClass.getFromAccountId()
    elif column == "tracking_category_ids":
        tracking_category_id = platformIdClass.getId("tracking_categories",field)
        return [tracking_category_id] if tracking_category_id else []
    

def getRequestObject(company_id, sampleData, supported_fields, platformIdClass, datamodel):
    requestObject = {}
    config = DEFAULT_DATAMODEL_CONFIG[datamodel] if datamodel in DEFAULT_DATAMODEL_CONFIG.keys() else {}
    integration_supported_fields = supported_fields[datamodel.upper()][platformIdClass.getIntegration()]
    if (len(integration_supported_fields) == 0):
        return requestObject
    voucher_related_datamodels = VOUCHER_RELATED_DATAMODELS.keys()
    voucher_data = {}

    if datamodel in voucher_related_datamodels:
        voucher_data = platformIdClass.getVoucherRelatedDatamodelData(datamodel,VOUCHER_RELATED_DATAMODELS)
    for rootfi_field in sampleData.keys():
        if rootfi_field not in integration_supported_fields and rootfi_field not in KEYS_TO_NEVER_OMIT:
            continue
        if "_id" in rootfi_field:
            try:
                if platformIdClass.getIntegration() == "NETSUITE" and rootfi_field == "currency_id":
                    requestObject[rootfi_field] = "1"
                    continue
                idData = voucher_data[rootfi_field if "ids" not in rootfi_field else rootfi_field[:-1]]
                requestObject[rootfi_field] = idData if "ids" not in rootfi_field else [idData]
            except KeyError:
                replaceValue = replaceIds(datamodel,rootfi_field,platformIdClass)
                if replaceValue:
                    requestObject[rootfi_field] = replaceValue
                else:
                    requestObject[rootfi_field] = sampleData[rootfi_field]
        elif rootfi_field == "line_items" or rootfi_field == "journal_lines":
            requestObject[rootfi_field] = handleLines(company_id, WRITE_BODIES, supported_fields, platformIdClass, rootfi_field)
        elif isinstance(sampleData[rootfi_field],dict): # invoice item, bill items
            item = {}
            for nested_field in sampleData[rootfi_field].keys():
                if "_id" in nested_field:
                    replaceValue = replaceIds(datamodel,nested_field,platformIdClass,rootfi_field)
                    if replaceValue:
                        item[nested_field] = replaceValue
                    else:
                        item[nested_field] = sampleData[rootfi_field][nested_field]
                else:
                    item[nested_field] = sampleData[rootfi_field][nested_field]
            requestObject[rootfi_field] = item
        elif rootfi_field in list(config.keys()):
            requestObject[rootfi_field] = handleDefaultValues(config, platformIdClass, rootfi_field, replaceIds,datamodel)
        elif datamodel in voucher_related_datamodels and "_date" in rootfi_field:
            if platformIdClass.getIntegration() == "QUICKBOOKS_SANDBOX": # TODO: change this 
                requestObject[rootfi_field] = "2023-09-01"
            else:
                requestObject[rootfi_field] = handleDates(rootfi_field, voucher_data)
        elif rootfi_field == "addresses":
            requestObject[rootfi_field] = WRITE_BODIES["ADDRESSES"]
        else:
            # use faker fields
            requestObject[rootfi_field] = sampleData[rootfi_field]

    return requestObject