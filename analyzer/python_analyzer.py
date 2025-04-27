import ast

class ComplexityAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.complexity = 0

    def visit_If(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.complexity = 1  
        self.generic_visit(node)
        print(f"Hàm '{node.name}' có độ phức tạp: {self.complexity}")
        return self.complexity

def analyze_file(file_path):
    with open(file_path, "r") as source:
        tree = ast.parse(source.read())
    
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            analyzer = ComplexityAnalyzer()
            analyzer.visit(node)
