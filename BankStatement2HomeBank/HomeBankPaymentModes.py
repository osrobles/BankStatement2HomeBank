#!/usr/bin/python3
"""
    HomeBank Payment Modes resources
    2022-11-20 19:05
"""

from enum import IntEnum


class PaymentModesEnum(IntEnum):
    """
    Payment modes enumerate
    """
    NONE = 0
    CREDIT_CARD = 1
    CHECK = 2
    CASH = 3
    BANK_TRANSFER = 4
    DEBIT_CARD = 6
    STANDING_ORDER = 7
    ELECTRONIC_PAYMENT = 8
    DEPOSIT = 9
    FIF = 10
    DIRECT_DEBIT = 11


paymentModes = {"Ninguno":  PaymentModesEnum.NONE.value,
                "Tarjeta de crédito": PaymentModesEnum.CREDIT_CARD.value,
                "Cheque": PaymentModesEnum.CHECK.value,
                "Efectivo": PaymentModesEnum.CASH.value,
                "Transferencia bancaria": PaymentModesEnum.BANK_TRANSFER.value,
                "Tarjeta de débito": PaymentModesEnum.DEBIT_CARD.value,
                "Orden de posición": PaymentModesEnum.STANDING_ORDER.value,
                "Pago electrónico": PaymentModesEnum.ELECTRONIC_PAYMENT.value,
                "Depósito": PaymentModesEnum.DEPOSIT.value,
                "FIF": PaymentModesEnum.FIF.value,
                "Cargo directo": PaymentModesEnum.DIRECT_DEBIT.value}


def getKeyList():
    """
    !@brief This function returns a list with the paymentModes dictionary keys

    @return paymentModes keys list
    """
    return list(paymentModes.keys())


def getValueList():
    """
    !@brief This function returns a list with the paymentModes dictionary values

    @return paymentModes values list
    """
    return list(paymentModes.values())
