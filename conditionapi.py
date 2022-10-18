from fastapi import FastAPI


app = FastAPI()

@app.get('/blog')
def shownew(limit: int="tsuahr",published: bool=True):
        if published:
          return {'data':f'{limit} published is of the db'}
        else:
          return {'data':f'{limit} unpublished is of the db'}
