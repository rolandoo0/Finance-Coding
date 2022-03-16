def Perpetuity_without_Growth(
    startDate: int, frequency: int, intrate: float, payment: int
):
    """
    Calculates the present value of a perpetuity without growth.\n
    startDate is the number of years from the present that the perpetuity starts.\n
    frequency is the number of years between payments.\n
    intrate is the interest rate in decimal form.\n
    payment is the amount of the payment.
    """
    firstCashflow = payment / ((1 + intrate) ** startDate)
    secondCashflow = payment / ((1 + intrate) ** (startDate + frequency))
    thirdCashflow = payment / ((1 + intrate) ** (startDate + frequency * 2))
    rate = secondCashflow / firstCashflow
    PresentValue = firstCashflow / (1 - rate)
    return PresentValue


def Perpetuity_with_Growth(
    startDate: int, frequency: int, intrate: float, growthRate: float, payment: int
):
    """
    Calculates the present value of a perpetuity with growth.\n
    startDate: the number of years from the present that the perpetuity with growth starts.\n
    frequency: the number of years between payments.\n
    intrate: the interest rate in decimal form.\n
    growthRate: the growth rate in decimal form.\n
    payment: the amount of the payment.\n\n

    **Note:** This function assumes that the first cashflow does not have the growth rate included since the growth begins in that year.
    """
    firstCashflow = payment / ((1 + intrate) ** startDate)
    secondCashflow = (payment * (1 + growthRate)) / (
        (1 + intrate) ** (startDate + frequency)
    )
    rate = secondCashflow / firstCashflow
    PresentValue = firstCashflow / (1 - rate)
    return PresentValue
