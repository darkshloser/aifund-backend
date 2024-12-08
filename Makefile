run-backend: refresh-subtree
	docker-compose up --build

refresh-subtree:
	git subtree pull --prefix=stock_scraper https://github.com/darkshloser/stockanalysis-scraper.git master


