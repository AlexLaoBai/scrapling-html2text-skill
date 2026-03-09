#!/usr/bin/env python3
"""
Scrapling结合html2text的网页内容提取脚本 - 优化升级版本
使用最新的Scrapling特性，提高反爬能力和内容提取质量
"""

import argparse
import sys
import os
from scrapling.fetchers import StealthyFetcher
from scrapling.fetchers import Fetcher  # 备用方案
import html2text
import time
from typing import Optional

def configure_html2text():
    """
    配置html2text，优化输出质量
    """
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # 不自动折行
    h.ignore_emphasis = False
    h.images_to_alt = True  # 将图片替换为alt文本
    h.images_with_size = True  # 保留图片尺寸
    h.skip_internal_links = False
    h.inline_links = True  # 使用内联链接格式
    return h

def extract_content_with_scrapling(url, max_chars=30000, use_stealth=True, max_retries=3):
    """
    使用Scrapling抓取网页并提取内容
    支持使用StealthyFetcher提高反爬能力，添加重试机制
    """
    for attempt in range(max_retries):
        try:
            if use_stealth:
                print(f"🔍 正在尝试抓取页面 (第 {attempt + 1} 次) - 隐身模式")
                page = StealthyFetcher.fetch(url, headless=True, solve_cloudflare=True, network_idle=True)
            else:
                print(f"🔍 正在尝试抓取页面 (第 {attempt + 1} 次) - 基础模式")
                page = Fetcher.get(url)
                
            print(f"✅ 成功抓取页面: {page.url}")
            
            # 智能提取正文内容
            content = extract_main_content(page, max_chars)
            
            if content:
                return content
            else:
                print("⚠️ 未找到正文内容，尝试使用备用提取方法")
                # 使用备用文本提取方法
                return page.get_all_text()[:max_chars] + "..."
                
        except Exception as e:
            print(f"❌ 抓取失败 (第 {attempt + 1} 次): {e}")
            if attempt < max_retries - 1:
                print("⏳ 正在重试...")
                time.sleep(2)
            else:
                print("❌ 多次尝试失败，无法抓取页面")
                return None

def extract_main_content(page, max_chars=30000):
    """
    智能提取网页正文内容
    使用Scrapling的自适应选择器和智能算法
    """
    # 按优先级尝试获取正文
    content_element = None
    selectors = [
        'article', 
        'main', 
        '.post-content', 
        '[class*="body"]',
        '.content',
        '#js_content',  # 微信公众号文章选择器
        '.article-content',
        '.entry-content',
        '.post-body',
        '[class*="article"]',
        '[class*="content"]'
    ]
    
    for selector in selectors:
        elements = page.css(selector)
        if elements:
            print(f"✅ 使用选择器 {selector} 找到正文")
            content_element = elements[0]
            break
    
    if content_element:
        # 使用html2text转换HTML为Markdown
        h = configure_html2text()
        markdown_content = h.handle(str(content_element))
        
        # 清理内容
        markdown_content = clean_content(markdown_content)
        
        # 截断内容
        if len(markdown_content) > max_chars:
            markdown_content = markdown_content[:max_chars] + "..."
        
        return markdown_content
    
    return None

def clean_content(content):
    """
    清理提取的内容，去除无用信息
    """
    # 去除多余的空行
    lines = content.split('\n')
    cleaned_lines = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            cleaned_lines.append(stripped_line)
    
    return '\n'.join(cleaned_lines)

def save_content(content, output_file):
    """
    保存内容到文件
    """
    try:
        os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ 内容已保存到: {output_file}")
        return True
    except Exception as e:
        print(f"❌ 保存失败: {e}")
        return False

def main():
    """
    主函数 - 优化版本
    """
    parser = argparse.ArgumentParser(description="使用Scrapling结合html2text提取网页内容 - 优化升级版本")
    parser.add_argument("url", help="要抓取的网页URL")
    parser.add_argument("output", help="保存路径")
    parser.add_argument("-c", "--chars", type=int, default=30000, 
                      help="最大字符数，默认30000")
    parser.add_argument("-n", "--no-stealth", action="store_true", 
                      help="不使用隐身模式（使用基础抓取方法）")
    parser.add_argument("-r", "--retries", type=int, default=3, 
                      help="最大重试次数，默认3次")
    parser.add_argument("-t", "--timeout", type=int, default=60, 
                      help="超时时间（秒），默认60秒")
    
    args = parser.parse_args()
    
    print("🔍 开始提取网页内容...")
    print(f"🔧 配置: 最大字符数={args.chars}, 重试次数={args.retries}, 隐身模式={not args.no_stealth}")
    
    content = extract_content_with_scrapling(
        args.url, 
        max_chars=args.chars, 
        use_stealth=not args.no_stealth, 
        max_retries=args.retries
    )
    
    if content:
        save_content(content, args.output)
    else:
        print("❌ 提取失败")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())