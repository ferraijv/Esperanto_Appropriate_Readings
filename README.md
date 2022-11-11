# Esperanto_Appropriate_Readings

The purpose of this project is to create a program that allows language learners to practice their target language with language samples pulled from Wikipedia. 
The program will rank the difficulty of each Wikipedia page and ask the reader to score each reading. Using these scores, the program will suggest readings
that match the user's level.

## Goal

I want to build a front-end that a learner can interact with to input their current level of competence with Esperanto. The program will then search
Wikipedia for a random article that is suitable for that specific learner to read. We can either present the text segment on our front-end or link the user to 
the article.

## Description

The program will seek out new articles each time the user interacts with the program. We will not be persisting articles or ratings. I need to figure out
the best way to develop a ranking system for difficulty. For the first attempt, I will try to find the number of distinct words in an article and the average
length of the word in the article. I hope to improve this algorithm as I delve deeper into this project.

## Test
test
