CATEGORIES = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타"
]

prompts = [
    {
        "title": "행궁 카페 광고 비디오 프롬프트",
        "content": "수원 화성 행궁동 카페의 따뜻하고 감성적인 분위기를 담은 15초 릴스 홍보 영상 스크립트 작성",
        "category": "영상 생성",
        "favorite": True
    },
    {
        "title": "요리 레시피 자동 생성기",
        "content": "냉장고에 남은 재료 3가지를 입력하면 만들 수 있는 15분 초간단 자취 요리 레시피 안내",
        "category": "자동화",
        "favorite": False
    },
    {
        "title": "중고등 맞춤형 수학 튜터 페르소나",
        "content": "친절하고 차근차근 단계별 힌트를 주며 스스로 문제를 풀 수 있도록 유도하는 AI 수학 선생님",
        "category": "페르소나",
        "favorite": False
    }
]

def show_menu():
    print("\n" + "=" * 25)
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
    print("0. 종료")
    print("=" * 25)

def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    title = input("제목: ").strip()
    content = input("내용: ").strip()
    
    print("\n카테고리 선택:")
    for idx, cat in enumerate(CATEGORIES, start=1):
        print(f"{idx}) {cat}")
    
    choice = input("선택 (1~6): ").strip()
    selected_category = CATEGORIES[int(choice) - 1]
    
    prompts.append({
        "title": title,
        "content": content,
        "category": selected_category,
        "favorite": False
    })
    print("✨ 프롬프트가 추가되었습니다!")

def show_list():
    print("\n=== 프롬프트 목록 ===")
    for idx, p in enumerate(prompts, start=1):
        fav = "⭐" if p["favorite"] else ""
        print(f"{idx}. [{p['category']}] {p['title']} {fav}")

def show_by_category():
    print("\n=== 카테고리별 조회 ===")
    for idx, cat in enumerate(CATEGORIES, start=1):
        print(f"{idx}) {cat}")
    choice = input("선택: ").strip()
    selected_category = CATEGORIES[int(choice) - 1]
    
    print(f"\n[{selected_category}] 카테고리:")
    for idx, p in enumerate([p for p in prompts if p["category"] == selected_category], start=1):
        fav = "⭐" if p["favorite"] else ""
        print(f"{idx}. {p['title']} {fav}")

def search_prompt():
    keyword = input("\n검색어: ").strip()
    print("\n검색 결과:")
    for idx, p in enumerate([p for p in prompts if keyword in p["title"] or keyword in p["content"]], start=1):
        fav = "⭐" if p["favorite"] else ""
        print(f"{idx}. [{p['category']}] {p['title']} {fav}")

def view_detail():
    choice = int(input("\n번호 입력: ")) - 1
    p = prompts[choice]
    print("─" * 30)
    print(f"제목: {p['title']}\n카테고리: {p['category']}\n내용:\n{p['content']}")
    print("─" * 30)

def toggle_favorite():
    choice = int(input("\n번호 입력: ")) - 1
    prompts[choice]["favorite"] = not prompts[choice]["favorite"]
    print("즐겨찾기 상태가 변경되었습니다!")

def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")
    for idx, p in enumerate([p for p in prompts if p["favorite"]], start=1):
        print(f"{idx}. [{p['category']}] {p['title']} ⭐")

def edit_prompt():
    print("\n=== 프롬프트 수정 ===")
    choice = int(input("수정할 번호 입력: ")) - 1
    p = prompts[choice]
    
    new_title = input(f"새 제목 (현재: {p['title']}): ").strip()
    if new_title:
        p["title"] = new_title
        
    new_content = input(f"새 내용 (현재: {p['content']}): ").strip()
    if new_content:
        p["content"] = new_content
    print("✨ 수정 완료!")

def main():
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
        elif choice == "0":
            print("종료합니다!")
            break

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
    
    if confirm == 'y':
        prompts.pop(index)
        print("🗑️ 프롬프트가 삭제되었습니다.")
    else:
        print("삭제가 취소되었습니다.")
if __name__ == "__main__":
    main()    