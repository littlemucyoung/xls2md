# !/usr/bin/env python
# --*--coding:utf-8--*--

"""XLS2MD CLI

Usage:
xls2md.py [--head] --from <from_path> [--sindex <sheet_index>|--sname <sheet_name>] --to <to_path>
xls2md.py -h | --help
xls2md.py -v | --version

Options:
-h --help Show this screen.
-v --version Show version.
--head  The excel file has a head row
--from  From_Path(path of the excel file)
--to  To_Path(path of the markdown file)
--sheet  Specify the target sheet(name or id)
"""

from docopt import docopt
import xlrd


def excel_to_md(from_path, sheet, to_path, has_head):
    book = xlrd.open_workbook(from_path)
    sheet = book.sheet_by_name(sheet) if sheet else book.sheet_by_index(sheet)
    with open(to_path, "w+") as md_file:
        output_md(sheet.row(0), md_file)
        if has_head:
            output_description(sheet.ncols, md_file)
        for rx in range(1, sheet.nrows):
            output_md(sheet.row(rx), md_file)


def output_description(ncols, file):
    file.write("|")
    for i in range(ncols):
        file.write(" --- |")
    file.write("\n")


def output_md(row, file):
    file.write("|")
    for cell in row:
        file.write(str(cell.value))
        file.write("|")
    file.write("\n")


def xls2md():
    arguments = docopt(__doc__, version='XLS2MD 0.1')
    has_head = arguments['--head']
    from_path = arguments['<from_path>']
    if arguments['--sindex']:
        sheet = int(arguments['<sheet_index>'])
    elif arguments['--sname']:
        sheet = arguments['<sheet_name>']
    else:
        sheet = 0
    to_path = arguments['<to_path>']
    excel_to_md(from_path, sheet, to_path, has_head)


if __name__ == '__main__':
    xls2md()
