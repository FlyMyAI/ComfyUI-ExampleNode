# ComfyUI-ExampleNode
Node to provide convenient ComfyUI standard, supported by flymy_comfyui. 

1.  `install.py` script is launched with ComfyUI-Manager
2. `nodes/__init__.py` should contain `__all__` attribute as provided 
```python
NODE_CLASS_MAPPINGS = {
    "some name": object
}
NODE_DISPLAY_NAME_MAPPINGS = {}  # this var does not affect anything at all
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
```
3. `requirements.txt` - default Python dependency map. Do not override `numpy` - we restrict this action with our engine. We strongly recommend to launch `pip freeze > requirements.txt` command

Do not add `.dont_pack_those_files` files to your repository - it's not used by flymy_comfyui.

# Cases
1. If there are nodes that can be installed with ComfyUI-Manager [https://github.com/ltdrdata/ComfyUI-Manager/blob/main/custom-node-list.json] - you do not have to edit these nodes.
2. If there are nodes that should be installed with git and requires any **manual** setup - you have to provide `install.py` script.
3. If there are python requirements that should be edited - provide custom repo with `requirements.txt` file. Python requirements are installed (sequentially) at the initialization of a pipeline.
