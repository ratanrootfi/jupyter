from fakeDataClass import fakeDataClass
import random

fakeData = fakeDataClass()
DEFAULT_DATAMODEL_CONFIG = {  # these are the default values we use for the write bodies. These get replace by the values in writeBodies
    "ACCOUNTS": {
        "sub_category": {
            "ZOHO_BOOKS": "long_term_liability",
            "ROOTFI_SANDBOX": "long_term_liability",
        }
    },
    "BANK_ACCOUNTS": {
        "category": {
            "ZOHO_BOOKS": "credit_card",  # bank and credit card supported
        }
    },
    "BANK_TRANSACTIONS": {
        "type": {"ZOHO_BOOKS": "deposit"},
        "raw_data": {"ZOHO_BOOKS": {"from_account_id": ""}},
    },
    "INVOICE_PAYMENTS": {
        "payment_mode": {"ZOHO_BOOKS": "cash"},
    },
    "BILL_PAYMENTS": {
        "payment_mode": {"ZOHO_BOOKS": "cash"},
    },
    "ITEMS": {
        "type": {"ZOHO_BOOKS": "INVENTORY"}
    },
    "TAX_RATES": {"tax_type": {"ZOHO_BOOKS": "cgst"}},

}

WRITE_BODIES = {
    "ACCOUNTS": {
        "nominal_code": fakeData.fakeDocumentNumber(),
        "name": fakeData.fakeName(),
        "description": fakeData.fakeDescription(),
        "currency_id": "",
        "current_balance": fakeData.fakeAmount(),
        "sub_category": "",
        "parent_account_id": "",
    },
    "INVOICES": {
        "amount_due": 1,
        "document_number": fakeData.fakeDocumentNumber(),
        "posted_date": "2023-01-01",
        "due_date": "2023-02-01",
        "currency_id": "",
        "memo": fakeData.fakeDescription(),
        "sales_order_ids": [],
        "contact_id": "",
        "line_items": "",
    },
    "LINE_ITEMS": [
        {
            "item_id": "",
            "tax_id": "",
            "description": fakeData.fakeDescription(),
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
        "account_number": "",
        "category": "",
    },
    "BANK_TRANSACTIONS": {
        "amount": fakeData.fakeAmount(),
        "type": "",
        "account_id": "",
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
    },
    "TAX_RATES": {
        "name": fakeData.fakeName(),
        "code": fakeData.fakeDocumentNumber(),
        "components": "",
        "effective_tax_rate": fakeData.fakePercentage(),
        "total_tax_rate": fakeData.fakePercentage(),
        "tax_type": "",

    },
    "EXPENSES": {
        "document_number": fakeData.fakeDocumentNumber(),
        "currency_id": "",
        "memo": fakeData.fakeDescription(),
        "account_id": "",
        "payment_mode": "",
        "posted_date": fakeData.fakePostedDate(),
        "contact_id": "",
        "line_items": "",
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
}
