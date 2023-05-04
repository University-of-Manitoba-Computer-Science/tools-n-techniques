#include "sad_action.h"

char* get_sad_action(void){
	char* ACTIONS[] = {"stepped on wildfire ", "heard Dracarys ", "fell down from a tower ",
			   "attended a red wedding ", "heard a voice saying 'hold the door' ", 
			   "became a whitewalker "};
	srand(time(NULL));
	int i = rand() % 6;
	return ACTIONS[i];
}
