
build:
	./build_site.py
	jekyll

clean:
	rm -rf year/_posts/*
	rm -rf launch-vehicle/_posts/*
	rm -rf location/_posts/*
