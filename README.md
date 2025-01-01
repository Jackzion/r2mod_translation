# r2mod_translation
### a mini tool to translate r2 mods .language
## first step -- replace your text_translation API keys

I give a translation api demo with youdao apis

```python
# translate_demo.py
app_key = 'xxxxxxxx'
app_secret = 'xxxxxxxx'
from_lang = 'en'
to_lang = 'zh-CHS'
```

## second step -- replace the file path you wish to translate

```python
# main.py
root_path = r'xxxxxxx'
process_en_files_and_folders(root_path)
```

## last step -- start python main.py
