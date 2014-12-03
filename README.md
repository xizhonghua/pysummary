#pystats

pystats is a python script for simple statistics tasks. pystats read from stand input by defualt, and use space as seperator.

### Install
1. download/clone the repository
2. `make install`

### Usage
Unix/Linux/Mac OS
 * `./pystats [options]`
 * Examples
   * `cat data.txt | ./pystats` or `./pystats < data.txt`
   * Output:
   ```
_______Field = 1
_______Lines = 26
________Mean = 4.80769230769
____Variance = 4.77071005917
______StdDev = 2.18419551762
_________Sum = 125.0
_________Min = 0.0
_________Max = 9.0
______Median = 5.0 
   ```
   * summarize 2nd field of a comma separated values (csv) file, skip first line (header)
   * `cat data.csv | ./pystats -d',' -f2 -s1`

### Options
| Option | Description |
|:------:|:-----------:|
| -f#    | field/column index (start from 1) |
| -d#    | delimiter   |
| -s#    | skip first # lines |
| -h     | print help  |

### Tips
* Make pystats.py as a command
    * Unix/Linux
        * copy pystats.py into a folder that is in PATH e.g., `/local/usr/bin`, `/opt/local/bin`.
    * Windows
        * TBD

### Dependencies
* None

### Contact
* Zhonghua Xi [xizhonghua@gmail.com](mailto:xizhonghua@gmail.com?subject=pystats)
