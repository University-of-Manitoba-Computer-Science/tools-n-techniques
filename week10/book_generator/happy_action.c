#include "happy_action.h"

char* get_happy_action(void){
	char* ACTIONS[] = {"sipped wine ", "won a trial by combat ", "received Master title ", 
			   "found a direwolf ", "escaped from the Boltons ", 
			   "received a message from the three-eyed raven "};
	srand(time(NULL));
	int i = rand()%6;

	return ACTIONS[i];
}
