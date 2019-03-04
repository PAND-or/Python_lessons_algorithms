#!/usr/bin/python3
__author__ = "Андрей Петров"


"""
2. Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.
"""

from collections import defaultdict

def my_huffman(input_str):
    def _make_dict_list(s):  # модификация из прошлой задачи
        hash_dict = defaultdict(int)

        str_len = len(s)
        for i in range(str_len):  # сдвиг каретки для взятия подстроки
            sub = s[i:i + 1]
            if sub not in hash_dict:  # Если подстрока встретилась первый раз
                for j in range(str_len):  # сдвиг каретки для поиска подстроки
                    if sub == s[j:j + 1]:
                        hash_dict[sub] += 1 #посчет сколько раз встречается
        return hash_dict


    def _make_tree_nodes(nodes, label, result, prefix = ''):
        childs = nodes[label]
        tree = {}
        if len(childs) == 2:
            tree['0'] = _make_tree_nodes(nodes, childs[0], result, prefix+'0')
            tree['1'] = _make_tree_nodes(nodes, childs[1], result, prefix+'1')
            return tree
        else:
            result[label] = prefix
            return label


    def _bin_code(_vals):
        vals = _vals.copy()
        nodes = {}
        for n in vals.keys():
            nodes[n] = []

        while len(vals) > 1:
            s_vals = sorted(vals.items(), key=lambda x:x[1])
            a1 = s_vals[0][0]
            a2 = s_vals[1][0]
            vals[a1+a2] = vals.pop(a1) + vals.pop(a2)
            nodes[a1+a2] = [a1, a2]
        code = {}
        root = a1+a2
        tree = _make_tree_nodes(nodes, root, code)
        return code, tree


    def _encode(s, code):
        res = []
        for t in s:
            res.append(code[t])
        return res


    code, tree = _bin_code(_make_dict_list(input_str))

    return _encode(input_str, code), code, tree


result = my_huffman('beep boop beer!')
print(f'encoded str {result[0]}, \ncode_dict: {result[1]}, \ncodetree: {result[2]}')
