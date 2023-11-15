import fastapi
from pydantic import BaseModel


class Message(BaseModel):
    message: str


app = fastapi.FastAPI()


@app.get("/")
async def greet_readers() -> Message:
    return Message(message="Welcome to my awesome presentation!")
