from app import app


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def allowed_file_size(file_content_length):
    return file_content_length <= app.config['MAX_CONTENT_LENGTH']
