# Discord_ChatBot
A basic discord chatbot
## Introduction
Conversational information access is a rapidly growing field which has gained significant attention in the past few years. A movie recommendation chat-bot is a task oriented recommender system that assists its users in accomplishing recommendation-oriented goals through a multi-turn conversational interaction. Currently in the market there are a broad range of dialogue systems and chat-bots. However, the task of conversational recommendation is characterized by a set of unique needs, which, in our case is related to movies. Further, these preferences may evolve or change during the course of interaction. For example, a user might want to get a movie recommendation based on their genre preference or mood and later may want to find out about streaming platforms. In addition to this, most of the chat services available are closed source commercial products. Hence we chose to build a customized Discord bot for the specific purpose of movie recommendation.

## Task & Purpose of ES:
The task is to develop an open-source conversational movie recommender system which caters to user’s preferences dynamically and supports multi-turn recommendations. To break down into further details:
-	A task-specific dialogue flow along with a set of associated intents to support effective elicitation of user preferences and to provide suggestions from a large collection of items
-	An effective way of dealing with dynamically changing user preferences which involves dialogue intents for revealing and modifying preferences. 
As the name suggests, operating within the movie domain, the main contribution of the work is an open source conversational movie recommendation system featuring a task specific dialogue flow and Discord’s chat interface. 

## Knowledge Source & Knowledge Acquisition:
There are several datasets available related to movies on platforms like Kaggle from sources like IMDB, Movie Lens, Meta Movie curated for both commercial and open source projects. Since the task of this project is to build a customized task specific bot, we have relied primarily on the domain knowledge and sourced the data with individual collection from each group member to build our Knowledge base. We have also gathered data from top websites related to movies and entertainment industry, popular streaming platforms like Netflix, Amazon Prime Video, Disney+, Hulu etc., and curated a custom set of dialogue intents.

## Knowledge Design & Engineering:
First, we curated data and dialogue for production use of the chat-bot. Then a Domain Expert and Subject Matter Expert would annotate the sentences with intents, patterns and responses. The data is further broken down into several sub categories of movies and genres. All of this data is stored in a JSON file – our Knowledge Base, using which, the neural intents model is trained. The Generic Assistant (Chat Bot) will use the neural intents techniques in knowledge base to relate the text and inference the data learnt from the knowledge base, based on the patterns and give the output into the chat box with appropriate response. The bot picks the features based on the tags we have created in the data file and connect the patterns. To ensure the data quality, more than one question shall be asked to the bot and a question can be asked more than twice. 

## User Interface:
The chat interface is implemented on Discord. For the Discord Integration, we have used python discord library to connect to the bot and run the python file which in turn hosts the bot on a local server. The bot is connected to a server on the Discord website or application and becomes active. A user can connect with the bot in a Discord Chat window and initiate the bot using the command ‘!bot’ and type a sentence following it. The bot replies back with appropriate response within the chat window. In this case, the user asks a question related to movie suggestion or updates his preference and the bot replies back with a movie recommendation based on the user input.

## Implementation

-	First, it is needed to install python 3, create and activate a virtual environment using Venv
-	Once the environment is active, at the same directory, store all the project files
-	Install the set of requirements as mentioned below using pip command:
o	Discord 1.7.3
o	Neuralintents 0.0.4
o	OS 0.1.2
o	NLTK 3.4.5
o	Simple JSON 3.16.0
-	Run the python file ‘recommender_bot.py’
-	Open the discord server the bot has been earlier connected to in either web browser or discord application.
-	Initiate a chat with the bot by referencing the bot with the command ‘!bot’ and type your message
That’s it! You can begin your conversation with our bot and get your recommendations.

## Group Members Tasks:
Nicholas Elliott: Knowledge Engineering, Quality Checks
Esra Ersoy: Knowledge Acquisition, Dialog Intent Design
Dheeraj Savanthy: Model Building, Performance reporting
Joseph Mendez: Project Coordinator, Domain Expert
