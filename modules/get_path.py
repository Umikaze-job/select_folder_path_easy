from datetime import datetime
import json
import os

class SelectFolderPathEasy6321:
    day_format = None
    def __init__(self):
        # 現在のスクリプトが存在するディレクトリのパス
        current_directory = os.path.dirname(os.path.realpath(__file__))

        # ひとつ上のディレクトリのパスを取得
        parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
        with open(os.path.join(parent_directory, 'setting.json'),"r") as f:
            json_dict = json.load(f)
            self.day_format = json_dict["day_format"]

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "folder_name": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "My_File"
                }),
                "file_name": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "image"
                }),
                "time_format":("STRING",{
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": self.day_format
                })
            }
        }
    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_my_path"
    CATEGORY = "umikaze"
    
    def get_my_path(self,folder_name,file_name,time_format):
        # 今日の日付を取得
        today = datetime.today()

        # 日付を指定した形式の文字列に変換
        formatted_date = today.strftime(time_format)
        return (f"{formatted_date}/{folder_name}/{file_name}",)

NODE_CLASS_MAPPINGS = {
    "SelectFolderPathEasy": SelectFolderPathEasy6321
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "SelectFolderPathEasy": "Select Folder Path Easy"
}