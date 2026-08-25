# 이번 미션은 깃허브 연결 테스테야
# 2984로 로그인 작업해도 가능하내
# 새로운 파일을 만들자
# 점검
# 확인
# 오늘밤 퇴실전 마지막 확인
# 다시 git 연습하기 
# 프로그램 시작 시 등록될 기본 프롬프트 데이터 (최소 3개 이상)
prompts = [
    {
        "title": "행궁 off the record 카페 숏폼 광고",
        "content": "수원 행궁동의 감성적인 'off the record' 카페를 위한 30초 숏폼 광고 영상 스크립트를 작성해줘. 차분한 로파이(Lo-fi) 음악과 함께 따뜻한 커피 한 잔의 여유를 시네마틱한 분위기로 연출하고, 마지막 3초에는 브랜드 로고와 함께 감성적인 슬로건을 노출해줘.",
        "category": "영상 생성",
        "favorite": True
    },
    {
        "title": "스마트 냉파 요리 레시피 및 노션 자동화",
        "content": "사용자가 입력한 냉장고 남은 재료와 선호하는 요리 스타일을 바탕으로, 초보자도 15분 내로 쉽게 따라 할 수 있는 요리 레시피를 단계별로 작성해줘. 그리고 이 결과물이 노션(Notion) 데이터베이스의 '제목', '요약', '레시피 본문' 속성에 바로 자동 저장될 수 있도록 마크다운 형식으로 구조화해줘.",
        "category": "자동화",
        "favorite": False
    },
    {
        "title": "개념 쏙쏙 친절한 AI 수학 튜터",
        "content": "당신은 학생들의 눈높이에 맞춰 친절하게 수학 개념을 설명해 주는 전문 수학 튜터입니다. 공식을 무조건 외우게 하지 말고, 피자 나누기나 쇼핑 할인 등 일상생활의 친근한 예시를 들어 설명해주세요. 학생이 한 번에 이해할 수 있도록 단계별로 유도 질문을 던지며 대화를 이끌어가주세요.",
        "category": "페르소나",
        "favorite": False
    }
]

def show_menu():
    """메인 메뉴를 출력하고 사용자의 선택을 받는 함수"""
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")
    choice = input("선택: ")
    return choice

def add_prompt():
    """새로운 프롬프트를 추가하는 함수"""
    print("\n=== 프롬프트 추가 ===")
    title = input("제목: ").strip()
    if not title:
        print("제목은 비워둘 수 없습니다. 다시 시도해주세요.")
        return

    content = input("내용: ").strip()
    if not content:
        print("내용은 비워둘 수 없습니다. 다시 시도해주세요.")
        return

    print("\n카테고리 선택:")
    print("1) 텍스트 생성  2) 이미지 생성  3) 영상 생성  4) 페르소나  5) 자동화  6) 기타")
    cat_choice = input("선택 번호 또는 직접 입력: ").strip()
    
    categories = {"1": "텍스트 생성", "2": "이미지 생성", "3": "영상 생성", "4": "페르소나", "5": "자동화", "6": "기타"}
    category = categories.get(cat_choice, cat_choice if cat_choice else "기타")

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }
    prompts.append(new_prompt)
    print("\n프롬프트가 추가되었습니다!")

def show_list():
    """저장된 모든 프롬프트 목록을 출력하는 함수"""
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, p in enumerate(prompts, 1):
        fav = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{fav}")
    print(f"\n총 {len(prompts)}개의 프롬프트")

def show_category():
    """카테고리별로 프롬프트를 조회하는 함수"""
    print("\n=== 카테고리별 조회 ===")
    print("1) 텍스트 생성  2) 이미지 생성  3) 영상 생성  4) 페르소나  5) 자동화  6) 기타")
    cat_choice = input("카테고리 선택 번호: ").strip()
    
    categories = {"1": "텍스트 생성", "2": "이미지 생성", "3": "영상 생성", "4": "페르소나", "5": "자동화", "6": "기타"}
    selected_cat = categories.get(cat_choice)
    
    if not selected_cat:
        print("잘못된 선택입니다.")
        return

    print(f"\n[{selected_cat}] 카테고리 프롬프트:")
    filtered = [p for p in prompts if p["category"] == selected_cat]
    
    if not filtered:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return

    for i, p in enumerate(prompts, 1):
        if p["category"] == selected_cat:
            fav = " ⭐" if p["favorite"] else ""
            print(f"{i}. {p['title']}{fav}")
    print(f"\n총 {len(filtered)}개의 프롬프트")

def search_prompt():
    """키워드로 프롬프트를 검색하는 함수"""
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어: ").strip().lower()
    if not keyword:
        print("검색어를 입력해주세요.")
        return

    results = []
    for i, p in enumerate(prompts):
        if keyword in p["title"].lower() or keyword in p["content"].lower():
            results.append((i + 1, p))

    print("\n검색 결과:")
    if not results:
        print("검색 결과가 없습니다.")
        return

    for num, p in results:
        fav = " ⭐" if p["favorite"] else ""
        print(f"{num}. [{p['category']}] {p['title']}{fav}")
    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")

def show_detail():
    """특정 프롬프트의 상세 내용을 출력하는 함수"""
    print("\n=== 프롬프트 상세 보기 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    try:
        num = int(input("번호 입력: "))
        if 1 <= num <= len(prompts):
            p = prompts[num - 1]
            fav = "⭐" if p["favorite"] else "없음"
            print("\n" + "─" * 28)
            print(f"제목: {p['title']}")
            print(f"카테고리: {p['category']}")
            print(f"즐겨찾기: {fav}")
            print("─" * 28)
            print("내용:")
            print(p['content'])
            print("─" * 28)
        else:
            print("존재하지 않는 번호입니다.")
    except ValueError:
        print("올바른 숫자를 입력해주세요.")

def manage_favorite():
    """즐겨찾기 추가 및 해제 함수"""
    print("\n=== 즐겨찾기 관리 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    try:
        num = int(input("프롬프트 번호 입력: "))
        if 1 <= num <= len(prompts):
            p = prompts[num - 1]
            p["favorite"] = not p["favorite"]
            status = "추가" if p["favorite"] else "해제"
            print(f"'{p['title']}' 프롬프트를 즐겨찾기에 {status}했습니다!")
        else:
            print("존재하지 않는 번호입니다.")
    except ValueError:
        print("올바른 숫자를 입력해주세요.")

def show_favorites():
    """즐겨찾기된 프롬프트만 모아서 보는 함수"""
    print("\n=== 즐겨찾기 목록 ===")
    fav_list = [p for p in prompts if p["favorite"]]
    
    if not fav_list:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return

    for i, p in enumerate(prompts, 1):
        if p["favorite"]:
            print(f"{i}. [{p['category']}] {p['title']} ⭐")
    print(f"\n총 {len(fav_list)}개의 즐겨찾기")

def main():
    """프로그램 실행 메인 루프"""
    while True:
        choice = show_menu()
        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            manage_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "0":
            print("\n프로그램을 종료합니다. 이용해주셔서 감사합니다!")
            break
        else:
            print("\n잘못된 입력입니다. 올바른 메뉴 번호를 선택해주세요.")

if __name__ == "__main__":
    main()