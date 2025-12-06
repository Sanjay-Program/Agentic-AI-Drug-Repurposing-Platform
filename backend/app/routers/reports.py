from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
from app.services.pdf_report import PdfReportService

router = APIRouter()
pdf_service = PdfReportService()


@router.get("/{report_id}")
def download_report(report_id: str):
    path = pdf_service.get_report_path(report_id)
    if not path or not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Report not found")

    return FileResponse(
        path,
        media_type="application/pdf",
        filename=f"innovation_report_{report_id}.pdf",
    )
