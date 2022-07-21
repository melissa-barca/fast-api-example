from fastapi import FastAPI, Request
import subprocess
import os


url = subprocess.run('echo ${RS_SERVER_URL}${RS_SESSION_URL}/p/$(/usr/lib/rstudio-server/bin/rserver-url 8000)', stdout=subprocess.PIPE, shell=True).stdout.decode().strip()
app = FastAPI(root_path=url)

@app.get("/")
async def root(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}

@app.get("/app")
def read_main(request: Request):
    return {"message": "App!", "root_path": request.scope.get("root_path")}