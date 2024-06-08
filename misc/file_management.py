import consts


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in consts.ALLOWED_EXTENSIONS


def allowed_file_size(file_content_length):
    return file_content_length <= consts.MAX_CONTENT_LENGTH


def allowed_excel_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'xlsx', 'xls'}
