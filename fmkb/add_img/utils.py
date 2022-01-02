import os

ALLOWED_IMAGE_EXTENSIONS = ["png", "jpg", "jpeg"]


def get_extension(file: str) -> str:
    return os.path.splitext(file)[1].replace(".", "")


def check_extension(file: str) -> bool:
    return get_extension(file).lower() in ALLOWED_IMAGE_EXTENSIONS
