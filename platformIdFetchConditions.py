PLATFORM_ID_FETCH_CONDITIONS = {
    "ACCOUNTS": {  ## datamodel we are querying for
        "currency_id": {  ## field we are querying on
            "ZOHO_BOOKS": {
                "is_base_currency": "true",  ## condition we are querying for - key is column name, value is the condition value
            }
        },
    },
    "BILLS":{
        "contact_id":{
            "ZOHO_BOOKS":{
                "contact_type":"VENDOR"
            },
            "ROOTFI_SANDBOX":{
                "contact_type":"VENDOR"
            },
            "XERO":{
                "contact_type":"VENDOR"
            },
            "QUICKBOOKS_SANDBOX":{
                "contact_type":"VENDOR"
            },
            "SAGE_CLOUD_ACCOUNTING":{
                "contact_type":"VENDOR"
            },
            "WAFEQ":{
                "contact_type":"VENDOR"
            },
            "NETSUITE":{
                "contact_type":"VENDOR"
            },
            "ODOO_ACCOUNTING":{
                "contact_type":"VENDOR"
            },
        },
        "line_items.account_id": {
            "ZOHO_BOOKS": {
                "sub_category": "other_current_liability"
            },
            "SAGE_CLOUD_ACCOUNTING":{
                # "sub_category":"CURRENT_ASSETS",
                "platform_id":"fea140d5917811eda8c40ef4cf562701" # TODO: figure out condition
            }
        },
        "line_items.tax_id": {
            "ZOHO_BOOKS": {
                # "raw_data ->> 'tax_type'": "tax_group"
                "tax_type": "igst"
            },
            "MS_DYNAMICS_365":{
                # "tax_type":"VAT"
                "platform_id":"STANDARD" # TODO: figure out condition
            },
            "ODOO_ACCOUNTING":{
                "tax_type":"none"
            }
        },
        "line_items.item_id": {
            "ZOHO_BOOKS": {
                "is_bill_item": "true",
                "is_invoice_item": "true",
            }
        }
    },
    "INVOICES": {
        "currency_id": {
            "ZOHO_BOOKS": {
                "is_base_currency": "true"
            }
        },
        "contact_id": {
            "ZOHO_BOOKS": {
                "contact_type": "CUSTOMER",
                "status": "ACTIVE"
            },
            "SAGE_CLOUD_ACCOUNTING":{
                "contact_type": "CUSTOMER"
            },
            "NETSUITE":{
                "contact_type": "CUSTOMER"
            }
        },
        "line_items.tax_id": {
            "ZOHO_BOOKS": {
                # "raw_data ->> 'tax_type'": "tax_group"
                "tax_type": "igst"
            },
            "MS_DYNAMICS_365":{
                # "tax_type":"VAT"
                "platform_id":"STANDARD" # TODO: figure out condition
            },
            "ODOO_ACCOUNTING":{
                "tax_type":"none"
            },
            "SAGE_CLOUD_ACCOUNTING":{
                "name":"No Tax"
            }
        },
        "line_items.account_id": {
            "ZOHO_BOOKS": {
                "sub_category": "other_current_liability"
            },
            "XERO":{
                "sub_category":"REVENUE"
            },
            "SAGE_CLOUD_ACCOUNTING":{
                "sub_category":"SALES"
            },
            "ODOO_ACCOUNTING":{
                "platform_id":"122"
            }
        },
        "line_items.tracking_category_ids":{
            "XERO":{
                "has_children":"false"
            }
        },
        "line_items.item_id":{
            "QUICKBOOKS_SANDBOX": {
                "type":"INVENTORY"
            }
        },
    },
    "BANK_ACCOUNTS": {
        "currency_id": {
            "ZOHO_BOOKS": {
                "is_base_currency": "true"
            },
            "SAGE_CLOUD_ACCOUNTING":{
                "platform_id":"USD"
            }
        },
    },
    "BANK_TRANSACTIONS": {
        "to_account_id": {
            "ZOHO_BOOKS": {
                "sub_category": "bank"
            }
        },  # only for bank transactions type deposit 
        "account_id": {
            "ZOHO_BOOKS": {
                "sub_category": "cash"
            }
        },
        "raw_data.from_account_id": {
            # "ZOHO_BOOKS": {
            #     "sub_category": "cash"
            # },
            "XERO":{
                "sub_category":"CURRLIAB"
            }
        },  # only for bank transactions type deposit 
        "contact_id": {
            "ZOHO_BOOKS": {
                "status": "ACTIVE", "contact_type": "CUSTOMER"
            }
        },
    },
    "CONTACTS": {
        "currency_id": {
            "ZOHO_BOOKS": {
                "is_base_currency": "true"
            },
            "SAGE_CLOUD_ACCOUNTING":{
                "platform_id":"USD"
            },
             "ODOO_ACCOUNTING": {
                "is_base_currency": "true"
            },
        },
    },
    "INVOICE_PAYMENTS": {
        "account_id": {
            "ZOHO_BOOKS": {
                "sub_category": "bank"
            },
            "QUICKBOOKS_SANDBOX":{
                "sub_category":"CashOnHand"
            },
            "ODOO_ACCOUNTING":{
                "sub_category":"asset_receivable"
            }
        },
        "raw_data.arr_account_id":{
            "NETSUITE":{
                "sub_category":"AcctRec"
            }
        }
    },
    "BILL_PAYMENTS": {
        "account_id": {
            "ZOHO_BOOKS": {
                "sub_category": "bank"
            },
            "QUICKBOOKS_SANDBOX":{
                "sub_category":"CashOnHand"
            },
            "ODOO_ACCOUNTING":{
                "sub_category":"asset_receivable"
            }
        }
    },
    "INVOICE_CREDIT_NOTES": {
        "line_items.tax_id": {
            "ZOHO_BOOKS": {
                # "tax_type": "igst",
                "raw_data ->> 'tax_type'": "tax_group"
            },
            "MS_DYNAMICS_365":{
                # "tax_type":"VAT"
                "platform_id":"STANDARD" # TODO: figure out condition
            }
        },
        "line_items.account_id":{
            "ZOHO_BOOKS": {
                "sub_category": "cost_of_goods_sold"
            },
            "SAGE_CLOUD_ACCOUNTING":{
                "sub_category":"SALES"
            }
        },
        "line_items.item_id":{
            "QUICKBOOKS_SANDBOX": {
                "type":"INVENTORY"
            },
        }
    },
    "BILL_CREDIT_NOTES": {
        "line_items.item_id": {
            "ZOHO_BOOKS": {
                "raw_data->>'item_type'": "sales_and_purchases"
            },
            "QUICKBOOKS_SANDBOX": {
                "type":"INVENTORY"
            },
        },
        "line_items.tax_id": {
            "ZOHO_BOOKS": {
                "tax_type": "igst"
            }
        },
        "line_items.account_id":{
            "ZOHO_BOOKS": {
                "sub_category": "cost_of_goods_sold"
            },
            "SAGE_CLOUD_ACCOUNTING":{
                "platform_id":"fea140d5917811eda8c40ef4cf562701" # TODO: figure out condition
            }
        }
    },
    "ITEMS": {
        # "account_id": {"ZOHO_BOOKS": {"category": "INCOME"}},
        "bill_item.account_id": { # purchase item
            "ZOHO_BOOKS": {
                "sub_category": "cost_of_goods_sold"
            },
            "XERO":{
                "sub_category":"EXPENSE"
            },
            "QUICKBOOKS_SANDBOX": {
                "sub_category":"SuppliesMaterialsCogs"
            },
            "SAGE_CLOUD_ACCOUNTING":{
                "platform_id":"fea140d5917811eda8c40ef4cf562701"  # TODO: figure out condition
            },
            "NETSUITE":{
                "sub_category":"Expense"
            },
            "MEKARI_JURNAL":{
                "sub_category":"Income"
            }
        }, 
        "invoice_item.account_id": {
            "ZOHO_BOOKS": {
                "category": "INCOME"
            },
            "XERO":{
                "sub_category":"EQUITY"
            },
            "QUICKBOOKS_SANDBOX":{
                "sub_category":"SalesOfProductIncome"
            },
            "SAGE_CLOUD_ACCOUNTING":{
                "sub_category":"SALES"
            },
            "NETSUITE":{
                "sub_category":"Income"
            },
            "MEKARI_JURNAL":{
                "sub_category":"Cost of Sales"
            }
        },
        "raw_data.inventory_asset_account_id":{
            "XERO":{
                "sub_category":"INVENTORY"
            },
            "QUICKBOOKS_SANDBOX":{
                "sub_category":"Inventory"
            }
        }
    },
    "EXPENSES": {
        "contact_id": {
            "ZOHO_BOOKS": 
                {
                    "status": "ACTIVE", "contact_type": "VENDOR"
                },
            "SAGE_CLOUD_ACCOUNTING": {
                    "platform_id": "587ef01ea74c4a36a5f64d0d16d178ac" # TODO: figure out condition
                    # "contact_type": "VENDOR"
                
                }
            },
        "currency_id": {
            "ZOHO_BOOKS": {
                "is_base_currency": "true"
            }
        },
        "line_items.account_id":{
            "ZOHO_BOOKS": {
                "sub_category": "cost_of_goods_sold"
            },
            "QUICKBOOKS_SANDBOX":{
                "sub_category":"CashOnHand"            
            },
            "MEKARI_JURNAL":{
                "sub_category":"Cost of Sales"
            }
        },
         "account_id":{ # TODO: passing account id in line items, why again passing ti in the main body? check
            "ZOHO_BOOKS": {
                "sub_category": "cost_of_goods_sold"
            },
            "QUICKBOOKS_SANDBOX":{
                "sub_category":"CashOnHand"
            }
        },
        "line_items.item_id": {
            "QUICKBOOKS_SANDBOX": {
                "type":"INVENTORY"
            }
        },
        "raw_data.paid_through_account_id":{
            "WAFEQ":{
                "sub_category":"CURRENT_ASSET"
            }
        }
    },
    "PURCHASE_ORDERS": {
         "line_items.account_id":{
            "ZOHO_BOOKS": {
                "sub_category": "cost_of_goods_sold"
            },
             "QUICKBOOKS_SANDBOX":{
                "sub_category":"CashOnHand"
            }
        },
        "line_items.item_id": {
            "ZOHO_BOOKS": {
                "raw_data->>'item_type'": "sales_and_purchases"
            },
            "QUICKBOOKS_SANDBOX": {
                "type":"INVENTORY"
            }
        },
        "line_items.tax_id": {
            "ZOHO_BOOKS": {
                "tax_type": "igst"
            },
             "MS_DYNAMICS_365":{
                # "tax_type":"VAT"
                "platform_id":"STANDARD" # TODO: figure out condition
            }
        },
    },
    "SALES_ORDERS": {
         "line_items.account_id":{
            "ZOHO_BOOKS": {
                "sub_category": "cost_of_goods_sold"
            },
            "XERO":{
                "sub_category":"REVENUE"
            },
             "QUICKBOOKS_SANDBOX":{
                "sub_category":"CashOnHand"
            }
        },
        "line_items.item_id": {
            "ZOHO_BOOKS": {
                "raw_data->>'item_type'": "sales_and_purchases"
            },
            "QUICKBOOKS_SANDBOX": {
                "type":"INVENTORY"
            }
        },
        "line_items.tax_id": {
            "ZOHO_BOOKS": {
                "raw_data ->> 'tax_type'": "tax_group",
                "raw_data->>'tax_specific_type'": "",
            },
             "MS_DYNAMICS_365":{
                # "tax_type":"VAT"
                "platform_id":"STANDARD" # TODO: figure out condition
            }
        },
    },
    "JOURNAL_ENTRIES":{
        "journal_lines.account_id":{
            "XERO":{
                "sub_category":"REVENUE"
            },
            "MS_DYNAMICS_365":{
                "platform_id":"22f3d74d-c32f-ee11-bdfa-6045bdacd6c5" # TODO: figure out condition
            }
        }
    },
    "TAX_RATES":{
        "raw_data.buy_tax_account_id":{
            "MEKARI_JURNAL":{
                "sub_category":"Other Current Assets"
            }
        },
        "raw_data.sell_tax_account_id":{
            "MEKARI_JURNAL":{
                "sub_category":"Other Current Liabilities"
            }
        }
    }
}


CUSTOM_TABLE_FETCH_CONDITIONS = {
    "EXPENSES":{
        "account_id":{
            "SAGE_CLOUD_ACCOUNTING": "bank_accounts"
        }
    },
    "INVOICE_PAYMENTS":{
        "account_id":{
            "SAGE_CLOUD_ACCOUNTING": "bank_accounts"
        }
    },
    "BILL_PAYMENTS":{
        "account_id":{
            "SAGE_CLOUD_ACCOUNTING": "bank_accounts"
        }
    }
}