const API_BASE=import.meta.env.VITE_API_BASE_URL||'http://localhost:8000';
export async function scoreEssay(essay){const res=await fetch(`${API_BASE}/api/v1/score`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({essay})}); const data=await res.json(); if(!res.ok) throw new Error(data?.detail?.message||data?.detail||'Scoring request failed.'); return data;}
