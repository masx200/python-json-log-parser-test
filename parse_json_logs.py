import json
import re


def find_next_array(log_string, start_index):
    """
    在日志字符串中寻找下一个JSON数组的起始和结束位置。

    参数:
    log_string (str): 包含JSON数组的日志字符串。
    start_index (int): 开始搜索的索引位置。

    返回:
    tuple: 包含数组开始和结束位置的元组，如果没有找到则返回(None, None)。
    """
    print("find_next_array")
    open_braces = 0
    close_braces = 0
    for i in range(start_index, len(log_string)):
        if log_string[i] == '[':
            open_braces += 1
        elif log_string[i] == ']':
            close_braces += 1

        # 当找到一个完整的JSON对象时
        if open_braces > 0 and open_braces == close_braces:
            return start_index, i + 1

    # 如果没有找到完整的JSON对象，返回None
    return None, None


def find_next_object(log_string, start_index):
    """
        在日志字符串中寻找下一个JSON对象的位置。

        该函数尝试从指定的开始索引找到一个完整的JSON对象。它通过计算开括号和闭括号的数量来确定JSON对象的起始和结束位置。

        参数:
        log_string (str): 包含日志信息的字符串，其中可能包含一个或多个JSON对象。
        start_index (int): 开始搜索JSON对象的字符串索引位置。

        返回:
        tuple: 一个元组，包含JSON对象的开始和结束索引位置。如果未找到完整的JSON对象，则返回(None, None)。
        """
    print("find_next_object")
    open_braces = 0
    close_braces = 0
    for i in range(start_index, len(log_string)):
        if log_string[i] == '{':
            open_braces += 1
        elif log_string[i] == '}':
            close_braces += 1

        # 当找到一个完整的JSON对象时
        if open_braces > 0 and open_braces == close_braces:
            return start_index, i + 1

    # 如果没有找到完整的JSON对象，返回None
    return None, None


def parse_json_logs(log_string):
    """
        解析JSON日志字符串。

        该函数接收一个包含JSON对象或数组的日志字符串，并将其解析为Python对象列表。

        参数:
        log_string (str): 包含JSON数据的日志字符串。

        返回:
        list: 解析后的JSON对象列表。
        """
    parsed_jsons = []
    index = 0

    while index < len(log_string):
        start_index, end_index = None, None
        while index < len(log_string) and re.match(r'\s', log_string[index]):
            index += 1
        if not index < len(log_string):
            break
        if log_string[index] == '[':
            start_index, end_index = find_next_array(log_string, index)
        else:
            start_index, end_index = find_next_object(log_string, index)
        if start_index is not None and end_index is not None:
            json_str = log_string[start_index:end_index].strip()
            try:
                parsed_json = json.loads(json_str)
                parsed_jsons.append(parsed_json)
                # print(json_str)
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON: {json_str}")
                print(e)

            index = end_index
        else:
            break

    return parsed_jsons
