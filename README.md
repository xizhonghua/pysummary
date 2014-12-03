#pystats.py

pystats.py is a python script for simple statistics tasks. pystats read from stand input and use space as seperator by defualt.

### Install
1. download/clone the repository
2. `make install` 
3. **pystats.py** will be installed to `/usr/local/bin`

### Usage
Unix/Linux/Mac OS
 * `pystats.py [options]`

### Options
| Option | Description |
|:------:|:-----------:|
| -f#    | field/column index (start from 1) |
| -d#    | delimiter   |
| -s#    | skip first # lines |
| -h     | print help  |


### Examples
   * `cat data.txt | pystats.py` or `pystats.py < data.txt`
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
   * Input:
   ```
"c1","c2","c3","c4"
1,2,3,4
5,6,7,8
9,0,1,2
3,4,5,6
```
   * `cat data.csv | pystats.py -d',' -f2 -s1`
   * Output:
   ```
_______Field = 2
_______Lines = 4
________Mean = 3.0
____Variance = 5.0
______StdDev = 2.2360679775
_________Sum = 12.0
_________Min = 0.0
_________Max = 6.0
______Median = 3.0
   ```

### Tips
* Make pystats.py on Windows
  * TBD 

### Dependencies
* None

### Contact
* Zhonghua Xi [xizhonghua@gmail.com](mailto:xizhonghua@gmail.com?subject=pystats)
