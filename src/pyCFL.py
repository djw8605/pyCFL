
import sys, re

class PDA:
    def __init__(self, string, current_stack):
        if string == '!':
            self.string = ""
        else:
            self.string = string
        self.current_stack = current_stack
        
    def RunRule(self, rules):
        """
        Function to run a set of rules given the current stack
        and the currently unparsed string.
        """
        
        variable_regex = re.compile("[A-Z]")
        #print "Staring runrule"
        #print self.string
        #print self.current_stack
        if len(self.current_stack) == 0:
            return None
        
        # Check if the current stack is a variable
        if variable_regex.search(self.current_stack[0]):
            #print "Found variable: %s" % self.current_stack[0]
            pda_instances = []
            for rule in rules[self.current_stack[0]]:
                # Copy a new working set
                tmp_set = self.current_stack[:]
                    
                # Add the variable statement
                tmp_set.pop(0)
                if rule != ['!']:
                    tmp_set = rule + tmp_set
                
                #print rule
                #print "Creating new PDA: %s, %s" % ( self.string, tmp_set)
                pda_instances.append(PDA(self.string, tmp_set))
            return pda_instances
        
        else:
            # If the current stack is a constant, then make sure the string matches
            if self.string.find(self.current_stack[0]) == 0:
                self.string = self.string[len(self.current_stack[0]):len(self.string)+1]
                self.current_stack.pop(0)
                return [ self ] 
            elif len(self.string) == 0 and self.current_stack[0] == '!':
                self.current_stack.pop(0)
                return [self]
            else:
                return None
        
    def IsFound(self):
        """
        Check if this PDA has found a correct string.  
        Which is true when the parsed string and current stack is empty.
        """
        if len(self.string) == 0 and len(self.current_stack) == 0:
            return True
        else:
            return False
        
    def __str__(self):
        return "%s, %s" % (self.string, str(self.current_stack))
        

def CreatePDA(rules):
    """
    Create the PDA given the rules above.
    Really this just parses out the rules correctly.
    """
    rule_regex = re.compile("([A-Z])->([\w|\!]*)")
    substition_regex = re.compile("([A-Z])")
    variables = {}
    
    for rule in rules:
        rule_object = rule_regex.search(rule)
        if rule_object is None:
            print "Error parsing rule: " + rule
        (variable, transform) = rule_object.groups()
        
        constants = substition_regex.split(transform)
        
        # Remove blank entries
        while '' in constants:
            constants.remove('')
        
        if not variables.has_key(variable):
            variables[variable] = []
        variables[variable].append(constants)
        
        
        
    return variables


def TestLine(parsed_rules, line):
    """
    This function runs the parsed rules on the line.
    It performs a breadth first search of the PDA instances.
    """
    
    #print "Starting testline"
    working_set = []
    
    # Initialize the working sets
    for initial_rule in parsed_rules['S']:
        working_set.append(PDA(line[:], initial_rule[:]))
    
    #print working_set
    working_set_tmp = []
    
    # Run the working sets until there are no valid ones left
    while len(working_set) > 0:
        for pda in working_set:
            #print pda
            pdas = pda.RunRule(parsed_rules)
            
            if pdas is not None:
                for pda_returns in pdas:
                    if pda_returns.IsFound():
                        return True
                working_set_tmp += pdas
        working_set = working_set_tmp
        working_set_tmp = []
    
    


def main():
    # Read in input
    number_of_rules = int(sys.stdin.readline().strip())
    
    rules = []
    for i in range(number_of_rules):
        rules.append(sys.stdin.readline().strip())
        
    parsed_rules = CreatePDA(rules)
    
    # Read in stdin
    for line in sys.stdin.readlines():
        try:
            result = TestLine(parsed_rules, line.strip())
            if result:
                print "Yes"
            else:
                print "No"
        except:
            print "No"
       
    



if __name__ == "__main__":
    main()
