import math

def annuity_to_lump_sum(face_value, discount=0.0):
    return face_value * (1 - discount)

def after_tax(amount, tax_rate):
    return amount * (1 - tax_rate)
