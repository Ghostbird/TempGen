# Tempgen

This is an improved version of a script I wrote a long time ago.

You pass it:

* A template file
* A semicolon separated CSV file
* _Optionally_ an output directory (must exist)

You will receive a new copy of the template for each line in the CSV except the first (header) line. In that copy all occurrences of the values in the CSV header line have been replaced with the corresponding values in the CSV line this file was generated from.

The filename of the generated file will correspond to the value in the column with the header `$file_name`, with the extension of the template appended.

## Example

### Input

#### template.txt

```text
Roses are $foo, violets are $bar.
The sky is $bar, the bar is $bar.
The $foo is bar, the foe is $bar.
```

#### test.csv


```csv
$file_name;$foo;$bar
file_1;red;blue
file_2;yellow;green
```
**Note:** The CSV file must have a final newline, otherwise the last replacement value is `gree`.

### Output

#### file_1.txt

```text
Roses are red, violets are blue.
The sky is blue, the bar is blue.
The red is bar, the foe is blue.
```

#### file_2.txt

```text
Roses are yellow, violets are green.
The sky is green, the bar is green.
The yellow is bar, the foe is green.
```