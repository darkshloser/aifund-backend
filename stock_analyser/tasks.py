from celery import shared_task
from django.utils import timezone
from datetime import time
from stock_scraper.stockanalysis_scraper.src.stockanalysis_scraper.scraper.scraper import StockAnalysis
from .models import PreMarketGainer

@shared_task
def update_premarket_gainers():
    # import rpdb
    # dbg = rpdb.Rpdb(port=12345)
    # dbg.set_trace()
    analysis = StockAnalysis(headless=True, sendbox=True)
    gainers = analysis.scrape_premarket_gainers()
    print("______________________________", flush=True)
    print(gainers, flush=True)

    # now = timezone.localtime(timezone.now()).time()
    # # Check if current time is between 9:00 and 15:00 local time
    # if time(9, 0) <= now <= time(15, 0):
    #     gainers = get_pre_market_gainers()  # Assuming this returns a list of tuples (ticker, name, price, change)
        
    #     # Clear old records and store the new top gainers
    #     PreMarketGainer.objects.all().delete()
    #     for g in gainers:
    #         ticker, name, price, change = g
    #         PreMarketGainer.objects.create(
    #             ticker=ticker, 
    #             name=name, 
    #             price=price, 
    #             change=change
            # )
