
build:
	./build_site.py
	jekyll

clean:
	rm -rf year/_posts/*
	rm -rf launch-vehicle/_posts/*
	rm -rf location/_posts/*

regendb:
	rm -f database/sounding-rocket-history.db
	rm -f database/alembic/versions/*.py
	rm -f database/alembic/versions/*.pyc
	alembic revision --autogenerate -m "Initializing database"
	alembic upgrade head
