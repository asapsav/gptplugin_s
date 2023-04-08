import json

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse

app = FastAPI()

_TODOS = {}


@app.post("/todos/{username}")
async def add_todo(username: str, todo: str):
  if username not in _TODOS:
    _TODOS[username] = []
  _TODOS[username].append(todo)
  return JSONResponse(content='OK', status_code=200)


@app.get("/todos/{username}")
async def get_todos(username: str):
  return JSONResponse(content=_TODOS.get(username, []), status_code=200)


@app.delete("/todos/{username}")
async def delete_todo(username: str, todo_idx: int):
  if username inx _TODOS and 0 <= todo_idx < len(_TODOS[username]):
    _TODOS[username].pop(todo_idx)
  return JSONResponse(content='OK', status_code=200)


@app.get("/logo.png")
async def plugin_logo():
  return FileResponse('logo.png')


@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest(request: Request):
  host = request.headers['host']
  with open("ai-plugin.json") as f:
    text = f.read().replace("PLUGIN_HOSTNAME", f"https://{host}")
  return JSONResponse(content=json.loads(text))


@app.get("/openapi.json")
async def openapi_spec(request: Request):
  host = request.headers['host']
  with open("openapi.json") as f:
    text = f.read().replace("PLUGIN_HOSTNAME", f"https://{host}")
  return JSONResponse(content=text, media_type="text/json")


if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=5002)
