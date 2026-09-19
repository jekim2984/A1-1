import os
import json

DATA_FILE = "prompts.json"
MARKDOWN_EXPORT_FILE = "prompts_by_category.md"

CATEGORIES = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타"
]

DEFAULT_PROMPTS = [
    {
        "title": "행궁 카페 광고 비디오 프롬프트",
        "content": "수원 화성 행궁동 카페의 따뜻하고 감성적인 분위기를 담은 15초 릴스 홍보 영상 스크립트 작성",
        "category": "영상 생성",
        "favorite": True,
        "views": 0
    },
    {
        "title": "요리 레시피 자동 생성기",
        "content": "냉장고에 남은 재료 3가지를 입력하면 만들 수 있는 15분 초간단 자취 요리 레시피 안내",
        "category": "자동화",
        "favorite": False,
        "views": 0
    },
    {
        "title": "중고등 맞춤형 수학 튜터 페르소나",
        "content": "친절하고 차근차근 단계별 힌트를 주며 스스로 문제를 풀 수 있도록 유도하는 AI 수학 선생님",
        "category": "페르소나",
        "favorite": False,
        "views": 0
    }
]

# 프롬프트 목록 전역 변수
prompts = []


def load_prompts():
    """보너스 1: JSON 파일에서 프롬프트 데이터 로드 (없으면 기본 데이터 생성)"""
    global prompts
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                # 데이터 유효성 및 views 필드 기본값 보장
                for p in loaded:
                    if "views" not in p:
                        p["views"] = 0
                prompts = loaded
                return
        except (json.JSONDecodeError, OSError) as e:
            print(f"⚠️ 데이터 파일 읽기 오류 ({e}). 기본 데이터를 사용합니다.")

    # 파일이 없거나 오류 발생 시 기본 데이터 사용
    prompts = [p.copy() for p in DEFAULT_PROMPTS]
    save_prompts()


def save_prompts():
    """보너스 1: 프롬프트 데이터를 JSON 파일로 저장"""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(prompts, f, ensure_ascii=False, indent=4)
    except OSError as e:
        print(f"⚠️ 데이터 저장 실패: {e}")


def show_menu():
    """메뉴 출력"""
    print("\n" + "=" * 30)
    print("=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 프롬프트 수정")
    print("9. 프롬프트 삭제")
    print("10. 인기 프롬프트 Top 목록 (보너스)")
    print("11. Markdown으로 내보내기 (보너스)")
    print("0. 종료")
    print("=" * 30)


def add_prompt():
    """1. 프롬프트 추가 (빈 값 검증 및 카테고리 예외 처리)"""
    print("\n=== 프롬프트 추가 ===")

    while True:
        title = input("제목: ").strip()
        if title:
            break
        print("❌ 제목은 비워둘 수 없습니다. 다시 입력해주세요.")

    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("❌ 내용은 비워둘 수 없습니다. 다시 입력해주세요.")

    print("\n카테고리 선택:")
    for idx, cat in enumerate(CATEGORIES, start=1):
        print(f"{idx}) {cat}")

    while True:
        choice = input(f"선택 (1~{len(CATEGORIES)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            selected_category = CATEGORIES[int(choice) - 1]
            break
        print(f"❌ 1부터 {len(CATEGORIES)} 사이의 번호를 입력해주세요.")

    prompts.append({
        "title": title,
        "content": content,
        "category": selected_category,
        "favorite": False,
        "views": 0
    })
    save_prompts()
    print("✨ 프롬프트가 추가되었습니다!")


def show_list():
    """2. 프롬프트 목록 출력"""
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for idx, p in enumerate(prompts, start=1):
        fav = "⭐" if p.get("favorite", False) else ""
        print(f"{idx}. [{p['category']}] {p['title']} {fav}")

    print(f"\n총 {len(prompts)}개의 프롬프트")


def show_by_category():
    """3. 카테고리별 프롬프트 조회"""
    print("\n=== 카테고리별 조회 ===")
    for idx, cat in enumerate(CATEGORIES, start=1):
        print(f"{idx}) {cat}")

    choice = input(f"선택 (1~{len(CATEGORIES)}): ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(CATEGORIES)):
        print("❌ 올바른 카테고리 번호를 입력해주세요.")
        return

    selected_category = CATEGORIES[int(choice) - 1]
    filtered = [p for p in prompts if p["category"] == selected_category]

    print(f"\n[{selected_category}] 카테고리 프롬프트:")
    if not filtered:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
        return

    for idx, p in enumerate(filtered, start=1):
        fav = "⭐" if p.get("favorite", False) else ""
        print(f"{idx}. {p['title']} {fav}")

    print(f"\n총 {len(filtered)}개의 프롬프트")


def search_prompt():
    """4. 프롬프트 검색 (제목 또는 내용)"""
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어: ").strip()
    if not keyword:
        print("❌ 검색어를 입력해주세요.")
        return

    results = [p for p in prompts if keyword in p["title"] or keyword in p["content"]]

    print("\n검색 결과:")
    if not results:
        print(f"'{keyword}'에 대한 검색 결과가 없습니다.")
        return

    for idx, p in enumerate(results, start=1):
        fav = "⭐" if p.get("favorite", False) else ""
        print(f"{idx}. [{p['category']}] {p['title']} {fav}")

    print(f"\n총 {len(results)}개의 프롬프트를 찾았습니다.")


def view_detail():
    """5. 프롬프트 상세 보기 (조회수 기록 및 즐겨찾기 표시)"""
    print("\n=== 프롬프트 상세 보기 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    choice = input("번호 입력: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(prompts)):
        print("❌ 유효하지 않은 번호입니다.")
        return

    p = prompts[int(choice) - 1]

    # 보너스 2: 상세 보기 시 사용 횟수(조회수) 증가
    p["views"] = p.get("views", 0) + 1
    save_prompts()

    fav_str = "⭐" if p.get("favorite", False) else "해당 없음"
    print("─" * 32)
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {fav_str}")
    print(f"조회수: {p['views']}회")
    print("─" * 32)
    print("내용:")
    print(p["content"])
    print("─" * 32)


def toggle_favorite():
    """6. 즐겨찾기 관리 (추가/해제 토글)"""
    print("\n=== 즐겨찾기 관리 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    choice = input("프롬프트 번호 입력: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(prompts)):
        print("❌ 유효하지 않은 번호입니다.")
        return

    p = prompts[int(choice) - 1]
    p["favorite"] = not p.get("favorite", False)
    save_prompts()

    action = "추가" if p["favorite"] else "해제"
    print(f"✨ '{p['title']}' 프롬프트를 즐겨찾기에 {action}했습니다!")


def show_favorites():
    """7. 즐겨찾기 목록 조회"""
    print("\n=== 즐겨찾기 목록 ===")
    favs = [p for p in prompts if p.get("favorite", False)]
    if not favs:
        print("즐겨찾기로 등록된 프롬프트가 없습니다.")
        return

    for idx, p in enumerate(favs, start=1):
        print(f"{idx}. [{p['category']}] {p['title']} ⭐")

    print(f"\n총 {len(favs)}개의 즐겨찾기")


def edit_prompt():
    """8. 프롬프트 수정"""
    print("\n=== 프롬프트 수정 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    choice = input("수정할 번호 입력: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(prompts)):
        print("❌ 유효하지 않은 번호입니다.")
        return

    p = prompts[int(choice) - 1]

    new_title = input(f"새 제목 (엔터 시 유지: '{p['title']}'): ").strip()
    if new_title:
        p["title"] = new_title

    new_content = input(f"새 내용 (엔터 시 유지: '{p['content']}'): ").strip()
    if new_content:
        p["content"] = new_content

    save_prompts()
    print("✨ 수정이 완료되었습니다!")


def delete_prompt():
    """9. 프롬프트 삭제"""
    print("\n=== 프롬프트 삭제 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    choice = input("삭제할 프롬프트 번호 입력: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(prompts)):
        print("❌ 유효하지 않은 번호입니다.")
        return

    index = int(choice) - 1
    p = prompts[index]
    confirm = input(f"정말 '{p['title']}' 프롬프트를 삭제하시겠습니까? (y/n): ").strip().lower()

    if confirm == "y":
        deleted = prompts.pop(index)
        save_prompts()
        print(f"🗑️ '{deleted['title']}' 프롬프트가 삭제되었습니다.")
    else:
        print("삭제가 취소되었습니다.")


def show_top_prompts():
    """10. 보너스 2: 조회수 기준 Top 인기 프롬프트 목록"""
    print("\n=== 인기 프롬프트 Top 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # 조회수 내림차순 정렬
    sorted_prompts = sorted(prompts, key=lambda x: x.get("views", 0), reverse=True)

    for rank, p in enumerate(sorted_prompts, start=1):
        fav = "⭐" if p.get("favorite", False) else ""
        print(f"{rank}. [{p['category']}] {p['title']} {fav} (조회수: {p.get('views', 0)}회)")

    print(f"\n총 {len(sorted_prompts)}개의 프롬프트 (조회수 순)")


def export_to_markdown():
    """11. 보너스 1: 카테고리별 Markdown 파일 내보내기"""
    print("\n=== Markdown 파일로 내보내기 ===")
    if not prompts:
        print("내보낼 프롬프트가 없습니다.")
        return

    lines = []
    lines.append("# 📑 나만의 프롬프트 모음집 (카테고리별)\n")
    lines.append(f"> 총 {len(prompts)}개의 프롬프트가 등록되어 있습니다.\n")

    lines.append("## 📌 목차")
    for cat in CATEGORIES:
        count = sum(1 for p in prompts if p["category"] == cat)
        lines.append(f"- [{cat}](#{cat.replace(' ', '-')}) ({count}개)")
    lines.append("\n---\n")

    for cat in CATEGORIES:
        cat_prompts = [p for p in prompts if p["category"] == cat]
        lines.append(f"## {cat}\n")
        if not cat_prompts:
            lines.append("*등록된 프롬프트가 없습니다.*\n")
            continue

        for idx, p in enumerate(cat_prompts, start=1):
            fav_str = "⭐ 즐겨찾기" if p.get("favorite", False) else "일반"
            views = p.get("views", 0)
            lines.append(f"### {idx}. {p['title']}")
            lines.append(f"- **분류 상태**: {fav_str} | **조회수**: {views}회")
            lines.append("```text")
            lines.append(p["content"])
            lines.append("```\n")

    try:
        with open(MARKDOWN_EXPORT_FILE, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"📄 '{MARKDOWN_EXPORT_FILE}' 파일로 성공적으로 내보냈습니다!")
    except OSError as e:
        print(f"❌ Markdown 파일 내보내기 실패: {e}")


def main():
    load_prompts()

    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            view_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "8":
            edit_prompt()
        elif choice == "9":
            delete_prompt()
        elif choice == "10":
            show_top_prompts()
        elif choice == "11":
            export_to_markdown()
        elif choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("❌ 올바른 메뉴 번호를 입력해주세요. (0 ~ 11)")


if __name__ == "__main__":
    main()