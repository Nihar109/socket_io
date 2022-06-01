from fastapi import FastAPI, exceptions, responses, Request, templating, Depends
#import asyncio
from folder.main_thread import Result

result1 = Result()
result = result1.main_threads()
app = FastAPI()

@app.get("/")
async def root():
    reprturn result

if __name__ == '__main__':
    from uvicorn import run
    run(app)






