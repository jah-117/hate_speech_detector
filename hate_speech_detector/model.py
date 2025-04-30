import joblib
import os
import regex as re
from nltk.stem import PorterStemmer

ps = PorterStemmer()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'assets/svm_text_classifier.pkl')

def isHate(sample):
    model_data = joblib.load(MODEL_PATH)
    clf = model_data['model']
    filtered_data = model_data['filtered_data']
    # print('model loaded successfully')

    sample = sample.split(' ')
  
    cleantext = []
    for s in sample:
        # cleaned = re.sub(r'[^\w]', '', s)
        cleaned = re.sub(r'[^a-zA-Z]', '', s)
        cleantext.append(cleaned)
        # print(cleantext)
    stemmed = []
    for w in cleantext:
        # print(w, " : ", ps.stem(w))
        if len(w) >= 3:
            stemmed.append(ps.stem(w))
    r = []
    for j in filtered_data:
        if j in stemmed:
            r.append(1)
        else:
            r.append(0)
    res=clf.predict([r])
    # print(res,"+++++++++++++++++++++++")
    # print(res,"+++++++++++++++++++++++")
    # print(res,"+++++++++++++++++++++++")
    # print(res,"+++++++++++++++++++++++")
    if res[0] == 2:
        return {'message':'Not Hate Speech', 'isHate':False}
    else:
        return {'message':'Hate Speech','isHate':True}