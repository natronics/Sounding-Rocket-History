
build:
	./build_site.py
	jekyll

clean:
	rm -rf year/_posts/*
	rm -rf launch-vehicle/_posts/*
	rm -rf location/_posts/*

regendb:
	rm -rf database/db_repository
	rm -rf database/sounding-rocket-history.db
	./manage.py --create
	./manage.py --migrate
