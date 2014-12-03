#pystats

pystats is a python script for simple statistics tasks. pystats read from stand input by defualt, and use space as seperator.

### Usage
* Unix/Linux/Mac OS
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

### Options
| Option | Description |
|:------:|:-----------:|
| -f#    | field/column index (start from 1) |
| -s#    | seperator   |
| -h     | print help  |

### Tips
* Make pystats.py as a command
    * Unix/Linux
        * copy pystats.py into a folder that is in PATH; such as `/local/usr/bin`, `/opt/local/bin`, etc.
    * Windows
        * TBD

### Dependencies
* None

### Contact
* Zhonghua Xi [xizhonghua@gmail.com](mailto:xizhonghua@gmail.com?subject=pystats)
