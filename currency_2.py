# My second attempt at this project. I had a much better grasp on the


rates = [("USD", "EUR", 0.74)]
value = 1
current = "USD"
to = "EUR"


def convert(rates, value, current, to):
    """
    This function will serve to convert currencies
    """
    if rates == []:
        return value

    currency = value * rates[0][2]
    print(currency)


convert([("USD", "EUR", 0.74)], 10, "USD", "EUR")


def convert(rates, value, current, to):
    """
    This function will serve to to convert USD to
    """
    if rates == []:
        return value

    currency = value / rates[0][2]
    print(currency)
