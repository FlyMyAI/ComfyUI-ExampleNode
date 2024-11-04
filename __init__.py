from .example_nodes import ExampleT2IFMANode

NODE_CLASS_MAPPINGS = {
    "ExampleT2IFMANode": ExampleT2IFMANode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ExampleT2IFMANode": "FlyMyAI example node T2I"
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
