run-backend: refresh-subtree
	docker-compose up --build

refresh-subtree:
    
	rm -rf stock_scraper || true
	# mkdir stock_scraper
	git subtree add --prefix=stock_scraper https://github.com/darkshloser/stockanalysis-scraper.git master



