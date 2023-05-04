#include "neutral_action.h"

char* get_neutral_action(void){
	char* ACTIONS[] = {"greeted Littlefinger ", "was judged by Cersei Lannister ", 
			   "smiled at Sansa Stark ", "heard a gossip from Lord Varys ", 
			   "learned to speak High Valyrian ", "petted Drogon ", "has no name "};
	srand(time(NULL));
	int i = rand() % 7;

	return ACTIONS[i];
}
