from fastapi import FastAPI

# 1. Create the 'app' instance
app = FastAPI()

# 2. Define a standard function with a decorator
@app.get("/")
def say_hello():
    return {"message": "Hello World"}

# 3. A function with a parameter (uses standard type hints)
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}