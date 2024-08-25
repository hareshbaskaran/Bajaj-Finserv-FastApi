from pydantic import BaseModel, Field, validator
from fastapi import FastAPI, HTTPException
from typing import List, Union


# Schema Validator - Pydantic
class BFHLRequest(BaseModel):
    data: List[Union[str, int]] = Field(
        ..., min_items=1, description="User request data"
    )

    @validator("data", each_item=True)
    def validate_items(cls, item):
        if item is None:
            raise ValueError("None values are not allowed in this request")

        if isinstance(item, str):
            if len(item) == 0:
                raise ValueError("Empty strings are not allowed")

            if not item.isdigit() and not item.isalpha():
                raise ValueError("Only alphabets or numeric strings are allowed")

            if len(item) > 1 and not item.isdigit():
                raise ValueError(
                    "Only single-character strings or number allowed"
                )

        return item

    @validator("data")
    def validate_data(cls, data):
        if not data:
            raise ValueError("Data list cannot be empty")

        return data
