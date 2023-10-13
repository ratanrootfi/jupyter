# TODO: avoid in nested fields
keys_to_avoid = {
    "ZOHO_BOOKS": {
        "BILL_CREDIT_NOTES": ["total_discount"],
        "EXPENSES": ["item_id", "tax_id", "quantity", "total_discount"],
        "PURCHASE_ORDERS": [
            "description"
        ],  ## TODO : check description is not undefined in old test but is always empty in db?
        "SALES_ORDERS": ["account_id"],
    }
}


def compare_json(json1: dict, json2: dict, integration, datamodel):
    for key in json1:
        if key not in json2:
            keysToAvoid = []
            try:
                keysToAvoid = keys_to_avoid[integration][datamodel]
            except KeyError:
                pass
            if key in keysToAvoid:
                #############################################
                ## example
                ## total_discount is not returned in bill credit notes
                ## we have common line items write body in write bodies so total_discount is passed in the request body
                #############################################
                continue
            raise ValueError(f"'{key}' not in response ❌")
        value1 = json1[key]
        value2 = json2[key]

        #############################################
        ## change date format for check - we pass "YYYY-MM-DD" and we get back "YYYY-MM-DDTHH:MM:SSZ" ##
        if "_date" in key:
            value2 = value2.split("T")[0]
        #############################################

        if isinstance(value1, dict):
            compare_json(value1, value2, integration, datamodel)
        elif isinstance(value1, list):
            if len(value1) != len(value2):
                raise ValueError(f"'{key}' length not matched ❌")
            if len(value1) == 0 and len(value2) == 0:
                continue

            if (isinstance(value1[0], str)) and (
                isinstance(value2[0], str)
            ):  # inoice and bill ids
                for o in range(len(value1)):
                    if value1[o] != value2[o]:
                        raise ValueError(f"'{key}' values not matched ❌")
            else:
                for i, (item1, item2) in enumerate(zip(value1, value2)):
                    compare_json(item1, item2, integration, datamodel)
        else:
            if value1 != value2:
                raise ValueError(f"'{key}' values not matched ❌")

