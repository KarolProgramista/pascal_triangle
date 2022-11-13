CFLAGS=-Wall
LIBS=-lm

all:
	$(CC) $(CFLAGS) main.c -o main $(LIBS)
