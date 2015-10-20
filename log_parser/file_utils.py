import codecs


def get_file_contents(file_name):
    with codecs.open(file_name, mode='r', encoding='utf-8') as tmp_file:
        tmp_data = tmp_file.read()
    return tmp_data


def save_xml_to_file(xml_data, file_name):
    with codecs.open(file_name, mode='w') as tmp_file:
        tmp_file.write(xml_data)