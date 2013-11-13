
build:
	./build_site.py
	jekyll

clean:
	rm -f year/_posts/*
	rm -f launch-vehicle/_posts/*
	rm -f location/_posts/*
	rm -f data/launch-vehicle/*
	rm -f data/location/*

regendb:
	rm -f database/sounding-rocket-history.db
	rm -f database/alembic/versions/*.py
	rm -f database/alembic/versions/*.pyc
	alembic revision --autogenerate -m "Initializing database"
	alembic upgrade head
