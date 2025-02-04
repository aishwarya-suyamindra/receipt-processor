from pydantic import field_validator, BaseModel, Field, model_validator
import re

class Item(BaseModel):
    """
    This class represents a single item in a receipt.
    """
    shortDescription: str = Field(description="Short description cannot be null")
    price: float

    @model_validator(mode="before")
    @classmethod
    def validate_before(cls, values):
        if isinstance(values, dict):
            for field_name, value in values.items():
                if value in [None, ""]:
                    raise ValueError(f"Field '{field_name}' cannot be empty")
        return values
    
    @field_validator("price", mode="before")
    def validate_price(value):
        if not isinstance(value, str) or not re.match(r"^\d+\.\d{2}$", value):
            raise ValueError("Item price must be a valid numeric string with two decimal places")
        try:
            return float(value)
        except:
            raise ValueError("Receipt total must be a valid numeric string with two decimal places")