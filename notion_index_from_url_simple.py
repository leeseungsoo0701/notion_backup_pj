#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
notion_index_from_url_simple.py  
- 특정 Notion URL 기준으로 전체 트리를 인덱싱하고 manifest.csv 저장
- "이승수" 등 필터링 없음
- 저장 포맷: created_date,title,id,url,object_type,methods
"""

import os
import sys
import csv
import requests
import datetime

NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
BASE_URL = "https://api.notion.com/v1"
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28"
}

OUTFILE = "/Users/seungsoo/Desktop/notion_backup_0907/out/manifest.csv"


def get_block_children(block_id):
    """해당 블록의 하위 children 가져오기"""
    url = f"{BASE_URL}/blocks/{block_id}/children?page_size=100"
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json().get("results", [])


def fetch_page(page_id):
    """페이지 메타데이터 조회"""
    url = f"{BASE_URL}/pages/{page_id}"
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()


def crawl(url, writer, visited):
    """재귀 크롤링"""
    if url in visited:
        return
    visited.add(url)

    page_id = url.split("-")[-1]
    try:
        page_meta = fetch_page(page_id)
    except Exception as e:
        print(f"페이지 조회 실패: {url}, {e}")
        return

    created_time = page_meta.get("created_time", datetime.datetime.now().isoformat())
    title = "Untitled"
    try:
        props = page_meta.get("properties", {})
        if "title" in props:
            rich_text = props["title"].get("title", [])
            if rich_text:
                title = rich_text[0].get("plain_text", "Untitled")
    except:
        pass

    writer.writerow([
        created_time.split("T")[0],
        title,
        page_id,
        url,
        "page",
        "페이지 생성자"
    ])
    print("저장:", title, url)

    # children 크롤링
    try:
        children = get_block_children(page_id)
        for child in children:
            child_id = child.get("id")
            child_type = child.get("type")
            child_url = f"https://www.notion.so/{child_id.replace('-', '')}"

            writer.writerow([
                created_time.split("T")[0],
                f"{child_type} block",
                child_id,
                child_url,
                child_type,
                "블록"
            ])

            # DB면 별도 처리 가능
            if child_type == "child_page":
                crawl(child_url, writer, visited)
    except Exception as e:
        print("children 조회 실패:", e)


def main():
    if len(sys.argv) < 2:
        print("사용법: python notion_index_from_url_simple.py <Notion_URL>")
        sys.exit(1)

    start_url = sys.argv[1]
    visited = set()

    os.makedirs(os.path.dirname(OUTFILE), exist_ok=True)
    with open(OUTFILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["created_date", "title", "id", "url", "object_type", "methods"])
        crawl(start_url, writer, visited)


if __name__ == "__main__":
    main()