
from torch import hub

def get_model(Tools):
   Model_Path=Tools.feedback_Model_Filepath()
   print(Model_Path)
   model = hub.load(r'C:\yolov5', 'custom', path=Model_Path, source='local')
   return model

