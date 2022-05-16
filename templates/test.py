import joblib
import random
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

symp1 = 'Itching'
symp2 = 'Skin Rash'
symp_list = []
symp_list.append(symp1)
symp_list.append(symp2)

rf_model = joblib.load('model.sav')


encoder = LabelEncoder()
data = pd.read_csv("Training.csv").dropna(axis = 1)
data["prognosis"] = encoder.fit_transform(data["prognosis"])
X = data.iloc[:,:-1]
symptoms = X.columns.values

symptom_index = {}
for index, value in enumerate(symptoms):
	symptom = " ".join([i.capitalize() for i in value.split("_")])
	symptom_index[symptom] = index

data_dict = {
	"symptom_index":symptom_index,
	"predictions_classes":encoder.classes_
}

input_symp = ['Itching', 'Skin Rash']
input_data = [0] * len(data_dict["symptom_index"])
for symptom in input_symp:
	index = data_dict["symptom_index"][symptom]
	input_data[index] = 1
		
# reshaping the input data and converting it
# into suitable format for model predictions
input_data = np.array(input_data).reshape(1,-1)
	
# generating individual outputs
rf_prediction = data_dict["predictions_classes"][rf_model.predict(input_data)[0]]

ds={'test':0}
idx=1
mlist=[
'Cefixime',
'Ceftazidime',
'Cefuroxime',
'Celecoxib',
'Cephalexin',
'Cidofovir',
'Cisplatin',
'Cladribine',
'Clarithromycin',
'Clindamycin',
'Clobazam',
'Clofarabine',
'Codeine',
'Crizanlizumab',
'Crizotinib',
'Cyclobenzaprine',
'Cyclophosphamide',
'Cyclosporine',
'Cyproheptadine',
'Cytarabine',
'Dacarbazine',
'Dactinomycin',
'Dapsone',
'Darunavir (Prezista®)',
'Dasatinib',
'Daunorubicin',
'Deferasirox (Exjade®)',
'Desmopressin (Stimate®)',
'Dexamethasone',
'Diclofenac',
'Didanosine',
'Dinutuximab',
'Dobutamine',
'Dopamine'
]
data2=pd.read_csv("Training.csv")
xx=np.array(data2['prognosis'])
xx=np.unique(xx)
listt=xx.tolist()
for item in listt:
  if item in ds:
    ds[item]=idx
  else:
    ds[item]=idx
  idx+=1

medicine={0:'None'}

for i in range(1,42):
  medicine[i]=random.choice(mlist)


final_res = medicine[ds[rf_prediction]]
print(final_res)