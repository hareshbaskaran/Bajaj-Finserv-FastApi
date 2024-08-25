from pydantic import BaseModel, EmailStr
from typing import List


class BFHLResponse(BaseModel):
    is_success: bool
    user_id: str
    email: EmailStr
    roll_number: str
    numbers: List[str]
    alphabets: List[str]
    highest_lowercase_alphabet: List[str]


class BFHLGetResponse(BaseModel):
    operation_code: int
