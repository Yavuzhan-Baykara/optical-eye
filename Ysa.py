
from torch import hub

def get_model(Tools):
   Model_Path=Tools.feedback_Model_Filepath()
   model = hub.load(r'.\yolov5', 'custom', path=Model_Path, source='local')
   return model

