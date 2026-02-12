from e_store.address import Address
from e_store.credit_card_information import CreditCardInformation


class BillingInformation:
    receiver_name: str
    receiver_phone: str
    delivery_date: Address
    credit_card_information: CreditCardInformation