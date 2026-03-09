#!/usr/bin/env python3
"""
测试 Scrapling+html2text 技能的简单脚本
"""

import subprocess
import tempfile
import os

def test_skill():
    """
    测试技能是否正常工作
    """
    print("🚀 开始测试 Scrapling+html2text 技能")
    
    # 创建临时文件
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md', encoding='utf-8')
    temp_file.close()
    
    # 测试 URL
    test_url = "https://example.com"
    
    try:
        # 测试基础功能
        print(f"📡 测试访问: {test_url}")
        result = subprocess.run(['python3', 'script/scrapling_fetch.py', test_url, temp_file.name, '--no-stealth'], 
                              capture_output=True, text=True, check=False, cwd=os.path.dirname(os.path.abspath(__file__)))
        
        print(f"📊 执行结果: {'成功' if result.returncode == 0 else '失败'}")
        
        if result.returncode == 0:
            # 检查输出文件大小
            file_size = os.path.getsize(temp_file.name)
            print(f"📄 输出文件大小: {file_size} 字节")
            
            # 读取输出文件内容
            with open(temp_file.name, 'r', encoding='utf-8') as f:
                content = f.read()
                
            print(f"📖 内容预览: {content[:200]}...")
            
            # 检查是否包含预期内容
            if "Example Domain" in content:
                print("✅ 测试成功：内容包含预期标题")
            else:
                print("⚠️  测试警告：内容可能不完整")
                
        else:
            print(f"❌ 测试失败，错误信息:")
            if result.stderr:
                print(f"   错误: {result.stderr}")
            if result.stdout:
                print(f"   输出: {result.stdout}")
                
    except Exception as e:
        print(f"❌ 测试过程出错: {e}")
        
    finally:
        # 清理临时文件
        try:
            os.remove(temp_file.name)
        except Exception:
            pass
            
        print("\n🎉 测试完成")

if __name__ == "__main__":
    test_skill()