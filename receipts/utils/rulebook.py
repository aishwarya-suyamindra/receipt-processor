from ..schemas.receipt import Receipt
from .util import count_alphanumeric_characters
import math
from datetime import time

# constants 
ROUND_DOLLAR_POINTS = 50
MULTIPLE_POINTS = 25
TWO_ITEM_POINTS = 5
ODD_PURCHASE_DATE_POINTS = 6 
PURCHASE_TIME_POINTS = 10
ITEM_DESC_POINTS = 0.2
ALPHANUMERIC_CHARACTER_POINTS = 1

def calculate_points(receipt: Receipt) -> int:
    """
    Calculates and returns the points for the given receipt.

    Parameters
    ----------
    receipt: Receipt
        The receipt to calculate points for
        
    Returns
    ----------
    int
        The points for the receipt
    """
    points = 0

    # alphanumeric characters 
    points += (ALPHANUMERIC_CHARACTER_POINTS * count_alphanumeric_characters(receipt.retailer))

    # points if the total is a round dollar
    if receipt.total == int(receipt.total):
        points += ROUND_DOLLAR_POINTS
    
    # points if the total is a multiple of 0.25
    if receipt.total % 0.25 == 0:
        points += MULTIPLE_POINTS
    
    # points for every two items on the receipt 
    points += TWO_ITEM_POINTS * (len(receipt.items) // 2)

    # item points based on the description
    for item in receipt.items:
        if len(item.shortDescription.strip()) % 3 == 0:
            points += int(math.ceil(item.price * ITEM_DESC_POINTS))
    
    # points for odd purchase date
    if receipt.purchaseDate.day % 2:
        points += ODD_PURCHASE_DATE_POINTS
    
    # points for purchase time - excludes boundary values
    if time(14, 0) < receipt.purchaseTime < time(16, 0):
        points += PURCHASE_TIME_POINTS
    
    return points

        



        
        

        
        
        