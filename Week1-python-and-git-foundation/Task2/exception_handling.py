"""Exception-Safe Calculator | try/except/else/finally"""

import operator

class DivisionByZeroError(Exception):
    pass

class InvalidOperationError(Exception):
    pass

class Calculator:
    def __init__(self):
        self.history = []
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '**': operator.pow,
        }
    
    def calculate(self, num1, num2, operation):
        result = None
        error_occurred = False
        
        try:
            if operation not in self.operations:
                raise InvalidOperationError(f"Invalid operation: {operation}")
            
            if operation == '/' and num2 == 0:
                raise DivisionByZeroError("Cannot divide by zero")
            
            result = self.operations[operation](num1, num2)
            
        except DivisionByZeroError as e:
            print(f"Error: {e}")
            error_occurred = True
        except InvalidOperationError as e:
            print(f"Error: {e}")
            error_occurred = True
        except Exception as e:
            print(f"Unexpected error: {e}")
            error_occurred = True
        else:
            print(f"Success: {num1} {operation} {num2} = {result}")
        finally:
            self.history.append({
                'num1': num1,
                'num2': num2,
                'operation': operation,
                'result': result,
                'error': error_occurred
            })
        
        return result
    
    def show_history(self):
        print("\n=== Calculation History ===")
        for i, record in enumerate(self.history, 1):
            status = "ERROR" if record['error'] else "SUCCESS"
            print(f"{i}. {record['num1']} {record['operation']} {record['num2']} = {record['result']} [{status}]")

if __name__ == "__main__":
    calc = Calculator()
    
    print("Exception Handling Demo =-\n")
    
    calc.calculate(10, 5, '+')
    calc.calculate(20, 4, '*')
    calc.calculate(10, 0, '/')
    calc.calculate(10, 5, '^')
    calc.calculate(2, 3, '**')
    
    calc.show_history()
