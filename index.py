from fastapi import FastAPI

app = FastAPI()  # <-- precisa chamar "app"

@app.get("/")
def read_root():
    return {"mensagem": "Olá, mundo!"}

#TesteWebhook

print('Webhook recebido com sucesso!')