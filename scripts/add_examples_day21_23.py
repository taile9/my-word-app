import sys

day21_examples = {
    "announce": ("The company will announce its quarterly earnings tomorrow.", "회사는 내일 분기별 수익을 발표할 것입니다."),
    "interested": ("We are very interested in your new software product.", "우리는 귀사의 새 소프트웨어 제품에 매우 관심이 있습니다."),
    "active": ("She remains an active member of the local community.", "그녀는 지역 사회의 적극적인 일원으로 남아있습니다."),
    "accept": ("The store does not accept personal checks as payment.", "그 매장은 개인 수표를 결제 수단으로 받아들이지 않습니다."),
    "foresee": ("I do not foresee any major problems with this project.", "나는 이 프로젝트에 어떤 주요 문제도 예견하지 않습니다."),
    "expansion": ("The business is planning a major expansion into Europe next year.", "그 사업체는 내년에 유럽으로의 대규모 확장을 계획하고 있습니다."),
    "relocate": ("The headquarters will relocate to a larger building next month.", "본사는 다음 달에 더 큰 건물로 이전할 것입니다."),
    "competitor": ("We must always stay one step ahead of our main competitor.", "우리는 항상 주요 경쟁업체보다 한 발 앞서 있어야 합니다."),
    "asset": ("A skilled workforce is a company's greatest asset.", "숙련된 인력은 회사의 가장 큰 자산입니다."),
    "contribute": ("Every team member is expected to contribute to the project's success.", "모든 팀원은 프로젝트의 성공에 기여할 것으로 기대됩니다."),
    "dedicated": ("He is a dedicated employee who often works on weekends.", "그는 주말에도 자주 일하는 헌신적인 직원입니다."),
    "misplace": ("I seem to have misplaced my car keys somewhere in the office.", "내가 사무실 어딘가에 자동차 열쇠를 잘못 둔 것 같습니다."),
    "considerable": ("The project requires a considerable amount of time and money.", "그 프로젝트는 상당한 양의 시간과 돈을 요구합니다."),
    "last": ("The effect of the medicine will last for about four hours.", "그 약의 효과는 약 4시간 동안 지속될 것입니다."),
    "emerge": ("Several new tech companies have emerged in the region recently.", "최근 이 지역에 몇몇 새로운 기술 기업들이 나타났습니다."),
    "grow": ("The national economy is expected to grow by 3% this year.", "올해 국가 경제는 3% 성장할 것으로 예상됩니다."),
    "select": ("Please select the shipping method that best suits your needs.", "당신의 필요에 가장 잘 맞는 배송 방법을 선택해 주십시오."),
    "merge": ("The two airlines voted to merge into a single corporation.", "두 항공사는 단일 기업으로 합병하기로 투표했습니다."),
    "imply": ("His silence seemed to imply that he agreed with the decision.", "그의 침묵은 그가 그 결정에 동의한다는 것을 암시하는 것 같았습니다."),
    "vital": ("Regular updates are vital for the security of your computer.", "정기적인 업데이트는 컴퓨터 보안에 필수적입니다."),
    "persist": ("If the symptoms persist for more than a week, consult a doctor.", "증상이 1주일 이상 지속되면 의사와 상의하십시오."),
    "independent": ("We need an independent committee to review the financial reports.", "재무 보고서를 검토하기 위해 독립적인 위원회가 필요합니다."),
    "force": ("The new regulations will force companies to reduce emissions.", "새로운 규정들은 회사들이 배출량을 줄이도록 강요할 것입니다."),
    "establish": ("The university plans to establish a new research center.", "그 대학은 새로운 연구 센터를 설립할 계획입니다."),
    "initiate": ("The government will initiate a new health program next month.", "정부는 다음 달에 새로운 건강 프로그램을 시작할 것입니다."),
    "enhance": ("Adding spices can greatly enhance the flavor of the dish.", "향신료를 추가하는 것은 요리의 풍미를 크게 향상시킬 수 있습니다."),
    "renowned": ("He is a world-renowned expert in the field of neuroscience.", "그는 신경과학 분야에서 세계적으로 유명한 전문가입니다."),
    "informed": ("We will keep you informed of any changes to the schedule.", "일정 변경 사항이 있으면 알려드리겠습니다."),
    "minutes": ("The secretary will take the minutes during the board meeting.", "비서가 이사회 동안 회의록을 작성할 것입니다."),
    "waive": ("The bank agreed to waive the overdraft fee just this once.", "은행은 이번 한 번만 초과 인출 수수료를 면제해 주기로 동의했습니다."),
    "reach": ("Please call me when you reach the hotel.", "호텔에 도착하면 제게 전화해 주십시오."),
    "authority": ("Only the manager has the authority to approve a refund.", "오직 매니저만이 환불을 승인할 권한을 가지고 있습니다."),
    "acquire": ("The museum recently acquired a rare painting by Van Gogh.", "그 박물관은 최근에 반 고흐의 희귀한 그림을 획득했습니다."),
    "surpass": ("This year's sales figures surpass all our previous records.", "올해의 판매 수치는 우리의 모든 이전 기록들을 능가합니다."),
    "run": ("He has been running his own business for the past ten years.", "그는 지난 10년 동안 자신의 사업을 운영해오고 있습니다."),
    "improbable": ("It is highly improbable that it will snow in August.", "8월에 눈이 내릴 가능성은 매우 낮습니다."),
    "edge": ("Our advanced technology gives us a competitive edge in the market.", "우리의 첨단 기술은 시장에서 우리에게 경쟁 우위를 제공합니다."),
    "simultaneously": ("The concert was broadcast simultaneously on TV and the internet.", "그 콘서트는 TV와 인터넷에 동시에 방송되었습니다."),
    "reveal": ("The company will reveal its new product design tomorrow.", "회사는 내일 새 제품 디자인을 공개할 것입니다."),
    "productivity": ("Taking regular breaks can actually increase your productivity.", "규칙적인 휴식을 취하는 것은 실제로 생산성을 높일 수 있습니다."),
    "uncertain": ("The future of the project remains uncertain due to budget cuts.", "예산 삭감으로 인해 파생된 그 프로젝트의 미래는 불확실한 상태로 남아있습니다."),
    "premier": ("This is the premier resort for luxury vacations in the country.", "이곳은 그 나라에서 호화로운 휴가를 위한 최고의 리조트입니다."),
}

day22_examples = {
    "agenda": ("The first item on today's agenda is the budget review.", "오늘 의제의 첫 번째 항목은 예산 검토입니다."),
    "convene": ("The committee will convene tomorrow morning to discuss the issue.", "위원회는 그 문제를 논의하기 위해 내일 아침에 모일 것입니다."),
    "refute": ("The lawyer presented evidence to refute the witness's statement.", "변호사는 증인의 진술을 반박하기 위한 증거를 제시했습니다."),
    "coordination": ("Successful event planning requires good coordination among all staff.", "성공적인 행사 기획은 모든 직원들 간의 원활한 조정(협동)을 요구합니다."),
    "unanimous": ("The board members reached a unanimous decision to sell the factory.", "이사회 이사들은 공장을 매각하기로 만장일치의 결정을 내렸습니다."),
    "convince": ("She tried to convince her boss to give her a raise.", "그녀는 상사에게 급여 인상을 해달라고 설득하려고 노력했습니다."),
    "consensus": ("After hours of debate, the group finally reached a consensus.", "몇 시간의 토론 끝에 그 그룹은 마침내 여론(합의)에 도달했습니다."),
    "defer": ("They decided to defer the launch date until the software is bug-free.", "그들은 소프트웨어의 버그가 없어질 때까지 출시일을 연기하기로 결정했습니다."),
    "usually": ("I usually drink a cup of coffee before starting work.", "나는 보통 일을 시작하기 전에 커피 한 잔을 마십니다."),
    "reschedule": ("We need to reschedule the meeting for next Tuesday.", "우리는 회의 일정을 다음 주 화요일로 변경해야 합니다."),
    "meeting": ("The weekly staff meeting will take place in room 204.", "주간 직원 회의는 204호에서 열릴 것입니다."),
    "determine": ("The investigation will determine the true cause of the accident.", "그 조사는 사고의 진짜 원인을 알아낼(결정할) 것입니다."),
    "report": ("Please submit your final report by the end of the week.", "이번 주말까지 귀하의 최종 보고서를 제출해 주십시오."),
    "comment": ("Our manager declined to comment on the recent rumors.", "우리 관리자는 최근 소문에 대해 언급하기를 거부했습니다."),
    "phase": ("The construction project is entering its final phase.", "건설 프로젝트가 마지막 단계(국면)에 접어들고 있습니다."),
    "approve": ("The city council will vote to approve the new building guidelines.", "시의회는 새 건축 지침을 승인하기 위해 투표할 것입니다."),
    "enclosed": ("Please find a copy of the contract enclosed with this letter.", "이 편지에 동봉된 계약서 사본을 확인해 주십시오."),
    "easy": ("This new software is very easy for beginners to learn.", "이 새 소프트웨어는 초보자들이 배우기에 매우 쉽습니다."),
    "record": ("The athlete broke the world record for the 100-meter sprint.", "그 육상 선수는 100미터 달리기 세계 기록을 경신했습니다."),
    "suggestion": ("I am open to any suggestion that could improve our workflow.", "나는 우리의 작업 흐름을 개선할 수 있는 어떤 제안에도 열려 있습니다."),
    "attention": ("The speaker asked for the audience's full attention.", "연사는 청중들의 완전한 주의 집중을 요청했습니다."),
    "object": ("Several residents objected to the construction of the new highway.", "몇몇 주민들이 새 고속도로 건설에 반대했습니다."),
    "coincidentally": ("Coincidentally, we both bought the exact same shirt yesterday.", "우연히도, 우리 둘 다 어제 정확히 똑같은 셔츠를 샀습니다."),
    "crowded": ("The subway is always extremely crowded during rush hour.", "지하철은 출퇴근 시간 동안 항상 극도로 붐빕니다."),
    "undergo": ("The company will undergo a major restructuring process this year.", "회사는 올해 대대적인 구조조정 과정을 겪을 것입니다."),
    "outcome": ("We are waiting for the final outcome of the presidential election.", "우리는 대통령 선거의 최종 결과를 기다리고 있습니다."),
    "narrowly": ("She narrowly avoiding hitting the car in front of her.", "그녀는 앞차와 부딪치는 것을 주의 깊게(가까스로) 피했습니다."),
    "differ": ("The two experts differ in their opinions on how to solve the problem.", "두 전문가는 문제를 해결하는 방법에 대한 의견이 다릅니다."),
    "discuss": ("We need to discuss the new marketing strategy tomorrow.", "우리는 내일 새로운 마케팅 전략을 논의해야 합니다."),
    "give": ("Please give this envelope to the receptionist on your way out.", "나가는 길에 이 봉투를 접수원에게 주십시오."),
    "brief": ("The manager held a brief meeting to update the team on the project status.", "관리자는 프로젝트 진행 상황을 팀에 간략히 알리는 짧은 회의를 열었습니다."),
    "distract": ("Loud noises can easily distract people from their work.", "큰 소음은 쉽게 사람들을 일에서 산만하게(주의를 분산시키게) 할 수 있습니다."),
    "emphasis": ("Our school places a strong emphasis on science and math education.", "우리 학교는 과학과 수학 교육에 강한 강조를 둡니다."),
    "press": ("The press conference will be held in the main lobby at 2 PM.", "기자 회견은 오후 2시에 메인 로비에서 열릴 것입니다."),
    "organize": ("She helped to organize the charity event last week.", "그녀는 지난주 자선 행사를 정리(준비)하는 것을 도왔습니다."),
    "mention": ("Did the boss mention anything about our upcoming bonuses?", "사장님이 다가오는 우리의 보너스에 대해 언급하셨나요?"),
    "persuasive": ("He made a very persuasive argument for increasing the budget.", "그는 예산 증가에 대한 매우 설득력 있는 주장을 했습니다."),
    "understanding": ("The two companies reached an understanding on the partnership terms.", "두 회사는 파트너십 조건에 대한 이해(합의)에 도달했습니다."),
    "adjourn": ("The judge decided to adjourn the trial until Monday morning.", "판사는 월요일 아침까지 재판을 휴회하기로 결정했습니다."),
    "constructive": ("We welcome any constructive criticism from our users.", "우리는 사용자들의 어떠한 건설적인 비판도 환영합니다."),
    "preside": ("The CEO will preside over the annual shareholders' meeting.", "CEO가 연례 주주 총회의 사회를 볼 것입니다."),
    "irrelevant": ("Please do not bring up issues that are irrelevant to the current topic.", "현재 주제와 관계가 없는 문제들은 꺼내지 마십시오."),
    "constraint": ("Due to time constraints, we will skip the Q&A session today.", "시간상의 제약 때문에 오늘은 질의응답 시간을 생략하겠습니다."),
}

day23_examples = {
    "host": ("Our city will host the international film festival next year.", "우리 도시는 내년에 국제 영화제를 주최할 것입니다."),
    "annual": ("The company's annual revenue exceeded 10 million dollars.", "그 회사의 연간 수익은 1000만 달러를 초과했습니다."),
    "purpose": ("The main purpose of this meeting is to brainstorm new ideas.", "이 회의의 주된 목적은 새로운 아이디어를 구상하는 것입니다."),
    "enroll": ("Many students wish to enroll in the advanced computer science class.", "많은 학생들이 고급 컴퓨터 과학 수업에 등록하기를 희망합니다."),
    "lecture": ("The professor gave a brilliant lecture on modern history.", "그 교수는 현대사에 대한 훌륭한 강의를 했습니다."),
    "participant": ("Every participant will receive a certificate of completion.", "모든 참석자는 수료증을 받을 것입니다."),
    "attend": ("All employees are required to attend the safety training session.", "모든 직원들은 안전 교육 세션에 참석해야 합니다."),
    "encourage": ("We encourage our staff to share their creative ideas freely.", "우리는 직원들이 창의적인 아이디어를 자유롭게 공유하도록 장려합니다."),
    "leave": ("Please leave your keys at the front desk when you check out.", "체크아웃할 때 프런트 데스크에 열쇠를 놔두고 가십시오."),
    "recommendation": ("I bought this book based on my friend's strong recommendation.", "나는 친구의 강력한 추천을 바탕으로 이 책을 샀습니다."),
    "conference": ("The medical conference will be held at the convention center.", "그 의학 회의는 컨벤션 센터에서 열릴 것입니다."),
    "schedule": ("The train is running exactly on schedule today.", "오늘은 기차가 정확히 일정대로 운행되고 있습니다."),
    "include": ("Does the accommodation price include breakfast?", "숙박 요금에 아침 식사가 포함되어 있나요?"),
    "result": ("The positive result of the blood test was a huge relief.", "혈액 검사의 긍정적인 결과는 큰 안도감이었습니다."),
    "register": ("You must register online before attending the workshop.", "워크숍에 참석하기 전에 반드시 온라인으로 등록해야 합니다."),
    "require": ("This demanding job will require your full dedication.", "이 힘든 일은 당신의 완전한 헌신을 요구할 것입니다."),
    "grateful": ("We are deeply grateful for your generous donation to the charity.", "우리는 자선 단체에 대한 당신의 관대한 기부에 깊이 감사하고 있습니다."),
    "overtime": ("Employees are paid double for working overtime on weekends.", "직원들은 주말 초과근무에 대해 두 배의 임금을 받습니다."),
    "responsibility": ("It is your responsibility to ensure the doors are locked at night.", "밤에 문이 잠겨 있는지 확인하는 것은 당신의 책임입니다."),
    "assent": ("The president gave his formal assent to the new bill.", "대통령은 새 법안에 공식적인 찬성(동의)을 표명했습니다."),
    "regard": ("The board members regard him as a highly competent manager.", "이사회 구성원들은 그를 매우 유능한 관리자로 간주합니다."),
    "tentative": ("We have made a tentative schedule, but it may change later.", "우리는 임시 일정을 세웠지만 나중에 변경될 수 있습니다."),
    "welcome": ("The mayor gave a warm welcome to the visiting delegation.", "시장은 방문 대표단에게 따뜻한 환영을 보냈습니다."),
    "function": ("The primary function of this organ is to filter the blood.", "이 기관의 주요 기능은 혈액을 걸러내는 것입니다."),
    "commence": ("The opening ceremony will commence promptly at 10 AM.", "개막식은 오전 10시 정각에 시작될 것입니다."),
    "objective": ("Our main objective for this quarter is to increase online sales.", "이번 분기의 주요 목표는 온라인 판매를 증가시키는 것입니다."),
    "excited": ("The children were incredibly excited about their trip to Disneyland.", "아이들은 디즈니랜드 여행에 대해 믿을 수 없을 정도로 신났습니다."),
    "reimbursement": ("Please submit your receipts to the finance department for reimbursement.", "상환을 위해 재무 부서에 영수증을 제출해 주십시오."),
    "treatment": ("The patient responded well to the medical treatment.", "그 환자는 의학적 치료에 좋은 반응을 보였습니다."),
    "honor": ("It is a great honor to receive this prestigious award.", "이 명망 있는 상을 받는 것은 큰 영예입니다."),
    "emphasize": ("The speaker continued to emphasize the importance of teamwork.", "연사는 미팅 내내 팀워크의 중요성을 강조했습니다."),
    "entry": ("The sign strictly prohibited unauthorized entry into the building.", "표지판은 건물에 허가 없는 입장을 엄격히 금지했습니다."),
    "bonus": ("All employees will receive a holiday bonus at the end of the year.", "모든 직원들은 연말에 휴일 상여금을 받을 것입니다."),
    "salary": ("She was offered a higher starting salary at the new company.", "그녀는 새 회사에서 더 높은 초봉을 제안받았습니다."),
    "earn": ("It takes years of hard work to earn a promotion in this firm.", "이 회사에서 승진을 (노력으로) 얻으려면(벌려면) 수년간의 헌신이 필요합니다."),
    "arise": ("Unexpected problems may arise during the construction phase.", "건설 단계 동안 예상치 못한 문제가 발생할 수 있습니다."),
    "labor": ("The cost of manual labor has increased significantly recently.", "수작업에 들어가는 노동(비용)이 최근 크게 올랐습니다."),
    "union": ("The labor union is negotiating a new contract with management.", "노동조합은 경영진과 새 계약을 협상하고 있습니다."),
    "existing": ("The software update is compatible with all existing models.", "소프트웨어 업데이트는 모든 기존의 모델들과 호환됩니다."),
    "exploit": ("The company was accused of trying to exploit its temporary workers.", "그 회사는 임시직 근로자들을 착취하려 했다는 비난을 받았습니다."),
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
add_examples_to_day(filepath, 'day21', day21_examples)
add_examples_to_day(filepath, 'day22', day22_examples)
add_examples_to_day(filepath, 'day23', day23_examples)
