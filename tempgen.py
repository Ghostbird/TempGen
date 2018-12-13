#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 4 14:04:41 2014

@author: Gijsbert “Ghostbird” ter Horst
"""

import argparse
import os
from functools import reduce

def operate(template_path, data_path, output_path):
    """ Write a new copy of the template for each line in the CSV except the first (header) line. Every copy has all occurrences of the values in the CSV header line have been replaced with the corresponding values in its line in the CSV.
    
    Args:
        template_path: The template file path
        data_path: The data file path
        output_path: The output path (must exist)
    """
    # Load the template lines
    with open(template_path,'r', encoding='utf-8') as template_file:
        template = [line for line in template_file]

    # The path extension will be appended to new created files 
    _, extension = os.path.splitext(template_path)

    with open(data_path, 'r', encoding='utf-8') as data_file:
        # The header is the first line of the CSV, minus the terminating newline, split on semicolons.
        placeholders = data_file.readline()[:-1].split(';')

        # Foreach line in the data file
        for line in data_file:
            # Construct a dictionary where the key is the placeholder and the value is the replacement value for this line, minus the terminating newline, split on semicolons
            replacements = dict(zip(placeholders, line[:-1].split(';')))

            # Write the new file, use the output path, the $file_name replacement value from this CSV line and extension from the template
            with open(os.path.join(output_path,replacements['$file_name'] + extension),'w', encoding='utf-8') as f_out:
                f_out.writelines([
                    # Feed the line to a reducer that goes over the replacements and replaces all occurrences of the placeholder with the value.
                    reduce(lambda x, y: x.replace(y[0],y[1]), replacements.items(), line)
                    for line in template
                ])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate template-based files for each line in a CSV file with string replacements.', epilog='The first line of the CSV defines the placeholders. For each subsequent line in the CSV, a new copy of the template is generated where all placeholders have been replaced with the corresponding column entries in that row of the CSV. Note that the value $file_name has a special meaning. This will be the filename for the file generated from that row, the file extension of the template file will be appended.')
    parser.add_argument('template', type=str, help='The template file')
    parser.add_argument('data', type=str, help='The CSV file (semicolon separated) that holds the string replacements.')
    parser.add_argument('-o', '--output_path', type=str, help='The output directory for the generated files.',  default='')
    args = parser.parse_args()
    operate(args.template, args.data, args.output_path)