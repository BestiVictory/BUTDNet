

import multiprocessing
from gensim.models import Word2Vec
from gensim.similarities import WmdSimilarity
import json

corpus=["Color and lighting are correct but tha black area is too heavy",
"The background is quite close to the subject which it difficult to isolate the subject from the background",
"The color is pretty good but I do think the reds in the image look oversaturated",
"The colors are nice and I know that there is not that much color in this subject",
"The lighting from the flash introduces artifice into the scene that does not look real or natural",
"The lines of composition are fine but the perspective is way too tight",
"Color and overall image is grey and could stand to have more saturation",
"The angle makes the overall image more interesting to look at",
"You may want to experiment with cropping the image a little to the left to move the owls head a bit more to the left margin for balance",
"The subject fills the frame minimizing the amount of empty space around the subject which helps to keep the subject dominant in the composition"
]



def takeSecond(elem):
    return elem[1]
def f1(x1):
  model = Word2Vec(corpus, size=10, min_count=1)
  instance = WmdSimilarity(corpus, model, num_best=5)
  instance = WmdSimilarity(corpus, model)

  with open(x1,'r',encoding='utf8')as fp:
    json_data = json.load(fp)
  Q={}
  x=1
  for i in json_data:
      x=x+1
      if(x>=5000 and x%5000==0):
          print('*****')
      A=[]
      for j in range(len(json_data[i])):
          inquire = json_data[i][j]
        
          inquire_v=inquire      
          sims = instance[inquire_v]
        
          A.append([json_data[i][j]]+[max(list(sims))])
      A.sort(key=takeSecond)
      if(A[0][0]!='' and A[1][0]!='' and A[2][0]!='' and A[3][0]!=''):
        Q[i]=[A[0][0],A[1][0],A[2][0],A[3][0]]
  
  with open('temp'+x1, 'w') as f:
    
    json.dump(Q, f)
if __name__ == '__main__':
    cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cores)
    xs=['0.json','1.json','2.json','3.json','4.json','5.json','6.json','7.json','8.json','9.json','10.json','11.json','12.json','13.json','14.json','15.json']
    pool.map(f1, xs)
    #####corpus = participle(corpus, True)  
    #print(corpus)
    #
    # model = Word2Vec(min_count=1)
    # model.build_vocab(corpus)
    # model.train(corpus, total_examples=model.corpus_count, epochs=model.epochs,)
   