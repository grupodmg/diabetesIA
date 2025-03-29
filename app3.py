from fastapi import FastAPI, HTTPException
from routers import routerPredictions

app = FastAPI()
app.include_router(routerPredictions.router)

if __name__=="__main__":
    app:run()