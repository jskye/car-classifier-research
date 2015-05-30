CC = g++
CFLAGS = `pkg-config --cflags opencv`
LDFLAGS = `pkg-config --libs opencv` -lm
ALL = car_detect

all: $(ALL)

car_detect: car_detect.o
	$(CC) $(LDFLAGS) -o $@ $^

car_detect.o: car_detect.cpp
	$(CC) $(LDFLAGS) -c $<

.PHONY: clean

clean:
	rm -rf *.o core* $(ALL)
