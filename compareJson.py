# TODO: avoid in nested fields -- done
keys_to_avoid = {
    "ZOHO_BOOKS": {
        "BILL_CREDIT_NOTES": ["line_items.total_discount"], # have to keep these to avoid as they get passed through line items
        "EXPENSES": ["line_items.item_id", "line_items.tax_id", "line_items.quantity", "line_items.total_discount"],
        "PURCHASE_ORDERS": [
            "description"
        ],  ## TODO : check description is not undefined in old test but is always empty in db?
        "SALES_ORDERS": ["line_items.account_id"],
    },
    "ODOO_ACCOUNTING": {
        "INVOICES": ["line_items.total_discount"],
        "INVOICE_CREDIT_NOTES": ["line_items.total_discount"],
        "BILL_CREDIT_NOTES": ["line_items.total_discount"],
        "BILLS": ["line_items.total_discount"],
        "SALES_ORDERS": ["line_items.total_discount"],
        "PURCHASE_ORDERS": ["line_items.total_discount"],
        "ITEMS":[
            "bill_item.account_id",
            "invoice_item.account_id",
            "description",
            "invoice_item.description" # item description gets returned
        ],
    },
    "WAVE":{
        "ITEMS":["bill_item.description","bill_item.unit_price","invoice_item.description"]
    },
    "MEKARI_JURNAL":{
        "INVOICES":["line_items.total_discount","total_discount","line_items.account_id"],
        "BILLS":["total_discount","line_items.account_id"],
        "INVOICE_CREDIT_NOTES":["line_items.total_discount","line_items.account_id"],
        "BILL_CREDIT_NOTES":["line_items.total_discount","line_items.account_id"],
        "ITEMS":["bill_item.description","bill_item.unit_price","invoice_item.description","invoice_item.unit_price"],
        "SALES_ORDERS":["line_items.total_discount","line_items.account_id","line_items.description"],
        "PURCHASE_ORDERS":["line_items.total_discount","line_items.account_id","line_items.description"],
        "EXPENSES":["line_items.total_discount","line_items.item_id","line_items.tax_id","line_items.quantity","line_items.unit_amount"],
    }
}


def compare_json(json1: dict, json2: dict, integration, datamodel,nested_key:str=None):
    for key in json1:
        if key in ['raw_data',"email","telephone","mobile","website","addresses","fax"]: # TODO: compare data for external links and phone numbers
            continue
        keysToAvoid = []
        try:
            keysToAvoid = keys_to_avoid[integration][datamodel]
        except KeyError:
            pass

        if nested_key:
            if (nested_key + "." + key )in keysToAvoid:
                #############################################
                ## example
                ## total_discount is not returned in bill credit notes
                ## we have common line items write body in write bodies so total_discount is passed in the request body
                #############################################
                continue
        if key not in json2:
            raise ValueError(f"'{key}' not in response")
        
        value1 = json1[key]
        value2 = json2[key]


        #############################################
        ## change date format for check - we pass "YYYY-MM-DD" and we get back "YYYY-MM-DDTHH:MM:SSZ" ##
        if "_date" in key:
            value2 = value2.split("T")[0]
        #############################################

        if isinstance(value1, dict):
            compare_json(value1, value2, integration, datamodel,key)
        elif isinstance(value1, list):
            if len(value1) != len(value2):
                raise ValueError(f"'{key}' length not matched. Expected {len(value1)} but got {len(value2)}")
            if len(value1) == 0 and len(value2) == 0:
                continue

            if (isinstance(value1[0], str)) and (isinstance(value2[0], str)):  # inoice and bill ids
                for o in range(len(value1)):
                    if value1[o] != value2[o]:
                        raise ValueError(f"'{key}' values not matched")
            # else: line items
            #     for i, (item1, item2) in enumerate(zip(value1, value2)):
            #         compare_json(item1, item2, integration, datamodel,key)
        else:
            if value1 != value2:
                raise ValueError(f"'{key}' values not matched")