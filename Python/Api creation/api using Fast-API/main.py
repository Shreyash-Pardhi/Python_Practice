from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read():
    return {"first": "apis"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)