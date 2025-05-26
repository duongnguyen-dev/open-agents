from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from loguru import logger
from llmbuddy.services.documents.documents_service import DocumentService

router = APIRouter()

@router.post("/extract_document")
async def extract_document(file: UploadFile = File(...)):
    try:
        doc_service = DocumentService()
        # Save the uploaded file to a temporary location
        doc_data = await file.read()
        result = doc_service.read_document(doc_data)
        return JSONResponse(content={"extracted_result": result})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))