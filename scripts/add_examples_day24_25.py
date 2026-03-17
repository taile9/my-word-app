import sys

day24_examples = {
    "appoint": ("The board appointed him as the new Chief Executive Officer.", "이사회는 그를 새로운 최고 경영자로 임명했습니다."),
    "appraisal": ("The company requires an annual performance appraisal for all staff.", "회사는 전 직원에 대해 연례 성과 평가를 요구합니다."),
    "promote": ("She was promoted to senior manager after three years of service.", "그녀는 3년 근무 후 수석 매니저로 승진했습니다."),
    "skilled": ("We need highly skilled workers for this complex project.", "이 복잡한 프로젝트를 위해서는 고도로 숙련된 근로자가 필요합니다."),
    "radically": ("The new software has radically changed how we communicate.", "새로운 소프트웨어는 우리의 소통 방식을 근본적으로 바꿨습니다."),
    "exceptional": ("The team showed exceptional dedication during the crisis.", "팀은 위기 상황에서 예외적으로 뛰어난 헌신을 보였습니다."),
    "appreciation": ("He sent a gift basket to show his appreciation for their help.", "그는 그들의 도움에 대한 감사를 표하기 위해 선물 바구니를 보냈습니다."),
    "evaluate": ("The committee will evaluate the results of the recent survey.", "위원회는 최근 설문조사의 결과를 평가할 것입니다."),
    "suggest": ("I suggest we review the budget before making a final decision.", "나는 최종 결정을 내리기 전에 예산을 검토할 것을 제안합니다."),
    "preference": ("When selecting a new laptop, speed is my primary preference.", "새 노트북을 선택할 때 속도가 내 최우선적인 선호 요소입니다."),
    "management": ("The success of the business relies heavily on good management.", "사업의 성공은 훌륭한 경영/관리에 크게 의존합니다."),
    "predict": ("Analysts predict a 5% increase in sales this quarter.", "분석가들은 이번 분기에 판매가 5% 증가할 것으로 예측합니다."),
    "transfer": ("He will transfer to the London completely next month.", "그는 다음 달에 런던 지사로 완전히 전근(이동)할 것입니다."),
    "award": ("The actor won the best performance award at the film festival.", "그 배우는 영화제에서 최우수 연기상을 받았습니다."),
    "mandatory": ("Attendance at the safety orientation is mandatory for new employees.", "새 직원들에게 안전 오리엔테이션 참석은 의무적입니다."),
    "competent": ("We are looking for a highly competent assistant to manage the schedule.", "우리는 일정을 관리할 고도로 유능한 조수를 찾고 있습니다."),
    "performance": ("The manager praised the team for their outstanding performance.", "관리자는 팀의 뛰어난 성과를 칭찬했습니다."),
    "reward": ("The company offers a financial reward for innovative ideas.", "회사는 혁신적인 아이디어에 대해 금전적 보상을 제공합니다."),
    "search": ("They continue to search for new ways to reduce manufacturing costs.", "그들은 제조 비용을 줄이기 위한 새로운 방법을 계속해서 찾고 있습니다."),
    "inexperienced": ("The mistake was made by an inexperienced new employee.", "그 실수는 경험 없는 신입 직원에 의해 발생했습니다."),
    "early": ("I try to get to the office early to avoid traffic.", "나는 교통 체증을 피하기 위해 사무실에 일찍 도착하려고 노력합니다."),
    "designate": ("Please smoke only in the designated areas.", "지정된 구역에서만 흡연해 주십시오."),
    "executive": ("The executive board will meet tomorrow to discuss the merger.", "임원진 이사회는 내일 합병에 대해 논의하기 위해 모일 것입니다."),
    "dedication": ("Her dedication to the project was widely recognized by her peers.", "프로젝트에 대한 그녀의 헌신은 동료들에게 널리 인정받았습니다."),
    "unanimously": ("The proposal was approved unanimously by the committee.", "그 제안은 위원회에 의해 만장일치로 승인되었습니다."),
    "progress": ("The construction team is making steady progress on the new bridge.", "건설 팀은 새 다리 작업에서 꾸준한 진전을 보이고 있습니다."),
    "congratulate": ("I want to congratulate you on your recent promotion.", "당신의 최근 승진을 축하하고 싶습니다."),
    "dismiss": ("The employer cannot dismiss a worker without a valid reason.", "고용주는 타당한 이유 없이 근로자를 해고할 수 없습니다."),
    "independence": ("The region finally gained independence after years of struggle.", "그 지역은 수년간의 투쟁 끝에 마침내 독립을 얻었습니다."),
    "participation": ("Active participation in the discussion is highly encouraged.", "토론에 적극적인 참여가 강력히 권장됩니다."),
    "praise": ("The teacher had nothing but praise for the student's hard work.", "선생님은 그 학생의 노력에 대해 칭찬만 했습니다."),
    "accomplishment": ("Graduating with honors is a significant accomplishment.", "우등으로 졸업하는 것은 대단한 성과입니다."),
    "deliberation": ("After much deliberation, they decided to sell the old house.", "많은 숙고 끝에, 그들은 오래된 집을 팔기로 결정했습니다."),
    "leadership": ("The team thrived under the leadership of the new coach.", "팀은 새 코치의 리더십 아래 번창했습니다."),
    "retire": ("My grandfather plans to retire from his teaching job next year.", "할아버지는 내년에 교직에서 은퇴할 계획입니다."),
    "nomination": ("He received a nomination for the employee of the year award.", "그는 올해의 직원상 후보 지명을 받았습니다."),
    "reorganize": ("The new manager wants to completely reorganize the sales department.", "새 관리자는 판매 부서를 완전히 재편성하기를 원합니다."),
    "serve": ("The hotel staff is always ready to serve the guests with a smile.", "호텔 직원은 항상 미소로 손님에게 서비스(제공)할 준비가 되어 있습니다."),
    "encouragement": ("Children need constant encouragement from their parents and teachers.", "아이들은 부모와 교사들로부터 끊임없는 격려가 필요합니다."),
    "resignation": ("He submitted his letter of resignation to human resources yesterday.", "그는 어제 인사부에 사직서를 제출했습니다."),
    "strictly": ("The dress code at the office is strictly enforced.", "사무실의 복장 규정은 엄격히 시행됩니다."),
}

day25_examples = {
    "congestion": ("The new subway line has significantly reduced traffic congestion.", "새 지하철 노선은 교통 혼잡을 눈에 띄게 줄였습니다."),
    "alleviate": ("We need to find ways to alleviate the workload of our nurses.", "우리는 간호사들의 업무량을 완화할 방법을 찾아야 합니다."),
    "divert": ("Traffic had to be diverted due to a massive accident on the highway.", "고속도로 대형 사고 때문에 교통이 우회되어야 했습니다."),
    "detour": ("We had to take a long detour because the main bridge was closed.", "주요 다리가 폐쇄되어서 우리는 길고 먼 우회로로 가야 했습니다."),
    "fuel": ("The airline spent millions more on jet fuel this year.", "그 항공사는 올해 제트 연료에 수백만 달러를 더 소비했습니다."),
    "malfunction": ("The elevator stopped working due to a mechanical malfunction.", "엘리베이터가 기계적 오작동 때문에 작동을 멈췄습니다."),
    "permit": ("You need a special permit to park in this exclusive residential area.", "이 전용 주거 구역에 주차하려면 특별한 허가증이 필요합니다."),
    "transportation": ("Public transportation is the most efficient way to get around Tokyo.", "대중교통은 도쿄를 돌아다니는 가장 효율적인 방법입니다."),
    "opportunity": ("Studying abroad is an excellent opportunity to learn a new language.", "해외에서 공부하는 것은 새로운 언어를 배울 훌륭한 기회입니다."),
    "clearly": ("Please speak clearly into the microphone so everyone can hear you.", "모두가 들을 수 있도록 마이크에 대고 명확히 말씀해 주세요."),
    "ongoing": ("The police investigation into the robbery is still ongoing.", "그 강도 사건에 대한 경찰의 조사는 아직 진행 중입니다."),
    "detailed": ("The manual includes a detailed explanation of how to use the device.", "설명서에는 기기 사용법에 대한 상세한 설명이 포함되어 있습니다."),
    "alternative": ("We must find an alternative energy source to replace fossil fuels.", "우리는 화석 연료를 대체할 대안 에너지를 찾아야 합니다."),
    "obtain": ("You must obtain permission from the owner before entering the property.", "그 부지에 들어가기 전에 소유주의 허가를 얻어야 합니다."),
    "designated": ("The front seats are designated for elderly and disabled passengers.", "앞좌석은 노인과 장애인 승객들을 위해 지정되어 있습니다."),
    "intersection": ("There is a traffic light at the intersection of Main and 1st Street.", "메인가와 1번가 교차로에 신호등이 있습니다."),
    "equip": ("Our classrooms are well equipped with modern technology.", "우리 교실들은 최신 기술 장비를 잘 갖추고 있습니다."),
    "commute": ("Many people commute more than an hour to work every day.", "많은 사람들이 매일 직장으로 통근하는 데 1시간 이상 걸립니다."),
    "downtown": ("We rented a small apartment located in the downtown area.", "우리는 시내 중심가(다운타운)에 위치한 작은 아파트를 렌트했습니다."),
    "automotive": ("Detroit has long been the center of the American automotive industry.", "디트로이트는 오랫동안 미국 자동차 산업의 중심지였습니다."),
    "closure": ("The sudden closure of the factory left hundreds without jobs.", "갑작스러운 공장 폐쇄로 수백 명이 일자리를 잃었습니다."),
    "vehicle": ("No motorized vehicle is allowed on this walking trail.", "이 산책로에는 모터가 달린 차량은 허용되지 않습니다."),
    "platform": ("The train to Chicago will depart from platform number five.", "시카고행 기차가 5번 승강장에서 출발할 것입니다."),
    "official": ("The government made an official announcement regarding the tax cuts.", "정부는 세금 감면에 관한 공식 발표를 했습니다."),
    "transit": ("The goods were damaged in transit from the warehouse.", "상품들이 창고에서 수송 중에 손상되었습니다."),
    "fare": ("Bus fare has increased by ten cents this year.", "올해 버스 요금이 10센트 올랐습니다."),
    "expense": ("The trip was largely paid for at the company's expense.", "여행은 대부분 회사 경비(비용)에서 지불되었습니다."),
    "trust": ("A good relationship is built on mutual trust and respect.", "좋은 관계는 상호 신뢰와 존중에 기반을 둡니다."),
    "head": ("The team is deciding in which direction they should head next.", "그 팀은 그들이 다음에 어느 방향으로 향해야 할지 결정하고 있습니다."),
    "drive": ("She likes to take a long drive along the coast on weekends.", "그녀는 주말에 해안을 따라 길게 (차를) 운전하는 것을 좋아합니다."),
    "fine": ("He had to pay a $100 fine for running a red light.", "그는 빨간불을 무시해서 100달러의 벌금을 내야 했습니다."),
    "pass": ("You must show your security pass to enter the building.", "건물에 들어가려면 보안 통행증을 보여주어야 합니다."),
    "securely": ("Make sure your seatbelt is securely fastened before takeoff.", "이륙 전에 안전벨트가 단단하게 매어졌는지 확인하십시오."),
    "prominently": ("The NO SMOKING sign was displayed prominently in the lobby.", "금연 표지판이 로비에 눈에 띄게 게시되어 있었습니다."),
    "reserved": ("These VIP seats are strictly reserved for special guests.", "이 VIP석은 특별 손님들을 위해 엄격히 예약되어 있습니다."),
    "average": ("The average temperature in this city during winter is quite mild.", "겨울 동안 이 도시의 평균 기온은 꽤 온화합니다."),
    "collision": ("There was a serious car collision on the highway yesterday.", "어제 고속도로에서 심각한 자동차 충돌이 있었습니다."),
    "tow": ("The police had to tow his illegally parked car away.", "경찰은 그의 불법 주차된 자동차를 견인해야 했습니다."),
    "reverse": ("He had to put the car in reverse to get out of the tight parking spot.", "그는 좁은 주차 공간에서 빠져나오기 위해 차를 후진으로 넣어야 했습니다."),
    "obstruct": ("Please do not leave bags in the aisle, as they obstruct the path.", "통로를 차단하므로 복도에 가방을 두지 마십시오."),
}

def add_examples_to_day(filepath, day, examples_dict):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    i = 0
    added_count = 0
    
    while i < len(lines):
        line = lines[i]
        parts = line.rstrip('\r\n').split('\t')
        
        if len(parts) >= 3 and parts[0] == day and parts[1] in examples_dict:
            word = parts[1]
            new_lines.append(line)
            
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                next_parts = next_line.rstrip('\r\n').split('\t')
                if next_parts[0] == '':
                    new_lines.append(lines[i + 1])
                    i += 2
                    continue
            
            eng, kor = examples_dict[word]
            new_lines.append(f'\t{eng}\t{kor}\n')
            added_count += 1
        else:
            new_lines.append(line)
        
        i += 1
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"Added {added_count} examples for {day}")
    return added_count

filepath = 'public/data2.csv'
add_examples_to_day(filepath, 'day24', day24_examples)
add_examples_to_day(filepath, 'day25', day25_examples)
