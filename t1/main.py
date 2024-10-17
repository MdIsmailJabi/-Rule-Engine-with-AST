import operator

# === Node Class for the AST ===
class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # 'operand' or 'operator'
        self.value = value  # Operator ('AND', 'OR') or operand (like 'age > 30')
        self.left = left  # Left child node
        self.right = right  # Right child node

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value})"

# === Parsing Logic ===
def parse_rule(rule_string):
    """Parse a rule string and build an AST."""
    tokens = rule_string.replace('(', ' ( ').replace(')', ' ) ').split()
    print(f"Tokens: {tokens}")  # Debugging tokens output
    return build_ast(tokens)

def build_ast(tokens):
    """Build an AST from a list of tokens."""
    def parse_expression(token_iter):
        stack = []  # Holds nodes and operators
        current_token = None

        while True:
            try:
                current_token = next(token_iter)
            except StopIteration:
                break
            
            print(f"Current Token: {current_token}")  # Debugging output

            if current_token == '(':
                # Start of a new nested expression
                stack.append(parse_expression(token_iter))
            elif current_token == ')':
                # End of a nested expression
                break
            elif current_token in {'AND', 'OR'}:
                # Check that we have enough operands for the operator
                if len(stack) < 2:
                    raise ValueError("Invalid expression: not enough operands for operator.")
                right = stack.pop()  # Right operand
                left = stack.pop()  # Left operand
                operator_node = Node(node_type='operator', value=current_token, left=left, right=right)
                print(f"Created Operator Node: {operator_node}")  # Debugging output
                stack.append(operator_node)  # Push operator node onto the stack
            else:
                # Directly append operands (conditions)
                stack.append(Node(node_type='operand', value=current_token))

        # Validate that the stack contains exactly one expression after processing
        if len(stack) != 1:
            raise ValueError("Invalid rule syntax: Could not build AST. Stack length: {}".format(len(stack)))

        return stack[0]  # Return the root of this expression

    return parse_expression(iter(tokens))

def create_rule(rule_string):
    """API: Create a rule (AST) from a rule string."""
    try:
        return parse_rule(rule_string)
    except Exception as e:
        raise ValueError(f"Invalid rule string: {e}")

# === Example Test Cases ===
if __name__ == "__main__":
    rule1_string = (
        "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) "
        "AND (salary > 50000 OR experience > 5)"
    )

    # Create rules from strings
    try:
        rule1 = create_rule(rule1_string)
        # Print the constructed AST for rule1
        print("Constructed AST for Rule 1:")
        print(rule1)
    except ValueError as e:
        print(e)
