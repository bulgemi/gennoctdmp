# _*_ coding: utf-8 _*_

import re
import operator


def gen_column(f):
    column_info = dict()

    f.write("[COLUMN]\n")

    while True:
        column = input(u"input column information(input format[column name, index], Enter to exit): ")

        if column == "":
            break
        # 공백 제거
        column = column.strip()

        comma = re.findall(",", column)

        if len(comma) == 0:
            print(u"invalid column format. column format[column name, index]!\n")
            exit()

        column_index = re.split(',', column)
        column_info[int(column_index[1])] = column_index[0].strip()

    sort_column_info = sorted(column_info.items(), key=operator.itemgetter(0))
    print(sort_column_info)

    for v in sort_column_info:
        f.writelines("\"%s\", NULL, NULL\n" % str(v[1]).strip())

    f.write("\n")


def gen_skip(f):
    f.write("[SKIP]\n")

    while True:
        skip = input(u"input Skip information(Enter to exit): ")

        if skip == "":
            f.write("\n")
            break

        skip = skip.strip()
        f.writelines("\"%s\"\n" % skip)


def gen_table(f):
    table_name = ""

    while True:
        table = input(u"input DB table name(Enter to exit): ")

        if table == "":
            break
        # 공백 제거
        table = table.strip()

        under_bar = re.findall('_', table)

        if len(under_bar) != 0:
            appname = re.split('_', table)
            table_name = appname[0] + "." + table
        else:
            table_name = table

        # 테이블 정보 생성
        f.write("[TABLE]\n")
        f.writelines("\"%s\"\n\n" % table_name.strip())

        # 컬럼 정보 생성
        gen_column(f)

        # 스킵 정보 생성.
        gen_skip(f)

if __name__ == "__main__":
    dmpfile = input(u"input file name: ")

    if dmpfile == "":
        exit()

    f = open(str(dmpfile)+".dmp", "w")
    gen_table(f)
    f.close()
