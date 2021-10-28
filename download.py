import rasterio
import time
import json
import pandas as pd
#https://downloadagiv.blob.core.windows.net/dhm-vlaanderen-ii-dtm-raster-1m/DHMVIIDTMRAS1m_k01.zip
list_url = []
for i in range(1, 2):
    if i<10:
        page_num = str(i) + ".zip"
        url = (
            "https://downloadagiv.blob.core.windows.net/dhm-vlaanderen-ii-dtm-raster-1m/DHMVIIDTMRAS1m_k0" + page_num
        )
        list_url.append(url)
    else:
        page_num = str(i) + ".zip"
        url = (
                "https://downloadagiv.blob.core.windows.net/dhm-vlaanderen-ii-dtm-raster-1m/DHMVIIDTMRAS1m_k" + page_num
        )
        list_url.append(url)


