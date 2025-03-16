from fastapi import APIRouter, UploadFile, Form
from app.services import ocr_service

router = APIRouter(
    prefix="/ocr",  # 设置路由前缀
    tags=["ocr"]  # 可选，为这些路由设置标签, 也可在装饰器中单独设置
)


@router.post("/file")
async def create_upload_file(file: UploadFile, lang: str | None = Form(None), stream: str | None = Form(None)):
    """
    :param file: 上传文件
    :param lang: zh-Hans, en-US
    :param stream: 1 或者其它
    :return:
    """
    if lang is not None:
        lang = lang.split(",")
    return await ocr_service.file_ocr(file, lang, stream=stream == "1")
