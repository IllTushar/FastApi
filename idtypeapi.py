import re
from fastapi import FastAPI


app = FastAPI()



@app.get('/blog')
def shownew(limit =10,published: bool=True):
    if published:
          {'data':f'{limit} published is of the db'}
    else:
        {'data':f'{limit} unpublished is of the db'}


@app.get('/blog/unpublished')   
def unpublisedblog():
    return {'data':'this is unpublished blog'}

@app.get('/blog/{id}')
def show(id: int):
    #featch blog of id = id!
    return {'data':id}




# @app.get('/blog/unpublished')   when we implement below the id then it show error 
# if we show above the id not show error called dynamic routing
# def unpublisedblog():
#     return {'data':'this is unpublished blog'}





# @app.get('/comment/{id}')
# def comment(id):
#     return {'data':{'comment':{'1','2'}}}

