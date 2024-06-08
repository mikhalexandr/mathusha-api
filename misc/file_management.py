def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {"png", "jpg", "jpeg"}


def allowed_file_size(file_content_length):
    return file_content_length <= 16 * 1024 * 1024
