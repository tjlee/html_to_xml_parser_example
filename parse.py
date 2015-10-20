import argparse

from log_parser import file_utils
from log_parser import xml_parser_wrapper


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", default="./report.html", help="Source html report file path")
    parser.add_argument("-r", "--report", default="./report.xml",
                        help="Parsed jUnit report file (default: ./report.xml)")

    args = parser.parse_args()

    data = file_utils.get_file_contents(args.source)
    test_collection = xml_parser_wrapper.parse_html_data(data)
    file_utils.save_xml_to_file(str(xml_parser_wrapper.wrap_to_junit_xml(test_collection)), args.report)

