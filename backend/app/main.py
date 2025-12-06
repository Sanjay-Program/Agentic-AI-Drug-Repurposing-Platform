from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import evaluation, reports, history, finance, research, signals

app = FastAPI(
    title="Agentic AI for Drug Repurposing",
    version="0.2.0",
    description="EY Hackathon: Multi-Agent Innovation Platform with portfolio, auto-research & ROI.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ok for hackathon
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(evaluation.router, prefix="/api/evaluation", tags=["evaluation"])
app.include_router(reports.router, prefix="/api/reports", tags=["reports"])
app.include_router(history.router, prefix="/api/history", tags=["history"])
app.include_router(finance.router, prefix="/api/finance", tags=["finance"])
app.include_router(research.router, prefix="/api/research", tags=["research"])
app.include_router(signals.router, prefix="/api/signals", tags=["signals"])


@app.get("/health")
def health():
    return {"status": "ok"}
