set -e
make --quiet CFLAGS=-g LDLIBS=-lcurses success
./success
