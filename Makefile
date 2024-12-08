run-backend: refresh-subtree
	docker-compose up --build

refresh-subtree:
	rm -rf stock_scraper/*
	git clone https://github.com/darkshloser/stockanalysis-scraper.git stock_scraper

