from flask import abort

def too_large(e):
    return "File is too large", 413

def invalid_image():
    return "Invalid image", 400
