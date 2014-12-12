#pystats.py

pystats.py is a python script for summary statistics. pystats.py reads from stand input, uses space as fields delimiter by defualt and outputs to stand output.

### Install
1. download/clone the repository
2. Unix/Linux `make install`, **pystats.py** will be installed to `/usr/local/bin`
3. Windows users please read [tips](#tips) first

### Usage
 * `pystats.py [options]`

### Options
| Option | Description |
|:------:|:-----------:|
| -f#    | field/column index (start from 1) |
| -d#    | delimiter   |
| -s#    | skip first # lines |
| -p#    | set print precision |
| -c#    | set confidence |
| -i#    | NA value to ignore |
| -h     | print help  |



### Examples
 * Use case: basic summary on single column text file
 * `cat data.txt | pystats.py` Unix/Linux, PowerShell on Windows
 * `pystats.py < data.txt` Unix/Linux, cmd.exe on Windows
 * Output:
```
_______Field = 1
_______Lines = 26
________Mean = 4.80769
____Variance = 4.77071
______StdDev = 2.18420
_________Sum = 125.00000
_________Min = 0.00000
_________Max = 9.00000
______Median = 5.00000
__Confidence = 0.95000
___Cnf.Itv.L = 3.90801
___Cnf.Itv.U = 5.70738
```
----
  * Use case: summarize 2nd field of a comma separated values (csv) file, skip first line (header)
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
________Mean = 3.00000
____Variance = 5.00000
______StdDev = 2.23607
_________Sum = 12.00000
_________Min = 0.00000
_________Max = 6.00000
______Median = 3.00000
__Confidence = 0.95000
___Cnf.Itv.L = -1.10852
___Cnf.Itv.U = 7.10852
```

* Use pystats as a module
```python
from pystats import *
with open('data.txt') as f:
    res = stats(stream = f, field=1, delimiter=' ', skip = 0, confidence=0.95)
    print res

# field, lines, mean, variance, std dev, sum, min, max, median, confidence interval
# (1, 26, 4.8076923076923075, 4.770710059171598, 2.18419551761549, 125.0, 0.0, 9.0, 5.0, (3.9080053326363, 5.707379282748315))
```

### Tips

* Make pystats.py as a command on Windows
 1. create a bin folder under current user's home folder. PowerShell `mkdir ~/bin`
 2. copy **pystats.py** to that folder. PowerShell `cp pystats.py ~/bin`
 3. add `C:/Users/YOURNAME/bin` to `PATH` variable
 4. add `.py` to `PATHEXT` variable to make python script executable


### Dependencies
* NumPy
* SciPy

### Contact
* Zhonghua Xi [xizhonghua@gmail.com](mailto:xizhonghua@gmail.com?subject=pystats)
