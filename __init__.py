import os                                                                                            
import importlib                                                                                     
                                                                                                     
# Get the directory of the current file                                                              
current_dir = os.path.dirname(__file__)                                                              
                                                                                                     
# Iterate over all files in the directory                                                            
for filename in os.listdir(current_dir):                                                             
    if filename.endswith('.py') and filename != '__init__.py':                                       
        module_name = filename[:-3]  # Remove the .py extension                                      
        module = importlib.import_module(f'.{module_name}', package=__name__)                        
        globals().update(vars(module))                                                               
                                       
