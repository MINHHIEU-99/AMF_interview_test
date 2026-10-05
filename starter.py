"""
Khung code cho bài test "Gộp BOM từ nhiều bản vẽ".
Xem đầy đủ đề bài trong README_candidate.md.

Việc của bạn: hoàn thành hàm merge_boms() bên dưới.
Chạy: python starter.py
"""

import json
import glob


def load_all_drawings():
    """Đọc toàn bộ file drawing_*.json trong thư mục hiện tại."""
    all_parts = []
    for filepath in sorted(glob.glob("drawing_*.json")):
        with open(filepath, "r", encoding="utf-8") as f:
            parts = json.load(f)
            for part in parts:
                part["source_file"] = filepath
            all_parts.extend(parts)
    return all_parts


def merge_boms(all_parts):
    """
    TODO: Hoàn thành hàm này.

    Input:
        all_parts: list các dict, mỗi dict là 1 part từ 1 bản vẽ, dạng:
            {"part_code": str, "part_name": str, "material": str,
             "qty": int, "source_file": str}

    Output: trả về tuple (merged_bom, needs_review)

        merged_bom: list các dict, mỗi dict là 1 chi tiết ĐÃ GỘP xong, ví dụ:
            {"part_code": "BR-102", "part_name": "Bracket mounting plate",
             "material": "SS400", "total_qty": 6,
             "source_files": ["drawing_1.json", "drawing_2.json"]}

        needs_review: list các dict mô tả cặp part bạn KHÔNG CHẮC là trùng
        hay khác nhau, để con người xem lại thay vì tự đoán, ví dụ:
            {"part_a": {...}, "part_b": {...},
             "reason": "Mã code giống nhau nhưng tên chi tiết khác nhau"}
    """
    merged_bom = []
    needs_review = []

    # ---------------- Code của bạn từ đây ----------------



    # ------------------------------------------------------

    return merged_bom, needs_review


if __name__ == "__main__":
    parts = load_all_drawings()
    print(f"Đã đọc {len(parts)} part từ {len(glob.glob('drawing_*.json'))} bản vẽ.\n")

    merged_bom, needs_review = merge_boms(parts)

    print("=" * 60)
    print("BOM SAU KHI GỘP")
    print("=" * 60)
    for item in merged_bom:
        print(item)

    print("\n" + "=" * 60)
    print("CẦN NGƯỜI DUYỆT (needs_review)")
    print("=" * 60)
    if not needs_review:
        print("(không có case nào được flag)")
    for item in needs_review:
        print(item)
