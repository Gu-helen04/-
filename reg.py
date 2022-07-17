import csv
import re


def open_files():
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def list_conversion(contacts_list):
    pattern_full_name = r"\s"
    pattern_phone_number = r"(\+?7|8)?\s*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(\s*\(?(доб.)\s*(\d+)\)?)?"
    for list_string in range(len(contacts_list)):
        for lines_with_name in range(3):
            if lines_with_name == 0:
                split_name = re.split(pattern_full_name, contacts_list[list_string][lines_with_name])
                if len(split_name) > 1:
                    for overwrite_string in range(len(split_name)):
                        contacts_list[list_string][overwrite_string] = split_name[overwrite_string]
            elif lines_with_name == 1:
                split_name = re.split(pattern_full_name, contacts_list[list_string][lines_with_name])
                if len(split_name) > 1:
                    for overwrite_string in range(len(split_name)):
                        contacts_list[list_string][overwrite_string + 1] = split_name[overwrite_string]
            elif lines_with_name == 3:
                split_name = re.split(pattern_full_name, contacts_list[list_string][lines_with_name])
                if len(split_name) > 1:
                    for overwrite_string in range(len(split_name)):
                        contacts_list[list_string][overwrite_string + 2] = split_name[overwrite_string]
    for overwrite_string in range(len(contacts_list)):
        re.split(pattern_phone_number, contacts_list[overwrite_string][5])
        result = re.sub(pattern_phone_number, r"+7(\2)\3-\4-\5 \7\8", contacts_list[overwrite_string][5])
        contacts_list[overwrite_string][5] = result
    return contacts_list


def duplicate_search(list_conversions):
    list_conversions_ = list_conversions
    double_index = []
    for string_for_comparison_1 in range(1, len(list_conversions) - 1):
        for string_for_comparison_2 in range(string_for_comparison_1 + 1, len(list_conversions)):
            if list_conversions[string_for_comparison_2][0] == list_conversions[string_for_comparison_1][0] and list_conversions[string_for_comparison_2][1] == list_conversions[string_for_comparison_1][1]:
                double_index.append(string_for_comparison_1)
                for cells_in_row in range(1, len(list_conversions[1])):
                    if list_conversions[string_for_comparison_2][cells_in_row] == '' and list_conversions[string_for_comparison_1][cells_in_row] != '':
                        list_conversions_[string_for_comparison_2][cells_in_row] = list_conversions[string_for_comparison_1][cells_in_row]
                    elif list_conversions[string_for_comparison_1][cells_in_row] == '' and list_conversions[string_for_comparison_2][cells_in_row] != '':
                        list_conversions_[string_for_comparison_1][cells_in_row] = list_conversions[string_for_comparison_2][cells_in_row]
    for index in double_index:
        index_int = int(index)
        del list_conversions_[index_int]
    return list_conversions_


def file_record(list_conversions):
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(list_conversions)
