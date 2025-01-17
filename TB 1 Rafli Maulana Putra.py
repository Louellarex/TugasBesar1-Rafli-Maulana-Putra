# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PkECd-JbkzeiwBGqdeSKjCnOXCUZ7JSW
"""

import re

def read_matrix_from_file(filename):
    try:
        with open(filename, 'r') as f:
            num_rows, num_cols = map(int, f.readline().strip().split())
            matrix = [line.strip() for line in f]
        return matrix, num_cols
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit()

def decode_message_from_matrix(matrix, num_cols):
    decoded_message = ""
    for col in range(num_cols):
        for row in range(len(matrix)):
            try:
                decoded_message += matrix[row][col]
            except IndexError:
                decoded_message += ' '
    return decoded_message

def clean_message_text(decoded_message):
    pattern = r'(?<=[\w])[^\w]+(?=[\w])'
    match_msg = re.findall(pattern, decoded_message)
    for non_word_char in match_msg:
        decoded_message = decoded_message.replace(non_word_char, ' ', 1)
    return decoded_message

filename = 'neomatrix.txt'

try:
    matrix, num_cols = read_matrix_from_file(filename)
    decoded_message = decode_message_from_matrix(matrix, num_cols)
    cleaned_message = clean_message_text(decoded_message)

    with open("result.txt", "w") as result_file:
        result_file.write(cleaned_message)

    print(f"Decoded Message:\n{cleaned_message}\nThe result is written in result.txt!")
except Exception as e:
    print(f"An error occurred: {e}")