import os 
import json

def scan_json_files(folder_path):
    combined_strings = []
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            filepath = os.path.join(folder_path,filename)
            try:
                # 打开并读取 json
                with open(filepath,'r',encoding="utf-8-sig") as file:
                    data = json.load(file)
                    if "strings" in data:
                        combined_strings.append(data["strings"])
            except Exception as e:
                print(f"handle file failed {filename} : {e}")
    print(combined_strings)
    return combined_strings

def save_combined_strings(output_file , strings):
    output_data = {"strings": strings}
    try:
        with open(output_file , 'w' , encoding='utf-8') as file:
            json.dump(output_data,file,ensure_ascii=False , indent=4)
        print(f"successfully combined")
    except Exception as e:
        print(f"save error : {e}")
        

combined_strings = scan_json_files("E:\steam\steamapps\common\Risk of Rain 2\Risk of Rain 2_Data\StreamingAssets\Language\en")
output_file = "combined_string.json"
if combined_strings:
    # 保存合并后的结果
    save_combined_strings(output_file, combined_strings)