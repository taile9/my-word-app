import sys

day11_examples = {
    "research": ("Extensive research is required before launching a new product.", "신제품을 출시하기 전에 광범위한 연구가 필요합니다."),
    "devise": ("The team is trying to devise a more efficient workflow.", "팀은 더 효율적인 작업 흐름을 고안하려고 노력 중입니다."),
    "revolutionary": ("Their revolutionary technology completely changed the industry.", "그들의 혁명적인 기술은 업계를 완전히 변화시켰습니다."),
    "innovative": ("She was praised for her innovative approach to problem-solving.", "그녀는 문제 해결에 대한 혁신적인 접근으로 찬사를 받았습니다."),
    "feature": ("The software's best feature is its user-friendly interface.", "이 소프트웨어의 가장 큰 특징은 사용자 친화적인 인터페이스입니다."),
    "inspiration": ("Nature provided the inspiration for her latest architectural design.", "자연은 그녀의 최신 건축 디자인에 영감을 제공했습니다."),
    "sufficiently": ("The meat must be cooked sufficiently to be safe to eat.", "고기는 먹기에 안전하도록 충분히 조리되어야 합니다."),
    "patent": ("The inventor filed a patent to protect his new device.", "발명가는 그의 새 장치를 보호하기 위해 특허를 출원했습니다."),
    "envision": ("It is hard to envision what the city will look like in 50 years.", "50년 후에 도시가 어떤 모습일지 상상하기 어렵습니다."),
    "extend": ("We have decided to extend the deadline by one week.", "우리는 마감 기한을 일주일 연장하기로 결정했습니다."),
    "following": ("Following the meeting, a summary email will be sent to all attendees.", "회의 후에 모든 참석자에게 요약 이메일이 발송될 것입니다."),
    "intend": ("We intend to open three new stores by the end of the year.", "우리는 연말까지 세 개의 새 매장을 열 작정입니다."),
    "grant": ("The university received a government grant for scientific research.", "대학교는 과학 연구를 위한 정부 보조금을 받았습니다."),
    "allow": ("The new system will allow employees to work from home twice a week.", "새 시스템은 직원들이 일주일에 두 번 재택근무를 할 수 있게 허락할 것입니다."),
    "inspect": ("Safety engineers inspect the building annually.", "안전 엔지니어들이 매년 건물을 검사합니다."),
    "improve": ("He reads English newspapers every day to improve his vocabulary.", "그는 어휘력을 향상시키기 위해 매일 영자 신문을 읽습니다."),
    "increasingly": ("Online shopping is becoming increasingly popular.", "온라인 쇼핑이 점점 더 인기를 얻고 있습니다."),
    "invest": ("It is important to invest in employee training programs.", "직원 교육 프로그램에 투자하는 것이 중요합니다."),
    "various": ("The store offers products in various colors and sizes.", "매장은 가지각색의 색상과 크기의 제품을 제공합니다."),
    "upgrade": ("You should upgrade your software to get the latest features.", "최신 기능을 얻으려면 소프트웨어를 업그레이드해야 합니다."),
    "manual": ("Please refer to the user manual if you have any difficulties installing the device.", "기기 설치에 어려움이 있으면 사용 설명서를 참조하세요."),
    "explore": ("The committee will explore different options to cut costs.", "위원회는 비용을 줄이기 위해 다른 선택지들을 조사할 것입니다."),
    "response": ("We received a positive response from the client regarding our proposal.", "우리는 제안에 관해 고객으로부터 긍정적인 응답을 받았습니다."),
    "appearance": ("Professional appearance is expected during client meetings.", "고객 회의 동안 전문적인 외모가 요구됩니다."),
    "successful": ("The marketing campaign was highly successful and boosted sales.", "마케팅 캠페인은 매우 성공적이었고 판매를 증가시켰습니다."),
    "hold": ("The company will hold its annual banquet next Friday.", "회사는 다음 주 금요일에 연례 만찬을 열 것입니다."),
    "advance": ("Medical advance has doubled human life expectancy over the past century.", "의학의 진보는 지난 세기 동안 인간의 기대 수명을 두 배로 늘렸습니다."),
    "reliable": ("We need to find a reliable supplier for raw materials.", "우리는 원자재를 위한 믿을 만한 공급업체를 찾아야 합니다."),
    "quality": ("The company prides itself on the high quality of its products.", "회사는 자사 제품의 높은 품질을 자랑스럽게 생각합니다."),
    "domestic": ("Domestic flights depart from terminal 2.", "국내선 항공편은 2터미널에서 출발합니다."),
    "development": ("Sustainable development is a key goal for modern cities.", "지속 가능한 발전은 현대 도시들의 주요 목표입니다."),
    "availability": ("Please check your manager's availability before scheduling the meeting.", "회의 일정을 잡기 전에 매니저가 시간이 있는지 확인해 주세요."),
    "update": ("The app will automatically download and install the latest update.", "앱은 최신 업데이트를 자동으로 다운로드하고 설치할 것입니다."),
    "accurate": ("The report must contain accurate sales figures.", "보고서에는 정확한 판매 수치가 포함되어야 합니다."),
    "complicate": ("Unnecessary regulations only complicate the process.", "불필요한 규정들은 과정을 오히려 복잡하게 만듭니다."),
    "accomplished": ("She is an accomplished pianist who has performed worldwide.", "그녀는 세계적으로 공연을 해온 숙련된 피아니스트입니다."),
    "inquiry": ("If you have any questions, please direct your inquiry to the help desk.", "질문이 있으시면 도움창구로 문의해 주십시오."),
    "indication": ("The sudden drop in temperature is an indication that winter is coming.", "갑작스러운 기온 하락은 겨울이 오고 있다는 징후입니다."),
    "manufacturer": ("The car manufacturer announced a recall of 5,000 vehicles.", "자동차 제조회사는 5,000대의 차량 리콜을 발표했습니다."),
    "compatible": ("This software is fully compatible with both Windows and Mac operating systems.", "이 소프트웨어는 윈도우와 맥 운영체제 모두와 완벽하게 호환됩니다."),
    "superior": ("This new processor offers superior performance compared to older models.", "이 새 프로세서는 구형 모델에 비해 우수한 성능을 제공합니다."),
    "absolute": ("Absolute silence is required in the library.", "도서관에서는 완전한 정숙이 요구됩니다."),
    "broaden": ("Traveling is a great way to broaden your perspective.", "여행은 시야를 넓히는 훌륭한 방법입니다."),
    "corrosion": ("Special paint is applied to the metal to prevent active corrosion.", "금속이 활발하게 부식되는 것을 막기 위해 특수 페인트가 칠해집니다."),
}

day12_examples = {
    "epuipment": ("Safety equipment must be worn at all times in the laboratory.", "실험실에서는 항상 안전 장비를 착용해야 합니다."),
    "automate": ("The factory plans to automate several manual assembly processes.", "공장은 몇 가지 수동 조립 공정을 자동화할 계획입니다."),
    "specification": ("The new computer meets all the required technical specifications.", "새 컴퓨터는 요구되는 모든 기술적 사양을 충족합니다."),
    "properly": ("Make sure the machine is properly cleaned after use.", "사용 후 기계가 제대로 청소되었는지 확인하십시오."),
    "safety": ("Passenger safety is the airline's highest priority.", "승객의 안전은 항공사의 최우선 사항입니다."),
    "precaution": ("As a precaution, please back up your data before updating the software.", "예방 조치로 소프트웨어 업데이트 전에 데이터를 백업하십시오."),
    "operate": ("You need a license to operate this heavy machinery.", "이 중장비를 작동하려면 자격증이 필요합니다."),
    "processing": ("The processing of your visa application may take up to three weeks.", "비자 신청 처리는 최대 3주가 소요될 수 있습니다."),
    "capacity": ("The stadium has a seating capacity of 50,000 people.", "경기장의 수용 인원은 50,000명입니다."),
    "assemble": ("It takes about two hours to assemble the furniture.", "가구를 조립하는 데 약 두 시간이 걸립니다."),
    "utilize": ("We should fully utilize all the resources available to us.", "우리는 사용 가능한 모든 자원을 충분히 활용해야 합니다."),
    "place": ("Please place the fragile items carefully in the box.", "부서지기 쉬운 물건들을 상자 안에 조심해서 넣어두세요."),
    "fill": ("The company hired more staff to fill the increasing number of orders.", "회사는 증가하는 주문을 이행하기 위해 더 많은 직원을 고용했습니다."),
    "manufacturing": ("The region is known for its automobile manufacturing industry.", "이 지역은 자동차 제조업으로 유명합니다."),
    "renovate": ("They plan to renovate the old hotel to attract more tourists.", "그들은 더 많은 관광객을 유치하기 위해 오래된 호텔을 보수할 계획입니다."),
    "decision": ("The board will make a final decision by the end of the week.", "이사회는 이번 주말까지 최종 결정을 내릴 것입니다."),
    "material": ("We only use high-quality material for our products.", "우리는 우리 제품에 고품질 재료만을 사용합니다."),
    "success": ("The launch of the new product was a huge success.", "새 제품의 출시는 큰 성공이었습니다."),
    "attribute": ("He attributes his success to hard work and dedication.", "그는 자신의 성공을 노력과 헌신의 덕분으로 돌립니다."),
    "efficiency": ("The new software will improve the efficiency of our daily operations.", "새 소프트웨어는 우리의 일일 작업 능률을 높여줄 것입니다."),
    "limit": ("There is a strict time limit for the exam.", "시험에는 엄격한 시간 제한이 있습니다."),
    "tailored": ("We provide financial advice tailored to each client's specific needs.", "우리는 각 고객의 구체적인 요구에 맞춘 재정 조언을 제공합니다."),
    "component": ("The motherboard is a critical component of any computer system.", "메인보드는 모든 컴퓨터 시스템의 핵심 부품입니다."),
    "capable": ("She is clearly capable of handling the demands of the job.", "그녀는 그 업무의 요구사항을 감당할 수 있는 능력이 분명히 있습니다."),
    "economize": ("We need to find ways to economize on office supplies.", "우리는 사무용품을 절약할 방법을 찾아야 합니다."),
    "flexible": ("Our company offers flexible working hours for parents.", "우리 회사는 부모들에게 융통성 있는 근무 시간을 제공합니다."),
    "comparable": ("The weather here is comparable to that of Southern California.", "이곳의 날씨는 남부 캘리포니아의 날씨와 필적할 만합니다."),
    "produce": ("The factory can produce up to 1,000 units per day.", "그 공장은 하루에 최대 1,000대를 생산할 수 있습니다."),
    "respectively": ("John and Mary won the first and second prizes respectively.", "존과 메리는 각각 1등상과 2등상을 받았습니다."),
    "device": ("This security device will alert you if anyone tries to enter.", "이 보안 장치는 누군가 침입하려고 시도하면 경보를 울릴 것입니다."),
    "trim": ("The company had to trim its budget due to financial difficulties.", "회사는 재정적 어려움 때문에 예산을 삭감해야 했습니다."),
    "launch": ("The tech giant will launch its new smartphone next month.", "그 거대 기술 기업은 다음 달에 새 스마트폰을 출시할 것입니다."),
    "separately": ("Please submit your resume and portfolio separately.", "이력서와 포트폴리오를 별도로 제출해 주십시오."),
    "expiration": ("Check the expiration date on the milk before drinking it.", "우유를 마시기 전에 유통기한 만료일을 확인하십시오."),
    "maneuver": ("It is difficult to maneuver a large truck through these narrow streets.", "이 좁은 거리에서 큰 트럭을 움직이는 것은 어렵습니다."),
    "coming": ("We need to prepare for the coming winter storm.", "우리는 다가오는 겨울 폭풍에 대비해야 합니다."),
    "damaged": ("The goods were damaged during transportation.", "화물은 수송 중에 손상을 입었습니다."),
    "prevent": ("Regular maintenance can prevent costly breakdowns.", "정기적인 유지보수는 비용이 많이 드는 고장을 예방할 수 있습니다."),
    "power": ("The solar panels provide enough power for the entire building.", "태양열 패널은 건물 전체에 충분한 전력을 제공합니다."),
    "chemical": ("Exposure to toxic chemicals can cause serious health problems.", "유독 화학제품에 노출되면 심각한 건강 문제를 일으킬 수 있습니다."),
}

day13_examples = {
    "complaint": ("The restaurant received a complaint about the cold food.", "식당은 차가운 음식에 대한 불평을 받았습니다."),
    "deal": ("The customer service team knows how to deal with angry clients.", "고객 서비스 팀은 화난 고객을 처리하는 방법을 알고 있습니다."),
    "argumentative": ("He became argumentative when his mistakes were pointed out.", "그는 자신의 실수가 지적되자 논쟁적인 태도를 보였습니다."),
    "appropriately": ("Please dress appropriately for the formal dinner.", "공식 만찬에 적절하게 차려입어 주십시오."),
    "respond": ("The fire department responded quickly to the emergency call.", "소방서는 긴급 신고에 신속하게 응답했습니다."),
    "infuriate": ("The long delay infuriated many passengers at the airport.", "긴 지연은 공항의 많은 승객들을 격분시켰습니다."),
    "curteous": ("The hotel staff was extremely courteous and helpful.", "호텔 직원은 매우 예의바르고 도움이 되었습니다."),
    "satisfaction": ("Customer satisfaction is our top priority.", "고객 만족이 우리의 최우선 사항입니다."),
    "inconvenience": ("We apologize for any inconvenience caused by the construction.", "공사로 인해 불편을 드려 죄송합니다."),
    "complete": ("You must complete the entire form before submitting it.", "제출하기 전에 전체 양식을 완료해야 합니다."),
    "specific": ("Can you give me specific details about the project timeline?", "프로젝트 일정에 대한 구체적인 세부 사항을 알려주시겠어요?"),
    "return": ("If you are not satisfied, you can return the item within 30 days.", "만족하지 않으시면 30일 이내에 물품을 반환하실 수 있습니다."),
    "replace": ("We will replace any defective products free of charge.", "우리는 결함이 있는 제품은 무료로 교체해 드립니다."),
    "presentation": ("Her presentation on market trends was highly informative.", "시장 동향에 대한 그녀의 발표는 매우 유익했습니다."),
    "evaluation": ("The manager will conduct a performance evaluation next week.", "관리자는 다음 주에 성과 평가를 실시할 것입니다."),
    "confident": ("The team feels confident about winning the upcoming match.", "팀은 다가오는 경기에서 이길 것이라고 자신합니다."),
    "cause": ("Investigators are trying to determine the cause of the fire.", "조사관들은 화재의 원인을 밝혀내려 노력하고 있습니다."),
    "commentary": ("The sports channel provided live commentary during the soccer game.", "스포츠 채널은 축구 경기 동안 라이브 해설을 제공했습니다."),
    "notification": ("You will receive a notification when your package is shipped.", "당신의 소포가 배송되면 통지를 받게 될 것입니다."),
    "apologize": ("I want to sincerely apologize for the misunderstanding.", "나는 오해에 대해 진심으로 사과하고 싶습니다."),
    "interact": ("Teachers encourage students to interact with each other during class.", "교사들은 수업 시간에 학생들이 서로 소통하도록 격려합니다."),
    "certain": ("Are you certain that the meeting starts at 9 AM?", "회의가 오전 9시에 시작하는게 확실합니까?"),
    "commitment": ("The CEO praised the staff for their commitment to excellence.", "CEO는 직원들의 탁월함에 대한 헌신을 칭찬했습니다."),
    "applaud": ("The audience stood up to applaud the brilliant performance.", "관객들은 훌륭한 공연에 박수를 보내기 위해 일어섰습니다."),
    "biography": ("He wrote a fascinating biography of the former president.", "그는 전직 대통령의 매혹적인 전기를 썼습니다."),
    "critical": ("Clean water is critical to the survival of the village.", "깨끗한 물은 마을 생존에 매우 중요합니다."),
    "depend on": ("Local businesses heavily depend on summer tourism.", "지역 상점들은 여름 관광업에 크게 의존합니다."),
    "combine": ("The new formula combines several active ingredients.", "새로운 공식은 여러 활성 성분을 결합시킵니다."),
    "priority": ("Fixing the software bug is our top priority.", "소프트웨어 버그를 수정하는 것이 우리의 최우선 사항입니다."),
    "observe": ("Visitors must observe the safety rules inside the factory.", "방문객들은 공장 내부의 안전 규칙을 준수해야 합니다."),
    "defective": ("Please return the defective merchandise to the store for a full refund.", "결함이 있는 상품은 전액 환불을 위해 상점으로 반환해 주십시오."),
    "reflect": ("His harsh words do not reflect the views of the entire company.", "그의 거친 말은 회사 전체의 견해를 반영하지 않습니다."),
    "attitude": ("A positive attitude can help you overcome many challenges.", "긍정적인 마음가짐은 당신이 많은 어려움을 극복하는 데 도움이 될 수 있습니다."),
    "disappoint": ("I am sorry to disappoint you, but the concert is sold out.", "당신을 실망시켜 미안하지만, 콘서트는 매진되었습니다."),
    "inquire": ("I called to inquire about the status of my application.", "내 지원서의 진행 상황을 문의하기 위해 전화했습니다."),
    "insert": ("Please insert your credit card into the machine.", "기계에 귀하의 신용카드를 삽입해 주십시오."),
    "disclose": ("The company refused to disclose details of the financial deal.", "회사는 재정 거래의 세부 사항을 공개하는 것을 거부했습니다."),
    "guarantee": ("We guarantee that our products are 100% organic.", "우리는 우리 제품이 100% 유기농임을 보장합니다."),
    "politely": ("The receptionist politely asked the guest to wait in the lobby.", "접수 담당자는 손님에게 로비에서 기다려달라고 공손하게 요청했습니다."),
    "seriously": ("You need to take your doctor's advice seriously.", "당신은 의사의 조언을 진지하게 받아들일 필요가 있습니다."),
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
add_examples_to_day(filepath, 'day11', day11_examples)
add_examples_to_day(filepath, 'day12', day12_examples)
add_examples_to_day(filepath, 'day13', day13_examples)
