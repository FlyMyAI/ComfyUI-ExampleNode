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
