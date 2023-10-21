from fastapi import FastAPI, Path
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse

app = FastAPI()

@app.get('/')
def root():
    return {'message' : 'Hello, student!'}

@app.get('/add')
def add(x: int, y: int) -> int:
    return x + y

@app.get('/double/{number}')
def double(number: int) -> int:
    return number * 2

@app.get('/welcome/{name}')
def welcome(name: str = Path(min_length=2, max_length=20)) -> str:
    return f'Good luck, {name}!'

@app.get('/phone/{number}')
def phone_number(number: str = Path(regex = '/^(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10,14}(\s*)?$/')):
    return {'phone' : number}

@app.get('/text')
def get_text():
    content = 'Lorem Ipsum Dolor sit amet'
    return PlainTextResponse(content=content)

@app.get('/html')
def get_html():
    content = './index.html'
    return HTMLResponse(content=content)

@app.get('/file')
def get_file():
    content = 'index.html'
    return FileResponse(
        content,
        media_type='application/octet-stream',
        filename='index2.html'
    )

@app.get(path:'/html', response_class = HTMLResponse)
def get_html():
    content = '<h2>HTML!!!</h2>'
    return HTMLResponse(content=content)