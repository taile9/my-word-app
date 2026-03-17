import sys

day14_examples = {
    "international": ("The airport handles international flights from over 50 countries.", "그 공항은 50개국 이상에서 오는 국제 항공편을 처리합니다."),
    "attraction": ("The Eiffel Tower is the city's main tourist attraction.", "에펠탑은 그 도시의 주요 관광 명소입니다."),
    "itinerary": ("We received a detailed itinerary for our trip to Europe.", "우리는 유럽 여행을 위한 상세한 여행 일정을 받았습니다."),
    "exotic": ("She likes to travel to exotic locations around the world.", "그녀는 전 세계의 이국적인 장소로 여행하는 것을 좋아합니다."),
    "diverse": ("New York is known for its diverse culinary scene.", "뉴욕은 다양한 요리 문화로 유명합니다."),
    "superb": ("The weather was superb during our vacation in Hawaii.", "우리의 하와이 휴가 동안 날씨는 훌륭했습니다."),
    "baggage": ("Please do not leave your baggage unattended at any time.", "어떤 상황에서도 수하물을 방치하지 마십시오."),
    "destination": ("Our final destination is the capital city of Japan.", "우리의 최종 목적지는 일본의 수도입니다."),
    "missing": ("The airline apologized for the missing luggage and offered compensation.", "항공사는 분실된 수하물에 대해 사과하고 보상을 제공했습니다."),
    "locate": ("It took us an hour to locate the hidden waterfall.", "숨겨진 폭포의 위치를 찾아내는 데 한 시간이 걸렸습니다."),
    "approximately": ("The flight will take approximately four hours.", "비행은 대략 네 시간 걸릴 것입니다."),
    "duty": ("It is the duty of the flight attendants to ensure passenger safety.", "승객의 안전을 보장하는 것은 승무원의 의무입니다."),
    "process": ("Getting a new passport can be a lengthy process.", "새 여권을 받는 것은 긴 과정일 수 있습니다."),
    "board": ("Passengers are now welcome to board the aircraft at gate 5.", "승객 여러분은 이제 5번 게이트에서 항공기에 탑승하시기 바랍니다."),
    "comfortable": ("These new train seats are much more comfortable than the old ones.", "이 새 기차 좌석은 옛날 것보다 훨씬 더 편안합니다."),
    "declare": ("Do you have anything to declare at customs?", "세관에 신고할 물건이 있습니까?"),
    "specify": ("Please specify your meal preference when booking the flight.", "항공편을 예약할 때 선호하는 식사를 명시해 주십시오."),
    "depart": ("The train is scheduled to depart in ten minutes.", "기차는 10분 후에 출발할 예정입니다."),
    "emergency": ("In case of an emergency, put on your oxygen mask first.", "비상시에는 먼저 산소 마스크를 착용하십시오."),
    "passenger": ("Every passenger must have their boarding pass ready.", "모든 승객은 탑승권을 준비해야 합니다."),
    "outgoing": ("The outgoing flights are delayed due to bad weather.", "출발하는 항공편들이 악천후로 인해 지연되고 있습니다."),
    "tighly": ("Please hold the handrail tightly when using the escalator.", "에스컬레이터를 이용할 때 손잡이를 단단히 잡으십시오."),
    "tour": ("We booked a guided tour of the ancient ruins.", "우리는 고대 유적의 가이드 투어를 예약했습니다."),
    "carrier": ("The largest national carrier announced new routes to Asia.", "최대 국적 항공사가 아시아로 가는 새로운 노선을 발표했습니다."),
    "customarily": ("In this country, people customarily tip 15 percent at restaurants.", "이 나라에서는 사람들이 관례적으로 식당에서 15%의 팁을 줍니다."),
    "confuse": ("The complicated subway map can confuse many tourists.", "복잡한 지하철 지도는 많은 관광객들을 혼란스럽게 할 수 있습니다."),
    "arrive": ("We should arrive at the airport two hours before departure.", "우리는 출발 2시간 전에 공항에 도착해야 합니다."),
    "brochure": ("I picked up a travel brochure about the national park.", "저는 국립공원에 대한 여행 안내 책자를 집어 들었습니다."),
    "involve": ("The new security properly checks involve full-body scanners.", "새로운 적절한 보안 검사는 전신 스캐너를 포함합니다."),
    "ship": ("They ship their products to over 100 countries worldwide.", "그들은 그들의 제품을 전 세계 100개국 이상으로 수송합니다."),
    "suitcase": ("She packed everything she needed into a single suitcase.", "그녀는 필요한 모든 것을 여행가방 하나에 짐을 쌌습니다."),
    "unavailable": ("The main runway is currently unavailable due to repairs.", "주 활주로는 수리 때문에 현재 이용할 수 없습니다."),
    "fill out/in": ("Please fill out this immigration form before landing.", "착륙하기 전에 이 입국 신고서를 작성해 주십시오."),
    "customs": ("It took an hour to get through customs at the border.", "국경에서 세관을 통과하는 데 한 시간이 걸렸습니다."),
    "away": ("The hotel is located far away from the noisy city center.", "그 호텔은 시끄러운 도심에서 멀리 떨어져 있습니다."),
    "dramatic": ("The hike offers dramatic views of the coastline.", "그 하이킹 코스는 매력적인 해안선 전망을 제공합니다."),
    "hospitality": ("The local people are known for their warm hospitality towards tourists.", "현지인들은 관광객들에 대한 따뜻한 환대로 유명합니다."),
    "indulge": ("On vacation, I like to indulge in local delicacies without worrying about calories.", "휴가 때는 칼로리 걱정 없이 현지 별미에 빠지는 것을 좋아합니다."),
    "proximity": ("The hotel's close proximity to the beach makes it very popular.", "호텔이 해변에 가까이 있다는 점은 호텔을 매우 인기 있게 만듭니다."),
    "seating": ("The stadium has a seating capacity of over 60,000.", "그 경기장은 60,000명 이상의 좌석 배열을 가지고 있습니다."),
    "unlimited": ("The all-inclusive package comes with unlimited drinks and snacks.", "모든 것이 포함된 패키지에는 무제한 음료와 간식이 제공됩니다."),
}

day15_examples = {
    "proposal": ("The city council approved the proposal to build a new library.", "시의회는 새 도서관을 짓는 제안을 승인했습니다."),
    "alliance": ("The two companies formed a strategic alliance to enter the European market.", "두 회사는 유럽 시장에 진출하기 위해 전략적 동맹을 맺었습니다."),
    "stipulation": ("One stipulation of the contract is that work must finish by Friday.", "계약의 한 가지 계약 조건은 작업이 금요일까지 끝나야 한다는 것입니다."),
    "term": ("We cannot agree to the new terms of the agreement.", "우리는 새로운 합의 조건에 동의할 수 없습니다."),
    "compromise": ("After hours of negotiation, they finally reached a compromise.", "몇 시간의 협상 끝에 그들은 마침내 타협에 도달했습니다."),
    "negotiation": ("The trade negotiation between the two countries broke down.", "두 국가 간의 무역 협상이 결렬되었습니다."),
    "agreement": ("They signed an agreement to end the legal dispute.", "그들은 법적 분쟁을 끝내는 합의서에 서명했습니다."),
    "deadlock": ("The peace talks have reached a deadlock.", "평화 회담이 교착 상태에 도달했습니다."),
    "review": ("The manager will review your performance at the end of the month.", "관리자는 월말에 귀하의 성과를 검토할 것입니다."),
    "contract": ("He refused to sign the contract until he had read all the fine print.", "그는 세부 조항을 모두 읽을 때까지 계약서에 서명하기를 거부했습니다."),
    "signature": ("We need your signature at the bottom of the page.", "페이지 하단에 당신의 서명이 필요합니다."),
    "originally": ("The building was originally designed to be a hospital.", "이 건물은 원래 병원으로 설계되었습니다."),
    "direction": ("The project is moving in the right direction.", "이 프로젝트는 올바른 방향으로 나아가고 있습니다."),
    "initially": ("Initially, I thought it was a bad idea, but I changed my mind.", "처음에는 그것이 나쁜 아이디어라고 생각했지만 마음을 바꿨습니다."),
    "expire": ("My passport will expire in six months.", "제 여권은 6개월 후에 만료됩니다."),
    "collaborate": ("We plan to collaborate with researchers from other universities.", "우리는 다른 대학의 연구원들과 협력할 계획입니다."),
    "dedicate": ("She decided to dedicate her life to helping the poor.", "그녀는 가난한 사람들을 돕는 데 인생을 바치기로 결심했습니다."),
    "revised": ("Please send me the revised document by tomorrow morning.", "내일 아침까지 수정된 문서를 보내주세요."),
    "imperative": ("It is imperative that we find a solution immediately.", "우리가 즉시 해결책을 찾는 것은 피할 수 없는 의무입니다."),
    "cooperatively": ("The departments worked cooperatively to complete the project on time.", "부서들은 프로젝트를 제때 완료하기 위해 협조적으로 일했습니다."),
    "commission": ("The salesperson receives a 10% commission on every item sold.", "판매원은 판매된 모든 품목에 대해 10%의 수수료를 받습니다."),
    "omit": ("Please do not omit any important details from the report.", "보고서에서 중요한 세부 사항을 빠뜨리지 마십시오."),
    "conflict": ("There is a clear conflict of interest in this case.", "이 사건에는 명백한 이익 충돌이 있습니다."),
    "renew": ("You must renew your driver's license before it expires.", "운전면허증이 만료되기 전에 갱신해야 합니다."),
    "proficient": ("She is proficient in both English and Spanish.", "그녀는 영어와 스페인어 모두에 능숙합니다."),
    "confidentiality": ("The doctor assured the patient of complete medical confidentiality.", "의사는 환자에게 완벽한 의료 기밀을 보장했습니다."),
    "dispute": ("The two countries are involved in a territorial dispute.", "두 국가가 영토 분쟁에 휩싸여 있습니다."),
    "objection": ("The lawyer raised an objection to the irrelevant question.", "사려깊지 않은 질문에 변호사가 이의를 제기했습니다."),
    "define": ("It is difficult to define the exact meaning of happiness.", "행복의 정확한 의미를 규정하는 것은 어렵습니다."),
    "impression": ("You only get one chance to make a good first impression.", "좋은 첫인상을 남길 기회는 단 한 번뿐입니다."),
    "security": ("Security at the airport has been tightened recently.", "최근 공항의 보안이 강화되었습니다."),
    "option": ("Renting a car is one option for getting around the island.", "렌터카를 빌리는 것은 섬을 돌아다니기 위한 하나의 선택권입니다."),
    "proceed": ("Please proceed to the nearest exit in an orderly fashion.", "질서정연하게 가장 가까운 출구로 진행해 주십시오."),
    "modify": ("We may need to modify our travel plans if the weather gets worse.", "날씨가 악화되면 우리는 여행 계획을 수정해야 할 수도 있습니다."),
    "narrow": ("The police are trying to narrow down the list of suspects.", "경찰은 용의자 목록을 좁히기 위해 노력하고 있습니다."),
    "bid": ("The company won the bid to supply computers to schools.", "그 회사는 학교에 컴퓨터를 공급하는 입찰에서 이겼습니다."),
    "settle": ("They hope to settle the lawsuit out of court.", "그들은 법정 밖에서 소송을 해결하기를 희망합니다."),
    "terminate": ("The company has the right to terminate the agreement at any time.", "회사는 언제든지 합의를 종료할 권리가 있습니다."),
    "challenging": ("Learning a new language can be a challenging but rewarding experience.", "새로운 언어를 배우는 것은 도전적이지만 보람 있는 경험일 수 있습니다."),
    "foundation": ("Trust is the foundation of any successful relationship.", "신뢰는 모든 성공적인 관계의 토대입니다."),
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
add_examples_to_day(filepath, 'day14', day14_examples)
add_examples_to_day(filepath, 'day15', day15_examples)
