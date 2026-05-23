const out=document.getElementById("out");
async function call(url,opt){try{const r=await fetch(url,opt);out.textContent=await r.text();}catch(e){out.textContent=e.message;}}
document.getElementById("simple").onclick=()=>call("http://localhost:8204/posts");
document.getElementById("credential").onclick=()=>call("http://localhost:8204/ai/chat",{method:"POST",credentials:"include",headers:{"Content-Type":"application/json"},body:JSON.stringify({prompt:"hello"})});
