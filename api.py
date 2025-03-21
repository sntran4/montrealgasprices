from fastapi import FastAPI
from scraper import scrape_montreal_gas_prices

app = FastAPI()


@app.get("/")
async def gas_prices():
    return scrape_montreal_gas_prices()