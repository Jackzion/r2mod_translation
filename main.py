import os
import mod_translate

# 递归检索 en 文件夹 （排除 cn）
def process_en_files_and_folders(root_dir):
    for dirpath,dirnames,filenames in os.walk(root_dir):
        en_items = [item for item in dirnames + filenames if item.startswith("en")]
        cn_items = [item for item in dirnames + filenames if item.startswith("zh")]
        # 检测到 cn_f , compare cn_f and en_f
        if cn_items:
            compare_cn_f(en_items,cn_items,dirpath)
        # 只有 en_f , replace en_f
        else :
            replace_en_f(en_items,dirpath)


def compare_cn_f(en_items,cn_items,dirpath):
        for i in range(len(en_items)):
            cn_item = cn_items[i]
            en_item = en_items[i]
            en_item_path = os.path.join(dirpath,en_item)
            cn_item_path = os.path.join(dirpath,cn_item)
            # is en_file
            if os.path.isfile(en_item_path) and en_item_path.endswith(('.txt','.json','.language')):
                mod_translate.compare_and_translate(en_item_path,cn_item_path)
            # is en_folder
            if os.path.isdir(en_item_path):
                en_sub_items = os.listdir(en_item_path)
                cn_sub_items = os.listdir(cn_item_path)
                for en_sub_item in en_sub_items:
                    en_sub_item_path = os.path.join(en_item_path,en_sub_item)
                    temp_string = en_sub_item.replace('_en','_zh')
                    cn_sub_item_path = os.path.join(cn_item_path,temp_string)
                    if temp_string in cn_sub_items:
                        # compare and save in cn_file
                        mod_translate.compare_and_translate(en_sub_item_path,cn_sub_item_path)
                    else:
                        # not find cn_file
                        # translate and replace in en_file
                        mod_translate.extract_and_translate(en_sub_item_path)
                        
def replace_en_f(en_items,dirpath):
    for en_item in en_items:
        en_item_path = os.path.join(dirpath,en_item)
        if os.path.isdir(en_item_path):
            print(f"Contents of folder: {en_item_path}")
            for sub_item in os.listdir(en_item_path):
                if(sub_item.endswith(('.txt','.json','.language'))):
                    full_path = os.path.join(en_item_path, sub_item)
                    print(f" translating File : {full_path} 。。。。")
                    mod_translate.extract_and_translate(full_path)
                    print(" finish translating 。。")
        else:
            if(en_item.endswith(('.txt','.json','.language'))):
                print(f"translating File : {en_item_path} 。。。。")
                mod_translate.extract_and_translate(en_item_path)
                print("finish translating 。。")

root_path = r'C:\Users\Ziio\AppData\Roaming\r2modmanPlus-local\RiskOfRain2\cache\TeamMoonstorm-Starstorm2\0.6.16\plugins'
process_en_files_and_folders(root_path)