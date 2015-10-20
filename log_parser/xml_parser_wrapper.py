from bs4 import BeautifulSoup
from lxml import etree
from log_parser import TestData

def parse_html_data(html_data):
    soup = BeautifulSoup(html_data, "html.parser")
    collection = []

    for test in soup.find_all('div', {'class': 'test'}):
        id = test.attrs['data-test-id']
        name = test.attrs['data-test-name']
        status = test.find('div', {'class': 'results'}).attrs['data-status']
        exception = ''
        if status != 'PASSED':
            exception = test.find('div', {'class': 'exception'}).text

        test_data = TestData.TestData(name, id, status, exception)
        collection.append(test_data)

    return collection


def wrap_to_junit_xml(tests):
    failed_count = 0

    root_testsuites = etree.Element('testsuites')
    el_testsuite = etree.Element('testsuite')

    for test in tests:
        el_testcase = etree.Element('testcase', name=test.name, classname=test.id)
        # move this shit outta here
        if test.status != "PASSED":
            el_error = etree.Element('error')
            el_error.text = test.exception
            el_testcase.append(el_error)
            failed_count += 1

        el_testsuite.append(el_testcase)

    passed_count = len(tests)
    el_testsuite.set("tests", str(passed_count))
    el_testsuite.set("failures", str(failed_count))
    root_testsuites.append(el_testsuite)

    return etree.tostring(root_testsuites, pretty_print=True, encoding='UTF-8', xml_declaration=False)
