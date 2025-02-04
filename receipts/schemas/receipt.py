from pydantic import field_validator, Field, BaseModel, model_validator
from pydantic.dataclasses import dataclass
from typing import List
from .item import Item
from datetime import datetime, time
import re

class Receipt(BaseModel):
    """
    This class represents a receipt with items.
    """
    retailer: str
    purchaseDate: datetime
    purchaseTime: time
    items: List[Item] = Field(min_length=1)
    total: float

    @model_validator(mode="before")
    @classmethod
    def validate_before(cls, values):
        if isinstance(values, dict):
            for field_name, value in values.items():
                if value in [None, ""]:
                    raise ValueError(f"Field '{field_name}' cannot be empty")
        return values

    # purchaseDate should be in the format 'YYYY-MM-DD'
    @field_validator("purchaseDate", mode="before")
    def validate_purchaseDate(value: str):
        try:
            date = datetime.strptime(value,'%Y-%m-%d')
            return date
        except:
            raise ValueError("Purchase Date must be a string in the format 'YY-MM-DD'")
    
    # purchaseTime should be in the format 'HH:MM'
    @field_validator("purchaseTime", mode="before")
    def validate_purchaseTime(value: str):
        try:
            time = datetime.strptime(value, '%H:%M').time()
            return time
        except:
            raise ValueError("Purchase Time must be a string in the format 'HH:MM'")
    
    # total should be a valid float value
    @field_validator("total", mode="before")
    def validate_price(value):
        if not isinstance(value, str) or not re.match(r"^\d+\.\d{2}$", value):
            raise ValueError("Receipt total must be a valid numeric string with two decimal places")
        try:
            return float(value)
        except:
            raise ValueError("Receipt total must be a valid numeric string with two decimal places")
    

    
