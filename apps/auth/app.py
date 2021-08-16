import uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hiroo():
    return {'hi':'roo'}

if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=8000, reload=True)