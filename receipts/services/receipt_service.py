
from ..schemas.receipt import Receipt
from ..schemas.item import Item
from typing import Dict
from ..utils.rulebook import calculate_points
from ..utils.util import generate_id

class ReceiptService():
    """
    This class represents a receipt processor which can perform a set of operations on receipts.
    It is given by a collection of receipts.
    """

    def __init__(self):
        self.receipts: Dict[str: int] = {} # map receipt ids to the calculated points 
    
    def get_points(self, id: str) -> int:
        """
        Returns the points for a given valid receipt ID.

        Parameters
        ----------
        id : str
            The receipt ID

        Raises
        ------
        ValueError
            If the receipt ID is not found.
        """
        if id not in self.receipts:
            raise ValueError("Invalid receipt ID")
        return self.receipts[id]
    
    def process_receipt(self, data: Receipt) -> str:
        """
        Processes the given receipt and calculates the points to award.
        Returns a unique ID for the receipt.

        Parameters
        ----------
        data : Receipt
            The receipt to process
        """
        total_points = calculate_points(data)
        receipt_id = generate_id()
        self.receipts[receipt_id] = total_points
        return receipt_id
