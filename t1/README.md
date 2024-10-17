# Rule Engine with AST

## Overview
A simple 3-tier rule engine that evaluates user eligibility based on various attributes using Abstract Syntax Trees.

## Installation
1. Clone the repository.
2. Install dependencies (if any).
3. Set up the database schema using the provided SQL.

## API Endpoints
- `create_rule(rule_string)`: Creates a rule and returns its AST.
- `combine_rules(rules)`: Combines multiple rules into a single AST.
- `evaluate_rule(ast, data)`: Evaluates the AST against provided user data.

## Non-Functional Requirements
### Security
- Basic input validation implemented to avoid injection attacks.

### Performance
- Optimized AST evaluation with minimal redundant checks.

## Testing
Includes various test cases for rule creation, combination, and evaluation.