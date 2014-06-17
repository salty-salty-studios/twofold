init -499 python:
    ## Fix broken SetField when object doesn't have the target field set already.
    #   <Shiz> renpytom: bug report                                                
    #   <Shiz> SetVariable only works if the variable already exists in the store  
    #   <Shiz> because else is_selected will crash                                 
    #   <renpytom> Not a bug.                                                          
    #   <Shiz> why not?                                                            
    #   <renpytom> I think leaving a variable undefined is kind of nonsensical.  
    # My ass.      
    SetField.get_selected = lambda self: hasattr(self.object, self.field) and getattr(self.object, self.field) == self.value
