from flask import Blueprint
from .controllers.receipt_controller import ReceiptController
from .services.receipt_service import ReceiptService

receipts_blueprint = Blueprint("receipts", __name__)
controller = ReceiptController(ReceiptService())

receipts_blueprint.add_url_rule("/process", None, controller.process_receipt, methods=['POST'])
receipts_blueprint.add_url_rule("<string:id>/points", None, controller.get_points, methods=['GET'])

        

    

    
