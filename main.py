from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def helloworld():
    return {"msg": "Hello world!"}