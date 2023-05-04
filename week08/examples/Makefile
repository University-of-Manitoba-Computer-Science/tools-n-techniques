CC = clang
CFLAGS = -Wall -Wextra -Wpedantic -Werror -g

.PHONY: clean

all: ccrash JCrash.class hello

JCrash.class: JCrash.java
	javac JCrash.java

clean:
	rm -f JCrash.class ccrash
