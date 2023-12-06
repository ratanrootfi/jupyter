from fakeDataClass import fakeDataClass
import random

fakeData = fakeDataClass()
DEFAULT_DATAMODEL_CONFIG = {  # these are the default values we use for the write bodies. These get replace by the values in writeBodies
    "ACCOUNTS": {
        "sub_category": {
            "ZOHO_BOOKS": "long_term_liability",
            "ROOTFI_SANDBOX": "long_term_liability",
            "XERO":"LIABILITY",
            "QUICKBOOKS_SANDBOX":"CreditCard",
             "QUICKBOOKS":"CreditCard",
            "SAGE_CLOUD_ACCOUNTING":"CURRENT_LIABILITY",
            "WAFEQ":"CURRENT_LIABILITY",
            "NETSUITE":"AcctPay",
            "ODOO_ACCOUNTING":"liability_current",
            "WAVE":"CREDIT_CARD",
            "MEKARI_JURNAL":"Other Current Liabilities"
        }
    },
    "BANK_ACCOUNTS": {
        "category": {
            "ZOHO_BOOKS": "credit_card",  # bank and credit card supported
            "XERO":"BANK",
            "QUICKBOOKS_SANDBOX":"CashOnHand",
            "SAGE_CLOUD_ACCOUNTING":"CHECKING"
        }
    },
    "BANK_TRANSACTIONS": {
        "type": {"ZOHO_BOOKS": "deposit","XERO":"SPEND"},
        "raw_data": {
            # "ZOHO_BOOKS": {"from_account_id": ""},
            "XERO":{"from_account_id": ""},
            "MEKARI_JURNAL":{"deposit_to_id":"75365574"}
        },
    },
    "INVOICE_PAYMENTS": {
        "payment_mode": {"ZOHO_BOOKS": "cash","SAGE_CLOUD_ACCOUNTING":"ELECTRONIC","MEKARI_JURNAL":"Cash"},
        "raw_data":{
            "NETSUITE":{"arr_account_id":""}
        }
    },
    "BILL_PAYMENTS": {
        "payment_mode": {"ZOHO_BOOKS": "cash","SAGE_CLOUD_ACCOUNTING":"ELECTRONIC","MEKARI_JURNAL":"Cash"},
    },
    "ITEMS": {
        "type": {"ZOHO_BOOKS": "INVENTORY",
                 "XERO":"INVENTORY",
                "QUICKBOOKS_SANDBOX":"INVENTORY" ,
                "MS_DYNAMICS_365":"INVENTORY",
                "NETSUITE":"SERVICE",
                "ODOO_ACCOUNTING":"INVENTORY",
                "WAVE":"INVENTORY" ,
                "QUICKBOOKS":"INVENTORY"
                },
        "raw_data":{
            "XERO":{
                "inventory_asset_account_id":""
            },
            "QUICKBOOKS_SANDBOX":{
                "inventory_asset_account_id":""
            },
            "QUICKBOOKS":{
                "inventory_asset_account_id":""
            },
            "NETSUITE":{
                "taxschedule":"1"
            }
        }
    },
    "TAX_RATES": {
        "tax_type": {
            "ZOHO_BOOKS": "cgst",
            "MS_DYNAMICS_365": "VAT",
            "ODOO_ACCOUNTING":"sale"
        },
        "raw_data":{
            "MEKARI_JURNAL":{"buy_tax_account_id":"","sell_tax_account_id":""}
        }
    },
    "EXPENSES":{
        "payment_mode":{
            "QUICKBOOKS_SANDBOX":"CreditCard",
            "QUICKBOOKS":"CreditCard",
            "MEKARI_JURNAL":"Cash"
        },
        "raw_data":{
            "WAFEQ":{
                "description":fakeData.fakeDescription(),
                "paid_through_account_id":"acc_kdMKzKN59q26gzPQC9x478" 
            }
        }
    },
    "INVOICE_CREDIT_NOTES":{
        "raw_data":{
            "SAGE_CLOUD_ACCOUNTING":{
                "currency_rate":1
            }
        }
    },
    "BILL_CREDIT_NOTES":{
        "raw_data":{
            "SAGE_CLOUD_ACCOUNTING":{
                "currency_rate":1
            }
        }
    }
}

WRITE_BODIES = {
    "ACCOUNTS": {
        "nominal_code": fakeData.fakeDocumentNumber(),
        "name": fakeData.fakeName(),
        "description": fakeData.fakeDescription()[:30],
        "currency_id": "",
        "current_balance": fakeData.fakeAmount(),
        "sub_category": "",
        "parent_account_id": "",
    },
    "INVOICES": {
        "amount_due": 1,
        "total_discount": 1,
        "document_number": fakeData.fakeDocumentNumber(),
        "posted_date": "2023-08-01",
        "due_date": "2023-09-01",
        "currency_id": "",
        "currency_rate":1,
        "memo": fakeData.fakeDescription(),
        "sales_order_ids": [],
        "contact_id": "",
        "line_items": "",
    },
    "BILLS":{
        "document_number":fakeData.fakeDocumentNumber(),
         "posted_date": "2023-08-01",
        "due_date": "2023-09-01",             
        "currency_id":"",             
        "amount_due":1,              
        "currency_rate":1,           
        "purchase_order_ids":[],      
        "contact_id":"",              
        "memo":fakeData.fakeDescription(),                    
        "line_items":""
    },
    "LINE_ITEMS": [
        {
            "item_id": "",
            "tax_id": "",
            "description": fakeData.fakeDescription()[:40],
            "quantity": fakeData.fakeQuantity(),
            "unit_amount": fakeData.fakeAmount(),
            "account_id": "",
            "total_discount": 1,
            "tracking_category_ids": "",
        }
    ],
    "JOURNAL_ENTRIES": {
        "account_id": "",
        "amount": fakeData.fakeAmount(),
        "currency_id": "",
        "journal_entry_type": "",
        "description": fakeData.fakeDescription(),
        "posted_date": fakeData.fakePostedDate(),
        "document_number": fakeData.fakeDocumentNumber(),
        "journal_lines": "",
    },
    "JOURNAL_LINES": [
        {
            "description": fakeData.fakeDescription(),
            "type": "CREDIT",
            "account_id": "",
            "tax_id": "",
            "net_amount": 100,
            "contact_id": "",
            "tracking_category_ids": "",
        },
        {
            "description": fakeData.fakeDescription(),
            "type": "DEBIT",
            "account_id": "",
            "tax_id": "",
            "net_amount": 100,
            "contact_id": "",
            "tracking_category_ids": "",
        },
    ],
    "BANK_ACCOUNTS": {
        "institution_name": fakeData.fakeName(),
        "account_name": fakeData.fakeName(),
        "balance": fakeData.fakeAmount(),
        "currency_id": "",
        "account_number": fakeData.fakeBankAccountNumber(),
        "category": "",
    },
    "BANK_TRANSACTIONS": {
        "amount": fakeData.fakeAmount(),
        "type": "",
        "account_id": "",
        "to_account_id":"",
        "currency_id": "",
        "transaction_date": fakeData.fakePostedDate(),
        "contact_id": "",
        "raw_data": "",
    },
    "CONTACTS": {
        "name": fakeData.fakeName(),
        "contact_name": fakeData.fakeName(),
        "contact_type": random.choice(["CUSTOMER", "VENDOR"]),
        "currency_id": "",
        "tax_number": "ODSPS1279F",
        "registration_number": "07CEUPK5322M1XX",
        "email":fakeData.fakeEmailAddress(),
        "telephone":"4223874516",
        "mobile":"9835261738",
        "fax":fakeData.fakePhoneNumber(),
        "website":fakeData.fakeWebsite(),
        "contact_persons":"",
        "addresses":""
    },
    "INVOICE_PAYMENTS": {
        "invoice_id": "",
        "account_id": "",
        "amount": 1,
        "payment_mode": "cash",
        "currency_id": "",
        "memo": fakeData.fakeDescription(),
        "payment_date": fakeData.fakePostedDate(),
        "contact_id": "",
        "document_number": fakeData.fakeDocumentNumber(),
        "raw_data":""
    },
    "BILL_PAYMENTS": {
        "bill_id": "",
        "amount": 1,
        "payment_mode": "",
        "currency_id": "",
        "memo": fakeData.fakeDescription(),
        "payment_date": fakeData.fakePostedDate(),
        "account_id": "",
        "contact_id": "",
        "document_number": fakeData.fakeDocumentNumber(),
    },
    "INVOICE_CREDIT_NOTES": {
        "contact_id": "",
        "document_number": fakeData.fakeDocumentNumber(),
        "remaining_credit": 1,
        "posted_date": fakeData.fakePostedDate(),
        "currency_id": "",
        "memo": fakeData.fakeDescription(),
        "invoice_ids": "",
        "line_items": "",
        "raw_data": ""
    },
    "BILL_CREDIT_NOTES": {
        "contact_id": "",
        "document_number": fakeData.fakeDocumentNumber(),
        "remaining_credit": 1,
        "posted_date": fakeData.fakePostedDate(),
        "currency_id": "",
        "memo": fakeData.fakeDescription(),
        "bill_ids": "",
        "line_items": "",
        "raw_data":""
    },
    "ITEMS": {
        "name": fakeData.fakeName(),
        "description": fakeData.fakeDescription(),
        "bill_item": {
            "unit_price": fakeData.fakeAmount(),
            "account_id": "",
            # "tax_id": "",
            "description": fakeData.fakeDescription(),
        },
        "code": fakeData.fakeDocumentNumber(),
        "invoice_item": {
            "unit_price": fakeData.fakeAmount(),
            "account_id": "",
            # "tax_id": "",
            "description": fakeData.fakeDescription(),
        },
        "is_bill_item": False,
        "is_invoice_item":True,
        "type": "",
        "quantity_on_hand": fakeData.fakeQuantity(),
        "raw_data": "",
    },
    "TAX_RATES": {
        "name": fakeData.fakeName(),
        "code": fakeData.fakeDocumentNumber(),
        "components": [{
            "name": fakeData.fakeName(),
            "rate": fakeData.fakePercentage(),
            "is_compound":False,
            # these below should in raw_data?
            "tax_agency": "1",
            "tax_applicable_on": "Sales",
        }],
        "effective_tax_rate": fakeData.fakePercentage(),
        "total_tax_rate": fakeData.fakePercentage(),
        "tax_type": "",
        "raw_data":""

    },
    "EXPENSES": {
        "document_number": fakeData.fakeDocumentNumber(),
        "currency_id": "",
        "memo": str(fakeData.fakeDescription())[:40],
        "account_id": "",
        "payment_mode": "",
        "posted_date": fakeData.fakePostedDate(),
        "contact_id": "",
        "line_items": "",
        "raw_data":""
    },
    "PURCHASE_ORDERS": {
        "description": "",
        "payment_mode": "",
        "delivery_date": fakeData.fakeDeliveryDate(),
        "bill_ids": "",
        "currency_id": "",
        "document_number": fakeData.fakeDocumentNumber(),
        "posted_date": fakeData.fakePostedDate(),
        "contact_id": "",
        "line_items": "",
    },
    "SALES_ORDERS": {
        "posted_date": fakeData.fakePostedDate(),
        "description": fakeData.fakeDescription(),
        "currency_id": "",
        "invoice_ids": "",
        "delivery_date": fakeData.fakeDeliveryDate(),
        "document_number": fakeData.fakeDocumentNumber(),
        "contact_id": "",
        "line_items": "",
    },
    "ADDRESSES":[{
        "type": "SHIPPING",
        "street": fakeData.fakeStreet(),
        "locality": fakeData.fakeLocality(),
        "city": fakeData.fakeCity(),
        "state": "US-AK",
        "country": "US",
        "pincode": fakeData.fakePincode(),
    },
    {
        "type": "BILLING",
        "street": fakeData.fakeStreet(),
        "locality": fakeData.fakeLocality(),
        "city": fakeData.fakeCity(),
        "state": "US-AK",
        "country": "US",
        "pincode": fakeData.fakePincode(),
    }
    ]
}
