import json
import json5
import re
import os
from translate import Translator
import translate_demo

# 将 en_f 翻译并替代
def extract_and_translate(input_file):
    # import json and take 'strings'
    try:
        with open(input_file,'r',encoding='utf-8-sig') as file:
            content = file.read()
            # 替换未被转义的换行符
            content = re.sub(r'(?<!\\)\n', '\\n', content) 
            # 替换空字符串 "" 为合法的 JSON 值 null
            cleaned_content = re.sub(r':\s*""', ': null', content)
            data = json.loads(cleaned_content)
            
        strings = data.get("strings",{})
        # handle key : value in strings , translate the vlaue
        for key , value in strings.items():
            # handle xml tags
            if re.search(r'<.*?>',value):
                text_parts = re.findall(r'>([^<>]+)<',value)
                translate_parts =  [translate_text(part) for part in text_parts]
                # replace all text parts
                for original , translated in zip(text_parts,translate_parts):
                    value = value.replace(original,translated)
            # handle normal strings
            else:
                value = translate_text(value)
            # flash
            strings[key] = value
        # save .json file
        with open(input_file,'w',encoding='utf-8') as file:
            json.dump(data,file,ensure_ascii=False, indent=4)
        local_result_path = input_file.replace('/', '_').replace('\\', '_')
        with open(local_result_path,'w',encoding='utf-8') as file:
            json.dump(data,file,ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"fail to translate : {e}")
    return 

# 比较 en_f 与 cn_f save in cn_f
def compare_and_translate(en_file,cn_file):
    print(f'。。。。{en_file} :: {cn_file}')
    # import json and take 'strings'
    try:
        with open(en_file,'r',encoding='utf-8-sig') as file:
            en_content = file.read()
            # 替换未被转义的换行符
            en_content = re.sub(r'(?<!\\)\n', '\\n', en_content) 
            # 替换空字符串 "" 为合法的 JSON 值 null
            en_content = re.sub(r':\s*""', ': null', en_content)
            en_data = json.loads(en_content)
            en_strings = en_data.get("strings",{})        
        with open(cn_file,'r',encoding='utf-8-sig') as file:
            cn_content = file.read()
            # 替换未被转义的换行符
            cn_content = re.sub(r'(?<!\\)\n', '\\n', cn_content) 
            # 替换空字符串 "" 为合法的 JSON 值 null
            cn_content = re.sub(r':\s*""', ': null', cn_content)
            cn_data = json.loads(cn_content)
            cn_strings = cn_data.get("strings",{})
            
        for en_key , en__value in en_strings.items():
            if en_key not in cn_strings.keys():
                temp_value = en__value
                # handle xml tags
                if re.search(r'<.*?>',temp_value):
                    text_parts = re.findall(r'>([^<>]+)<',temp_value)
                    translate_parts =  [translate_text(part) for part in text_parts]
                    # replace all text parts
                    for original , translated in zip(text_parts,translate_parts):
                        temp_value = temp_value.replace(original,translated)
                # handle normal strings
                else:
                    temp_value = translate_text(temp_value)
                # new key:value
                cn_strings[en_key] = temp_value
                # save .json file
                with open(cn_file,'w',encoding='utf-8') as file:
                    json.dump(cn_data,file,ensure_ascii=False, indent=4)
                local_result_path = cn_file.replace('/', '_').replace('\\', '_')
                with open(local_result_path,'w',encoding='utf-8') as file:
                    json.dump(cn_data,file,ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"fail to translate : {e}")
    return 

def translate_text(text):
    return translate_demo.translate(text)

