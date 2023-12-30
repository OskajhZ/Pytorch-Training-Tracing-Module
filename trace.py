# Copyright 2023 Xiangnan Zhang, School of Future Technology, Beijing Institute of Technology

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import pickle
import torch
import os
import matplotlib.pyplot as plt

class Statistic():
    def __init__(self,path):
        self.train_loss=[]
        self.train_accuracy=[]
        self.test_loss=[]
        self.test_accuracy=[]
        self.path=path
        
    def save(self):
        with open(os.path.join(self.path,"object.pkl"),"wb") as file:
            pickle.dump(self,file,protocol=pickle.HIGHEST_PROTOCOL)
        file.close()
        
    def draw(self,name):
        plt.subplot(2,2,1)
        plt.plot(self.train_loss)
        plt.title("Train Loss")
        plt.xlabel("Adjustment Times")

        plt.subplot(2,2,2)
        plt.plot(self.train_accuracy)
        plt.title("Train Accuracy")
        plt.xlabel("Adjustment Times")

        plt.subplot(2,2,3)
        plt.plot(self.test_loss)
        plt.title("Test Loss")
        plt.xlabel("Batch Number")

        plt.subplot(2,2,4)
        plt.plot(self.test_accuracy)
        plt.title("Test Accuracy")
        plt.xlabel("Batch Number")

        plt.suptitle(f"{name} Training Monitor")

        plt.tight_layout()
        plt.savefig(os.path.join(self.path,"Train_monitor.png"))
        plt.show()
        
        self.save()
        
def load_statistic(path):
    with open(os.path.join(path,"object.pkl"),"rb") as file:
        statis=pickle.load(file)
    file.close()
    return statis

def sys_load(model_path,statis_path):
    statis=load_statistic(statis_path)
    model=torch.load(model_path)
    return (model,statis)

class Sys():
    def __init__(self,model,model_path,statis):
        self.model=model
        self.model_path=model_path
        self.statis=statis
        
    def sys_conclude(self,name):
        torch.save(self.model,self.model_path)
        self.statis.draw(name)
        print("Model and statis saved. Adjustment times: %d" %(len(self.statis.train_loss)))
        