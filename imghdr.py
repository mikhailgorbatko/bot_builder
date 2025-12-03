# imghdr.py — простой совместимый заглушечный модуль для Python 3.13+

import os
import mimetypes
from typing import Optional, Union, BinaryIO

FileT = Union[str, bytes, os.PathLike, BinaryIO]

def what(file: FileT, h: bytes | None = None) -> Optional[str]:
    """
    Простейшая реализация imghdr.what.
    Определяет тип по расширению файла. Этого достаточно для telegram-бота.
    """
    name: Optional[str] = None

    # Если передали файловый объект — возьмём имя, если оно есть
    if hasattr(file, "read"):
        name = getattr(file, "name", None)
    else:
        name = str(file)

    if name:
        mime, _ = mimetypes.guess_type(name)
        if mime and mime.startswith("image/"):
            return mime.split("/")[-1]  # 'image/png' -> 'png'

    return None
