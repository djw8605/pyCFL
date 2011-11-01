
import sys, re


def CreatePDA(rules):
    rule_regex = re.compile("([A-Z])->([\w|!|]+)")
    
    for rule in rules:
        rule_object = rule_regex.search(rule)
        if rule_object is None:
            print "Error parsing rule: " + rule
        
        rule


def main():
    # Read in input
    number_of_rules = int(sys.stdin.readline().strip())
    
    rules = []
    for i in range(number_of_rules):
        rules.append(sys.stdin.readline().strip())
        
    print rules
    
    
    



if __name__ == "__main__":
    main()
