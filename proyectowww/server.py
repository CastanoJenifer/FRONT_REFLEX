from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Montar la carpeta 'assets' como un directorio estático
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# Ruta que devuelve un archivo específico
@app.get("/assets/{filename}")
def get_asset(filename: str):
    return FileResponse(f"assets/{filename}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
