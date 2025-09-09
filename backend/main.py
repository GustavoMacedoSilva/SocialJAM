from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':'blog list'}

@app.get('/blog/{id}')
def about(id:int):
    # achando o a largura do
    return {'data': id}

@app.get('/blog/unpublished')


@app.get('/blog/{id}/comments')
def comments(id):
    #dando um fetch nos comentarios com id = id
    return {'data': {'1','2'}}