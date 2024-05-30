from sklearn.metrics.pairwise import cosine_similarity
import json
import numpy as np

lesson = open("Assignments\\Cosign Similarity\\lessons.json", encoding='utf8')
quizes = open("Assignments\\Cosign Similarity\\quizes.json", encoding='utf8')


les = json.load(lesson)
quiz = json.load(quizes)

for i in range(0,10): # use "len(quiz)" for all quiz questions
    ans = []
    for j in range(len(les)):
        emb_les = les[j]["emb"]
        emb_quiz = quiz[i]["emb"]
        
        con1 = np.array(np.matrix(emb_les)).ravel()
        con2 = np.array(np.matrix(emb_quiz)).ravel()
        
        cosine_sim = cosine_similarity([con1], [con2])
        ans.append(cosine_sim[0][0])

    max_index = ans.index(max(ans))
    min_index = ans.index(min(ans))
    print(f"when {i},{j} then max:{max_index} min:{min_index}")
    
    with open("Assignments\\Cosign Similarity\\results.txt",'a',encoding='utf8') as file:
        file.write(f"\n{i+1}) Quiz Question:\n{quiz[i]["question"]}\n")
        file.write(f"\n**Lesson with max similarity:**\n{les[max_index]["text"]}")
        file.write(f"\n**Lesson with No/Less similarity:**\n{les[min_index]["text"]}")
        file.write("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print("done")