from e_store.card_type import CardType


class CreditCardInformation:
    card_number: str
    name_on_card: str
    cvv: str
    expiry_month: int
    expiry_year: int
    card_type = CardType
