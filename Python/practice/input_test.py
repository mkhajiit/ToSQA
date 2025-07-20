enemy_hp = 10
player_hp = 4
skill_point = 0
turn = 1

def print_status():
  global turn # 전역 변수 turn을 쓰겠다 선언
  print(f"남아있는 적의 체력은 {enemy_hp}입니다.")
  print(f"남아있는 유저의 체력은 {player_hp}입니다.")
  print(f"남아있는 필살기 포인트는 {skill_point}입니다.")
  turn += 1

while True:
  print(f"턴{turn} 시작")
  command = input("명령어를 입력해주세요(공격,방어,필살기): ")
  if command == "공격":
    skill_point += 1
    player_hp -= 1
    enemy_hp -= 2
    print_status()
    
  elif command == "방어":
    skill_point += 1
    print_status()

  elif command == "필살기":
    if skill_point >= 3:
      enemy_hp -= 6
      skill_point -= 3
      print_status()
    else:
      print("필살기 포인트가 부족합니다!")
  else:
    print("잘못된 입력입니다.")
  
  # 위에 조건을 실행하고 실행됨
  if enemy_hp <= 0:  # 적 체력이 0 이하인가?
    print("적을 물리쳤습니다!")
    break
  elif player_hp <= 0:  # 플레이어 체력이 0 이하인가?
    print("플레이어가 쓰러졌습니다...")
    break