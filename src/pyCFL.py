
import sys, re


def CreatePDA(rules):
    rule_regex = re.compile("([A-Z])->([\w]*)")
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
    pass
    
    


def main():
    # Read in input
    number_of_rules = int(sys.stdin.readline().strip())
    
    rules = []
    for i in range(number_of_rules):
        rules.append(sys.stdin.readline().strip())
        
    parsed_rules = CreatePDA(rules)
    
    for line in sys.stdin.readlines():
        TestLine(parsed_rules, line)
    



if __name__ == "__main__":
    main()
