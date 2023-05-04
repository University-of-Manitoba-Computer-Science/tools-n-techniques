#ifndef CHAPTER_DRIVER_H
#define CHAPTER_DRIVER_H

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "sad_action.h"
#include "neutral_action.h"
#include "happy_action.h"

typedef enum{SAD, NEUTRAL, HAPPY} Action;

char* get_article(void);
char* get_place(void);
char* get_noun(void);
char* get_sentence(Action Act);

#endif
