
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field
import hmac, hashlib, time

SECRET='dev-secret'
app=FastAPI(title='HTTPS REST API')

class PostIn(BaseModel):
    title:str=Field(min_length=1,max_length=120)
    content:str=Field(min_length=1,max_length=5000)

def verify(ts:str,sig:str,body:str):
    if abs(time.time()-int(ts))>300: return False
    expected=hmac.new(SECRET.encode(),f'{ts}.{body}'.encode(),hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected,sig)

@app.post('/secure/posts')
def create_post(data:PostIn,x_api_key:str=Header(''),x_timestamp:str=Header('0'),x_signature:str=Header('')):
    if x_api_key!='demo-key': raise HTTPException(401,'invalid api key')
    if not verify(x_timestamp,x_signature,data.model_dump_json()): raise HTTPException(401,'invalid signature')
    return {'ok':True,'security':['encryption(TLS assumed)','integrity(HMAC)','auth(API key)']}
