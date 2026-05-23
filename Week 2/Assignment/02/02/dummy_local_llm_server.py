from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Dummy Local LLM Core (OpenAI-compatible)')

class Req(BaseModel):
    model: str
    messages: list[dict]
    temperature: float = 0.7
    max_tokens: int = 256

@app.post('/v1/chat/completions')
def completion(req: Req):
    user_msg = next((m.get('content','') for m in req.messages if m.get('role')=='user'), '')
    return {
        'id':'chatcmpl-local-dummy-001',
        'object':'chat.completion',
        'model':req.model,
        'choices':[{'index':0,'message':{'role':'assistant','content':f'[LOCAL-DUMMY] {user_msg[:120]}'},'finish_reason':'stop'}]
    }
