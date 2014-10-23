

class SimpleBot:
    
    order = None
    order_roam = 1
    order_defend = 2
    order_patrol = 3
    order_assist = 4
    order_attack = 5
    
    state = None
    state_idle = 1
    state_attacking = 2
    state_traveling = 3
    
    path = None
    vehicle = None
    
    def update (self):
        
        if self.state == self.state_idle:
            
            if self.order == self.order_roam:
                # pick new random waypoint
                # set state to state_traveling
            elif self.order == self.order_defend:
                # is at base?
                #   get path to base
                #   set state to state_traveling
                # are enemeis in sight?
                #   set state to state attacking
                # is another defender being attacked?
                #   get path to line of fire
                #   set state to state_traveling
                # are other defending units being attacked?
                #   get path to attacker
                #   set state to state_traveling
            elif self.order == self.order_patrol:
                # are enemeis in sight?
                #   set state to state attacking
                # is end of path reached?
                #   is end of path also beginning of path
                #       set state to state_traveling
                #   else
                #       invert path
                #       set state to state_traveling
            elif self.order == self.order_assist:
                # are enemeis in sight?
                #   set state to state attacking
                # is team leader not at end of path?
                #   get path to team leader
                # set state to state_traveling
            elif self.order == self.order_attack:
                # 
                
                
        elif self.state == self.state_traveling:
            
        elif self.state == self.state_attacking:
    
