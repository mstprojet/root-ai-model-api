from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

app = FastAPI()


# Exemple : on simule un modèle IA
class SimpleModel:
    def predict(self, text: str) -> str:
        if "bonjour" in text.lower():
            return "French"
        elif "hello" in text.lower():
            return "English"
        else:
            return "Unknown"


model = SimpleModel()


# Pour recevoir une requête JSON
class InputText(BaseModel):
    text: str


@app.post("/predict")
async def predict(input: InputText):
    result = model.predict(input.text)
    return {"language": result}


@app.get("/ping")
async def ping():
    return {"message": "L'IA est en vie!"}


# Lancer en local : uvicorn main:app --reload
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
