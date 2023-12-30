# Pytorch-Training-Tracing-Module
This module called "trace" is used to trace whole traning process, as well as draw statistical graph and save model/data. 
## Importing
In terms of importing this module, you should code as follows:
```
import trace
from trace import Statistic
```
NOTICE: The class Statistic() should be imported separately, because it is the preriquisit of function ```load_statistic()``` and ```sys_load()```.
## Details
### ```Statistic(path)```
### ```load_statistic(path)```
### ```sys_load(model_path,statis_path)```
### ```Sys(model,model_path,statis)```
