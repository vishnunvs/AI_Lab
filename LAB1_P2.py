
#---------------Program2-template--------------------
#Bunny needs help 2-dimensional
class shore:
        loc_x = 10
        loc_y = 10

        """Class to define the environment."""
        def __init__(self,agent_x_loc,agent_y_loc):
                #location of the agent 
                self.agent_x_loc = agent_x_loc
                self.agent_y_loc = agent_y_loc
        def percept(self,total_steps,u_steps,d_steps,l_steps,r_steps,direction):
                """input: agent location
                output: shore reached or not"""
                if total_steps!=0:
                        print(self.agent_x_loc,"\t\t",self.agent_y_loc,"\t\t",direction)
                # update agent location
                 
                #give perception
                if self.agent_x_loc == loc_x && self.agent_y_loc == loc_y:
                        return 1
                else:
                        return 0
        
class agent:
        """Class that defines agent"""
        
        def move_left(self):
                    """Perform action moves left"""
            
                          
        def move_right(self):
                    """Perform action moves right"""
        
        def move_up(self):
                    """Perform action moves up"""
            
                          
        def move_down(self):
                    """Perform action moves down"""
        
       
        
        

        
        

