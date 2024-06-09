PYVERSION=3.11

build:
	@ mkdir -p build out ; \
	python3 -m venv ./build/env ; \
	source ./build/env/bin/activate ; \
	pip3 install -r build_requirements.txt ; \
	pip3 install -r requirements.txt ; \
	python3 -m cython ./src/foxtrot.py --3str --embed -o ./build/foxtrot.c ; \
	gcc ./build/foxtrot.c -I/usr/include/python3.11 -lpython3.11 -o ./out/foxtrot

clean:
	@ rm -rf out build

run:
	@ ./out/foxtrot

all: clean build run