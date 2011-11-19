
import sys, re

class PDA:
    def __init__(self, string, current_stack):
        self.string = string
        self.current_stack = current_stack
        
    def RunRule(self, rules):
        variable_regex = re.compile("[A-Z]")
        print "Staring runrule"
        print self.string
        print self.current_stack
        if variable_regex.search(self.current_stack[0]):
            print "Found variable: %s" % self.current_stack[0]
            pda_instances = []
            for rule in rules[self.current_stack[0]]:
                # Copy a new working set
                tmp_set = self.current_stack[:]
                    
                # Add the variable statement
                tmp_set.pop(0)
                if rule != ['!']:
                    tmp_set = rule + tmp_set
                
                print rule
                print "Creating new PDA: %s, %s" % ( self.string, tmp_set)
                pda_instances.append(PDA(self.string, tmp_set))
            return pda_instances
        
        else:
            if self.string.find(self.current_stack[0]) == 0:
                self.string = self.string[len(self.current_stack[0]):len(self.string)+1]
                self.current_stack.pop(0)
                return [ self ] 
            #elif self.current_stack[0] == '!':
                
            else:
                return None
        
    def IsFound(self):
        if len(self.string) == 0 and len(self.current_stack) == 0:
            return True
        else:
            return False
        
    def __str__(self):
        return "%s, %s" % (self.string, str(self.current_stack))
        

def CreatePDA(rules):
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
    
    print "Starting testline"
    working_set = []
    
    # Initialize the working sets
    for initial_rule in parsed_rules['S']:
        working_set.append(PDA(line[:], initial_rule[:]))
    
    print working_set
    working_set_tmp = []
    
    while len(working_set) > 0:
        for pda in working_set:
            print pda
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
    
    for line in sys.stdin.readlines():
        result = TestLine(parsed_rules, line.strip())
        if result:
            print "Yes: %s" % line
        else:
            print "No: %s" % line
    



if __name__ == "__main__":
    main()
