from fastapi import FastAPI

app = FastAPI() # The "brain" of your API

@app.get("/") # The "address" or route
def home():
    return {"message": "FastAPI is running!"}