import os
import mimetypes

# 过滤掉本项目中那些明显不是代码文件的目录
ignore_items=['.git', '.vscode', 'db', '__pycache__','imgs', 'images', 'assets', 'diary']
support_mimes=[
  'text/plain',
  'text/x-python',
  'application/x-python-code',
]
support_exts=['py']

def analysis_code_registry(code_path):
  if not os.path.exists(code_path):
    raise FileExistsError(f'{registry_path} not Exists!')
  
  analysis={}
  
  for dirpath, dirnames, filenames in os.walk(code_path):
    # 过滤
    dirnames[:]=[d for d in dirnames if d not in ignore_items]
    
    for filename in filenames:
      file_path=os.path.join(dirpath, filename)
      file_ext=os.path.splitext(file_path)[1][1:]
      file_mime=mimetypes.guess_type(file_path)[0]
      is_support_mime=file_mime in support_mimes
      is_supprt_ext=file_ext in support_exts
      
      if is_support_mime and is_supprt_ext:
        analysis[file_path]=file_path
      
  print(analysis)

if __name__ == '__main__':
  registry_path=os.path.abspath(os.path.join(__file__, '../../..'))
  analysis_code_registry(registry_path)
  # analysis_code_registry('sdsd')