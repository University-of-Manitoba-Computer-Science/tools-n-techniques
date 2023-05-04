CC = clang
CFLAGS = -Wall -Wpedantic -Wextra -Werror -g

book_generator: book_generator.c chapter_driver.o sad_action.o neutral_action.o happy_action.o
	$(CC) $(CFLAGS) $^ -o $@

chapter_driver.o: chapter_driver.c sad_action.o neutral_action.o happy_action.o
	$(CC) $(CFLAGS) -c $<

sad_action.o: sad_action.c
	$(CC) $(CFLAGS) -c $< 

neutral_action.o: neutral_action.c
	$(CC) $(CFLAGS) -c $<

happy_action.o: happy_action.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm book_generator
	rm *.o
	rm *.md
