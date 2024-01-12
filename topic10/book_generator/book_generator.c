#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "chapter_driver.h"

int main(void)
{
	FILE *chapter1, *chapter2, *chapter3;

	fprintf(stdout, "Creating chapter files.\n");
	chapter1 = fopen("./chapter1.md", "w");
	chapter2 = fopen("./chapter2.md", "w");
	chapter3 = fopen("./chapter3.md", "w");
	fprintf(stdout, "Chapter files created.\n");

	fprintf(stdout, "Chapter 1 being created...\n");
	fprintf(chapter1, "# Chapter 1 - The Beginning\n\n");
	fprintf(chapter1, "%s\n", get_sentence(SAD));
	sleep(1);
	fprintf(chapter1, "%s\n", get_sentence(NEUTRAL));
	fprintf(stdout, "Chapter 1 done.\n");
	
	sleep(1);

	fprintf(stdout, "Chapter 2 being created...\n");
	fprintf(chapter2, "# Chapter 2 - The Development\n\n");
	fprintf(chapter2, "%s\n", get_sentence(NEUTRAL));
	sleep(1);
	fprintf(chapter2, "%s\n", get_sentence(SAD));
	fprintf(stdout, "Chapter 2 done.\n");

	sleep(1);

	fprintf(stdout, "Chapter 3 being created...\n");
	fprintf(chapter3, "# Chapter 3 - The Ending\n\n");
	fprintf(chapter3, "%s\n", get_sentence(HAPPY));
	sleep(1);
	fprintf(chapter3, "%s\n", get_sentence(SAD));
	fprintf(stdout, "Chapter 3 done.\n");

	fclose(chapter1);
	fclose(chapter2);
	fclose(chapter3);

	return EXIT_SUCCESS;
}
