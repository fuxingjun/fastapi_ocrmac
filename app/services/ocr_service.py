from fastapi import UploadFile
from fastapi.responses import StreamingResponse
from ocrmac import ocrmac
from PIL import Image
from io import BytesIO

from app.utils.http import http_success, http_fail

# 支持的格式与对应的 MIME 类型映射
SUPPORTED_FORMATS = {
    "JPEG": "image/jpeg",
    "PNG": "image/png",
    "GIF": "image/gif",
    "WEBP": "image/webp",
}


async def file_ocr(file: UploadFile, lang=None, stream: bool = False):
    try:
        # 读取上传文件的二进制内容
        contents = await file.read()

        # 将二进制内容转换为 BytesIO 对象（Pillow 可处理的流）
        image_stream = BytesIO(contents)

        # 使用 Pillow 打开图像
        image = Image.open(image_stream)

    except Exception as e:
        return http_fail(str(e))
    instance = ocrmac.OCR(image, language_preference=lang)
    if stream:
        img = instance.annotate_PIL()
        # img.save("t.png")
        img_byte_arr = BytesIO()
        # 获取原始格式（例如："JPEG"、"PNG"）
        original_format = image.format

        # 检查是否支持该格式
        if original_format not in SUPPORTED_FORMATS:
            return http_fail(f"Unsupported format: {original_format}")
        img.save(img_byte_arr, format=original_format)
        img_byte_arr.seek(0)

        # 动态设置媒体类型
        media_type = SUPPORTED_FORMATS[original_format]
        return StreamingResponse(img_byte_arr, media_type=media_type)
    else:
        annotations = instance.recognize()
        # print(annotations)
        return http_success({"annotations": annotations})
