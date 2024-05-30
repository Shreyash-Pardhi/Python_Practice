The following folder has two json files "lessons" and "quizes"


Both files have multiple lessons and quizes and a vector embeddding corresponding to each lesson and quiz. Vector embedding are mathematical representaion of sentences.


For Eg- "I like hiking" can be represented by a vector embedding which looks like this-[0.010030677542090416, 0.003412498626857996, -0.02..........]

We use cosine similarity to find similarity between two vectors which shows how two sentences are similar to each other.

Code to find cosine similarity:

	from sklearn.metrics.pairwise import cosine_similarity


	# Example vectors
	vector1 =[1, 2, 3]
	vector2 = [1, 2, 3]



	# Calculate cosine similarity
	cosine_sim = cosine_similarity([vector1], [vector2])

	print(cosine_sim[0][0])

	Output-0.9600014517991347


write program which finds a lesson with highest cosine similairy to every quiz and stores it in a txt file. There might be irregulaties in the json files.






