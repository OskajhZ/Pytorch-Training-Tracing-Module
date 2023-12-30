# A Pytorch Training Process Tracing Module
**Xiangnan Zhang**

**School of Future Technology, Beijing Institute of Technology**

<br/>
This module called "trace" is used to trace whole traning process, as well as realize visualization of accuracy and loss. 

All loss and accuracy can be traced via a Statistic object. During training and testing, these data will be appended to its list-format attributes. The model and traning data will
be saved and loaded at the same time, hence to guarantee the whole-traning-process tracing. While saving the model and traning data, line charts of loss and accuracy will be shown and saved as follows.

![image](https://userblink.csdnimg.cn/direct/f369e83f57c94812b20778c958e78681.png)
## Importing
In terms of importing this module, you should code as follows:
```
import trace
from trace import Statistic
```
**NOTICE**: The class Statistic() should be imported separately, because it is the preriquisit of function ```load_statistic()``` and ```sys_load()```.
## Details
### ```Statistic(path)```
Objects that belong to this class stores traning and testing loss and accuracy. So when you are initializing your model, you should create a Statistic like this:
```
statis=Statistic(statis_path)
```
its ```__init__()```method will establish attributes ```self.train_loss```, ```self.train_accuracy```, ```self.test_loss``` and ```self.test_accuracy```. Each of them are empty list, so you can 
use ```.append()``` method to append values in your train_loop and test_loop functions, like this:
```
def test_loop(test_ds,model,loss_fn,statis):
    model.eval()
    ...
    statis.test_loss.append(test_loss)
    statis.test_accuracy.append(accuracy)
    ...
```
There are two methods for Statistic project called ```self.draw()``` and ```self.save```, which can be used to draw statistical images and save Statistic object as pkl files. However, in most cases you should use Sys object's ```.sys_conclude()``` method instead.
### ```load_statistic(path)```
This function is used to load a Statistic object. But in most cases, you should use ```sys_load()``` function instead.
### ```sys_load(model_path,statis_path)```
This function is used to load both model and Statistic object. It is highly recommended that you use this function to load these two items, because it can guarentee that model and Statistic object can be loaded at the same time.
### ```Sys(model,model_path,statis)```
This class aims to process model and Statistic object at the same time. You should create a Sys project after the model and Statistic object are loaded or iinitialized, like this:
```
syst=trace.Sys(model,model_path,statis)
```
Then you can use ```.sys_conclude()``` method to save both the model and Statistic object:
```
syst.sys_conclude("ConvM(4_categ)")
```
A string that represents the model should be given when using this method. When you need to save your model and Statistic object, this method is always highly recommended.

<br/>
After saving, the model will be saved as a pth file, and the Statistic object will be saved as a pkl file. These suffixes should be included into file paths.

## Deficiency
When using this module to trace data, train_loss will dramatically increase at the begining of a new training process, which can be seen in the front image. However, I'm not sure whether it is the module's problem, or it is my model's problem.
