from flask import request, jsonify
from ..schemas.receipt import Receipt
from pydantic import ValidationError

class ReceiptController:
    """
    This class represents the controller that interprets a set of requests related to receipts and takes the appropriate action. 
    """
    def __init__(self, service):
        """
        Initializes the ReceiptController with the given service instance.

        Parameters:
        -----------
        service : object
            The receipt service instance that the controller interacts with.
        """
        self.service = service

    def process_receipt(self):
        """
        Processes the receipt received in the body of the request and returns the ID associated with the receipt.

        Returns
        ----------
        JSON response the ID of the receipt and HTTP Status code 200 if successful. 
        
        JSON response with the errors and HTTP Status code 400 if the request is invalid.
        """
        data = request.json
        try:
            receipt = Receipt(**data)
            id = self.service.process_receipt(receipt)
            return jsonify({"id": id}), 200
        except ValidationError as e:
            errors = []
            for error in e.errors():
                errors.append(error['msg'])
            return jsonify({"description": "The receipt is invalid.", 
                            "error": errors}), 400

    def get_points(self, id: str):
        """
        Retrieves the points for the given receipt ID. 

        Parameters
        ----------
        id : str
            The receipt ID
        
        Returns
        ----------
        JSON response with HTTP Status code 200 if successful. 
        
        JSON response with HTTP Status code 404 if the receipt ID is not found.
        """
        try:
            points = self.service.get_points(id)
            return jsonify({"points": points}), 200
        except ValueError:
            return jsonify({"description": "No receipt found for that ID"}), 404
        


