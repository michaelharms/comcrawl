from typing import Dict
import requests
import json
import io
import gzip


def download_single_result(result: Dict) -> str:
    result_url = result["url"]
    offset, length = int(result["offset"]), int(result["length"])

    offset_end = offset + length - 1

    prefix = "https://commoncrawl.s3.amazonaws.com"
    response = requests.get(f"{prefix}/{result['filename']}", headers={"Range": f"bytes={offset}-{offset_end}"})

    raw_data = io.BytesIO(response.content)
    f = gzip.GzipFile(fileobj=raw_data)

    data = f.read()
    data = data.decode("utf-8")

    html = ""

    if len(data) > 0:
        _, _, html = data.strip().split("\r\n\r\n", 2)

    return html
