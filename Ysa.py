
import torch
from ToolKit import ToolKit



def get_model(Tools):
   Model_Path=Tools.feedback_Model_Filepath()
   print(Model_Path)
   model = torch.hub.load(r'C:\yolov5', 'custom', path=Model_Path, source='local')
   return model

