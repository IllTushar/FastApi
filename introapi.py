from fastapi import FastAPI

app = FastAPI()


@app.get('/about')
def info():
    return {'data':'Tushar is Good'}   ##{}=> dictionary return response in json format.. 
  
  
@app.get('/newdic')
def dec():
    return {'data':{'name':'Tushar Gupta'}}