def change_cell_output(show="all"):
    """
    Changes how many statements are shown after Jupyter cell evaluation.

    Default is 'last_expr'.

    Options are 'all', 'last', 'last_expr', 'none', 'last_expr_or_assign'.
    
    I usually want all outputs, so 'all' is the default.
    """
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = show
    return None