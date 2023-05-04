#include "chapter_driver.h"

char* get_article(void){
	char* ARTICLE[] = {"A ", "One ", "An elder ", "M'Lord ", "M'Lady ", "Maester "};
	
	srand(time(NULL));
	return ARTICLE[rand() % 6];
}

char* get_noun(void)
{
	char* ARTICLE[] = {"Targeryen ", "Lannister ", "Stark ", "Baratheon ", "Tyrell ", "Martell ", 
			   "Hightower ", "Greyjoy "};
	
	srand(time(NULL));
	return ARTICLE[rand() % 8];
}

char* get_place(void){
	char* ARTICLE[] = {"at The Wall.", "at Winterfell.", "at Whiteharbor.", "at Greywater Watch.",
			   "at Asshai.", "at Braavos.", "at The Dothraki Sea.", "at Volantis.", "at The Eyrie."};
	
	srand(time(NULL));
	return ARTICLE[rand() % 9];
}

char* get_sentence(Action Act){
	char* prefix = get_article();
	char* noun = get_noun();
	char* suffix = NULL;
	char* place = get_place();

	switch(Act){
		case SAD:
			suffix = get_sad_action();
			break;
		case NEUTRAL:
			suffix = get_neutral_action();
			break;
		case HAPPY:
			suffix = get_happy_action();
			break;
		default:
			fprintf(stderr, "ERROR: Action is not supported. (get_sentence).\n");
			suffix = get_happy_action();
			break;
	}
			

	int size = strlen(prefix) + strlen(noun) + strlen(suffix)+ strlen(place);
	char* to_return = calloc(size, sizeof(char));
	strcat(to_return, prefix);
	strcat(to_return, noun);
	strcat(to_return, suffix);
	strcat(to_return, place);
	
	return to_return;
}
