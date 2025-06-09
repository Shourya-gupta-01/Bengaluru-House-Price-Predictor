from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import pickle

data=pd.read_csv('cleaned_data.csv')

def index(request):
    location=sorted(data['location'].unique())
    return render(request, 'index.html', {'location': location})

def makePrediction(request):
    location = request.POST.get('location')
    bhk = int(request.POST.get('bhk'))
    bath = int(request.POST.get('bath'))
    sqft = float(request.POST.get('sqft'))
    
    # Load the model
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Prepare the input data
    input_data = pd.DataFrame([[location, bhk, bath, sqft]], columns=['location', 'bhk', 'bath', 'total_sqft'])

    # Make prediction
    prediction = model.predict(input_data)[0]
    prediction*=100000
    
    if prediction>100000000:
        prediction=str(prediction)[0]+str(prediction)[1]+'.'+str(prediction)[2]+str(prediction)[3]+' crores'
    elif prediction>10000000:
        prediction=str(prediction)[0]+'.'+str(prediction)[1]+str(prediction)[2]+' crores'
    elif prediction>1000000:
        prediction=str(prediction)[0]+str(prediction)[1]+'.'+str(prediction)[2]+str(prediction)[3]+' lakhs'
    elif prediction>100000:
        prediction=str(prediction)[0]+'.'+str(prediction)[1]+str(prediction)[2]+' lakhs'
    else:
        pass
    
    return HttpResponse(prediction)