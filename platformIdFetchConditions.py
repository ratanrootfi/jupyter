PLATFORM_ID_FETCH_CONDITIONS = {
    "ACCOUNTS": {  ## datamodel we are querying for
        "currency_id": {  ## field we are querying on
            "ZOHO_BOOKS": {
                "is_base_currency": "true",  ## condition we are querying for - key is column name, value is the condition value
            }
        },
    },
    "INVOICES": {
        "currency_id": {"ZOHO_BOOKS": {"is_base_currency": "true"}},
        "contact_id": {"ZOHO_BOOKS": {"contact_type": "CUSTOMER", "status": "ACTIVE"}},
        "line_items.tax_id": {"ZOHO_BOOKS": {"raw_data ->> 'tax_type'": "tax_group"}},
        "line_items.account_id": {"ZOHO_BOOKS": {"sub_category": "other_current_liability"}},
    },
    "BANK_ACCOUNTS": {
        "currency_id": {"ZOHO_BOOKS": {"is_base_currency": "true"}},
    },
    "BANK_TRANSACTIONS": {
        "account_id": {"ZOHO_BOOKS": {"sub_category": "bank"}},  # only for bank transactions type deposit 
        "from_account_id": {
            "ZOHO_BOOKS": {"sub_category": "cash"}
        },  # only for bank transactions type deposit 
        "contact_id": {"ZOHO_BOOKS": {"status": "ACTIVE", "contact_type": "CUSTOMER"}},
    },
    "CONTACTS": {
        "currency_id": {"ZOHO_BOOKS": {"is_base_currency": "true"}},
    },
    "INVOICE_PAYMENTS": {"account_id": {"ZOHO_BOOKS": {"sub_category": "bank"}}},
    "BILL_PAYMENTS": {"account_id": {"ZOHO_BOOKS": {"sub_category": "bank"}}},
    "INVOICE_CREDIT_NOTES": {
        "line_items.tax_id": {
            "ZOHO_BOOKS": {
                "tax_type": "igst"
            }
        },
        "line_items.account_id":{
            "ZOHO_BOOKS": {
                "sub_category": "cost_of_goods_sold"
            }
        }
    },
    "BILL_CREDIT_NOTES": {
        "line_items.item_id": {"ZOHO_BOOKS": {"raw_data->>'item_type'": "sales_and_purchases"}},
        "line_items.tax_id": {
            "ZOHO_BOOKS": {
                "tax_type": "igst"
            }
        },
        "line_items.account_id":{
            "ZOHO_BOOKS": {
                "sub_category": "cost_of_goods_sold"
            }
        }
    },
    "ITEMS": {
        # "account_id": {"ZOHO_BOOKS": {"category": "INCOME"}},
        "bill_item.account_id": {"ZOHO_BOOKS": {"sub_category": "cost_of_goods_sold"}}, # purchase item
        "invoice_item.account_id": {"ZOHO_BOOKS": {"category": "INCOME"}},
    },
    "EXPENSES": {
        "contact_id": {"ZOHO_BOOKS": {"status": "ACTIVE", "contact_type": "VENDOR"}},
        "currency_id": {"ZOHO_BOOKS": {"is_base_currency": "true"}},
        "line_items.account_id":{
            "ZOHO_BOOKS": {
                "sub_category": "cost_of_goods_sold"
            }
        },
         "account_id":{ # TODO: passing account id in line items, why again passing ti in the main body? check
            "ZOHO_BOOKS": {
                "sub_category": "cost_of_goods_sold"
            }
        }
    },
    "PURCHASE_ORDERS": {
         "line_items.account_id":{
            "ZOHO_BOOKS": {
                "sub_category": "cost_of_goods_sold"
            }
        },
        "line_items.item_id": {"ZOHO_BOOKS": {"raw_data->>'item_type'": "sales_and_purchases"}},
        "line_items.tax_id": {
            "ZOHO_BOOKS": {
                "tax_type": "igst"
            }
        },
    },
    "SALES_ORDERS": {
         "line_items.account_id":{
            "ZOHO_BOOKS": {
                "sub_category": "cost_of_goods_sold"
            }
        },
        "line_items.item_id": {"ZOHO_BOOKS": {"raw_data->>'item_type'": "sales_and_purchases"}},
        "line_items.tax_id": {
            "ZOHO_BOOKS": {
                "raw_data ->> 'tax_type'": "tax_group",
                "raw_data->>'tax_specific_type'": "",
            }
        },
    },
}