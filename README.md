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
| -h     | print help  |



### Examples
 * Use case: basic summary on single column text file
 * `cat data.txt | pystats.py` Unix/Linux, PowerShell on Windows
 * `pystats.py < data.txt` Unix/Linux, cmd.exe on Windows
 * Output:
```
=======Field = 1
=======Lines = 26
========Mean = 4.80769
====Variance = 4.77071
======StdDev = 2.18420
=========Sum = 125.00000
=========Min = 0.00000
=========Max = 9.00000
======Median = 5.00000
==Confidence = 0.95000
=Cnf. Itv. L = 3.90801
=Cnf. Itv. U = 5.70738
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
=======Field = 2
=======Lines = 4
========Mean = 3.00000
====Variance = 5.00000
======StdDev = 2.23607
=========Sum = 12.00000
=========Min = 0.00000
=========Max = 6.00000
======Median = 3.00000
==Confidence = 0.95000
=Cnf. Itv. L = -1.10852
=Cnf. Itv. U = 7.10852
```


### Tips

* Make pystats.py as a command on Windows
 1. create a bin folder under current user's home folder. PowerShell `mkdir ~/bin`
 2. copy **pystats.py** to that folder. PowerShell `cp pystats.py ~/bin`
 3. add `C:/Users/YOURNAME/bin` to `PATH` variable
 4. add `.py` to `PATHEXT` variable to make python script executable


### Dependencies
* None

### Contact
* Zhonghua Xi [xizhonghua@gmail.com](mailto:xizhonghua@gmail.com?subject=pystats)
