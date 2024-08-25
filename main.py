from fastapi import FastAPI
from models.model import BFHLRequest
from models.schema import BFHLResponse, BFHLGetResponse
from enums.constants import USER_ID, EMAIL, ROLL_NUMBER, OPERATION_CODE


app = FastAPI()

## Check connection with hosting service
## localhost - port:8080


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/health")
def health():
    return {"Api is up and running"}


### post method


@app.post("/bfhl")
async def bfhl_post(request: BFHLRequest):
    numbers = []
    alphabets = []
    highest_lowercase = []

    # Process data to segregate numbers and alphabets
    for item in request.data:
        if isinstance(item, str) and item.isalpha():
            alphabets.append(item)
        elif isinstance(item, (str, int)) and str(item).isdigit():
            numbers.append(str(item))

    # Determine the highest lowercase alphabet
    lowercase_alphabets = [char for char in alphabets if char.islower()]
    if lowercase_alphabets:
        highest_lowercase.append(max(lowercase_alphabets))

        # Create the response
    response = BFHLResponse(
        is_success=True,
        user_id=USER_ID,
        email=EMAIL,
        roll_number=ROLL_NUMBER,
        numbers=numbers,
        alphabets=alphabets,
        highest_lowercase_alphabet=highest_lowercase,
    )
    return response


## get method


@app.get("/bfhl", response_model=BFHLGetResponse)
async def bfhl_get():
    return BFHLGetResponse(operation_code=OPERATION_CODE)
