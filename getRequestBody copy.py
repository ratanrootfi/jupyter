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
        tempLine = getRequestObject(
            company_id,
            k,
            supported_fields,
            platformIdClass,
            key,
        )
        lines.append(tempLine)
    return lines

def handleDefaultValues(config, platformIdClass, key,replaceIds):
    # replace specific field values from default_datamodel_config in writeBodies.py
    default_value = config[key][platformIdClass.getIntegration()]
    if isinstance(default_value, dict):
        default_values_data = {}
        for each_key in default_value.keys():
            if "id" in each_key:
                default_values_data[each_key] = replaceIds(each_key) # replace ids in nested fields rawdata, invoice item, bill item
            else:
                default_values_data[each_key] = default_value[each_key] # use default values default_datamodel_config in writeBodies.py
        default_value = default_values_data

    return default_value


def getRequestObject(company_id, sampleData, supported_fields, platformIdClass, datamodel):

    def replaceIds(column: str):
        if datamodel in NESTED_DATA_FIELDS:
            field = datamodel+"."+column
        else:
            field = column
            
        if column == "currency_id":
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
        elif column == "account_id":
            return platformIdClass.getId("accounts",field)
        elif column == "from_account_id":
            return platformIdClass.getFromAccountId()
        elif column == "tracking_category_ids":
            tracking_category_id = platformIdClass.getId("tracking_categories",field)
            return [tracking_category_id] if tracking_category_id else []

    returnData = {}
    config = default_datamodel_config[datamodel] if datamodel in default_datamodel_config.keys() else {}
    
    integration_supported_fields = supported_fields[datamodel.upper()][platformIdClass.getIntegration()]
    voucher_related_datamodels = VOUCHER_RELATED_DATAMODELS.keys()
    
    if datamodel in voucher_related_datamodels:
        #######################################
        # This for the datamodels in the voucher related datamodels list
        # all the ids can be fetched from the invoices or bills and the master ids should match the voucher itself
        # we can avoid making one sql query for each id field and can use the voucher master ids
        # for example for invoice payments we fetch one invoice and use all the ids like account id, contact id from the invoice data itself
        #######################################
        voucher_data = platformIdClass.getVoucherRelatedDatamodelData(datamodel,VOUCHER_RELATED_DATAMODELS)
        for i in sampleData.keys():
            if i not in integration_supported_fields:
                continue
            if "_id" in i:
                try:
                    idData = voucher_data[i if "ids" not in i else i[:-1]]
                    returnData[i] = idData if "ids" not in i else [idData]
                except KeyError:
                    returnData[i] = replaceIds(i)
            elif i == "line_items" or i == "journal_lines":
                returnData[i] = handleLines(company_id, writeBodies, supported_fields, platformIdClass, i)
            elif i in list(config.keys()):
                returnData[i] = handleDefaultValues(config, platformIdClass, i, replaceIds)
            elif "_date" in i:
                returnData[i] = handleDates(i, voucher_data)
            else:
                # use faker fields
                returnData[i] = sampleData[i]

        return returnData

    for i in sampleData.keys():
        if i not in integration_supported_fields:
            continue
        if "_id" in i:
            returnData[i] = replaceIds(i)
        elif i == "line_items" or i == "journal_lines":
            returnData[i] = handleLines(company_id, writeBodies, supported_fields, platformIdClass, i)
        elif i in list(config.keys()):
            returnData[i] = handleDefaultValues(config, platformIdClass, i, replaceIds)
        else:
            # use faker fields
            returnData[i] = sampleData[i]

    return returnData