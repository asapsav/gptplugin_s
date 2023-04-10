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

@app.get("/generate-openapi-yaml")
async def generate_openapi_yaml():
    import yaml  # Import the pyyaml library

    import os
    from fastapi.openapi.utils import get_openapi

    # Get the OpenAPI JSON schema
    openapi_schema = get_openapi(
        title="My Application",
        version="1.0.0",
        routes=app.routes,
    )

    # Convert the JSON schema to YAML
    openapi_yaml = yaml.dump(openapi_schema)

    # Create the .well-known directory if it doesn't exist
    os.makedirs(".well-known", exist_ok=True)

    # Write the YAML schema to the .well-known/openapi.yaml file
    print("Writing OpenAPI YAML schema to .well-known/openapi.yaml")
    with open(".well-known/openapi.yaml", "w") as yaml_file:
        yaml_file.write(openapi_yaml)

    return {"detail": "OpenAPI YAML schema has been generated and stored in .well-known/openapi.yaml"}


@app.on_event("startup")
async def on_startup():
    # Call the generate_openapi_yaml function during the startup event
    await generate_openapi_yaml()

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
