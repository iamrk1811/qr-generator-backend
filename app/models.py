from pydantic import BaseModel


# Define the input schema for the request
class SpaceQRRequest(BaseModel):
    url: str
    extra: str
