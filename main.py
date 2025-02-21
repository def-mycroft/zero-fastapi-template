import yaml
import logging
from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from api.endpoints import router as api_router

# Load configuration
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

app = FastAPI(title="template API app", version=config["api"]["version"])

# Enable gzip compression for responses larger than 1KB
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Include the API router with our endpoints
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config["server"]["host"], port=config["server"]["port"])
