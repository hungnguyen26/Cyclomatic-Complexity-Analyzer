import ast

class ComplexityAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.complexity = 1
        self.cfg_edges = []
        self.current_node_id = 0
        self.prev_node_id = None

    def visit_FunctionDef(self, node):
        self.complexity = 1
        self.cfg_edges = []
        self.current_node_id = 0
        self.prev_node_id = "start"

        self.cfg_edges.append(("ENTRY", "start"))
        self.generic_visit(node)

    def _add_node(self, label):
        node_id = f"{label}_{self.current_node_id}"
        self.cfg_edges.append((self.prev_node_id, node_id))
        self.prev_node_id = node_id
        self.current_node_id += 1

    def visit_If(self, node):
        self.complexity += 1
        self._add_node("if")
        self.generic_visit(node)

    def visit_For(self, node):
        self.complexity += 1
        self._add_node("for")
        self.generic_visit(node)

    def visit_While(self, node):
        self.complexity += 1
        self._add_node("while")
        self.generic_visit(node)

    def visit_Expr(self, node):
        self._add_node("expr")
        self.generic_visit(node)

    def visit_Assign(self, node):
        self._add_node("assign")
        self.generic_visit(node)

    def visit_Return(self, node):
        self._add_node("return")
