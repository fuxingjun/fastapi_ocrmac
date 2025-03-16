from fastapi import FastAPI

from app.views import ocr

app = FastAPI()

# 将路由器挂载到主应用
app.include_router(ocr.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5008, log_level="info", reload=True, timeout_keep_alive=60)
