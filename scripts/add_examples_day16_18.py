import sys

day16_examples = {
    "completely": ("The new software is completely different from the older version.", "새 소프트웨어는 이전 버전과 완전히 다릅니다."),
    "refuse": ("The store may refuse to accept returns without a receipt.", "매장은 영수증 없는 반품을 거절할 수 있습니다."),
    "temporarily": ("The service will be temporarily unavailable during maintenance.", "유지보수 기간 동안 서비스가 일시적으로 중단될 것입니다."),
    "dealer": ("You can buy this car from any authorized dealer.", "이 차는 공인 딜러를 통해 구입할 수 있습니다."),
    "bulk": ("Buying wholesale items in bulk can save you a lot of money.", "도매 물품을 대량으로 구매하면 많은 돈을 절약할 수 있습니다."),
    "inventory": ("The store conducts a full inventory check every month.", "매장은 매달 전체 재고 조사를 실시합니다."),
    "short": ("We are running short on office supplies this week.", "이번 주에는 사무용품이 부족합니다."),
    "cost": ("The total cost of the project exceeded our initial budget.", "프로젝트의 총비용이 우리의 초기 예산을 초과했습니다."),
    "selection": ("This supermarket offers a wide selection of fresh fruits.", "이 슈퍼마켓은 매우 다양한 신선한 과일을 제공합니다."),
    "commercial": ("The area is known for its high-rise commercial buildings.", "이 지역은 고층 상업 건물들로 유명합니다."),
    "order": ("Please place your order by 3 PM for next-day delivery.", "다음 날 배송을 원하시면 오후 3시까지 주문해 주십시오."),
    "provide": ("The hotel will provide fresh towels upon request.", "호텔은 요청 시 새 수건을 제공할 것입니다."),
    "contact": ("Please contact customer support if you need further assistance.", "추가 도움이 필요하시면 고객 지원팀에 연락하십시오."),
    "invoice": ("We will send you an invoice as soon as the items are shipped.", "물품이 배송되는 대로 저희가 송장을 보내드리겠습니다."),
    "move": ("The company plans to move its headquarters to a new city.", "회사는 본사를 새 도시로 이전할 계획입니다."),
    "supply": ("Water supply is limited during the dry season.", "건기 동안에는 물 공급이 제한됩니다."),
    "discount": ("Employees receive a 20% discount on all store items.", "직원들은 매장의 모든 물품에 대해 20% 할인을 받습니다."),
    "distribute": ("The charity will distribute blankets to the homeless.", "자선 단체는 집 없는 사람들에게 담요를 배포할 것입니다."),
    "acquisition": ("The recent acquisition of a smaller firm expanded our market share.", "최근 소규모 기업의 인수가 우리의 시장 점유율을 넓혔습니다."),
    "assure": ("I assure you that your personal information is safe with us.", "귀하의 개인 정보는 저희가 안전하게 보관하고 있음을 보장합니다."),
    "subject": ("Prices are subject to change without prior notice.", "가격은 사전 통지 없이 변경될 수 있습니다."),
    "seek": ("The company is actively seeking new investors.", "그 회사는 적극적으로 새로운 투자자를 찾고 있습니다."),
    "satisfactory": ("The manager found the team's performance strictly satisfactory.", "관리자는 팀의 실적이 전적으로 만족스럽다고 생각했습니다."),
    "confirmation": ("You will receive an email confirmation of your booking.", "당신은 예약에 대한 이메일 확인을 받게 될 것입니다."),
    "unable": ("We are unable to process your request at this time.", "지금은 귀하의 요청을 처리할 수 없습니다."),
    "payment": ("Full payment is required before the delivery of goods.", "상품 배송 전에 전액 결제가 필요합니다."),
    "measure": ("We must measure the dimensions of the room before buying furniture.", "우리는 가구를 사기 전에 방의 치수를 측정해야 합니다."),
    "bargain": ("At $50, this high-quality jacket is an absolute bargain.", "50달러면 이 고품질 재킷은 완전한 특가품입니다."),
    "stock": ("This item is currently out of stock.", "이 상품은 현재 재고가 없습니다."),
    "affordability": ("The affordability of housing is a major concern for young people.", "주택의 감당할 수 있는 가격은 젊은이들에게 주요 관심사입니다."),
    "clientele": ("The restaurant has a highly loyal clientele.", "그 식당은 매우 충성도 높은 단골 고객들을 보유하고 있습니다."),
    "acclaim": ("The director's new movie received critical acclaim worldwide.", "그 감독의 새 영화는 전 세계적으로 비평가들의 호평을 받았습니다."),
    "represent": ("Our lawyers will represent us in the court hearing.", "우리 변호사들이 법정 청문회에서 우리를 대표할 것입니다."),
    "rating": ("The TV show maintained a high rating throughout its first season.", "그 TV 쇼는 첫 시즌 내내 높은 시청률을 유지했습니다."),
    "encompass": ("The festival will encompass a wide range of musical genres.", "그 축제는 다양한 음악 장르를 포함할 것입니다."),
    "finalize": ("We need to finalize the contract details by tomorrow.", "우리는 내일까지 계약 세부 사항을 마무리해야 합니다."),
    "market": ("There is a growing market for electric vehicles.", "전기 자동차에 대한 시장이 커지고 있습니다."),
    "retail": ("The store manager has over 10 years of experience in retail.", "매장 매니저는 소매업에서 10년 이상의 경험이 있습니다."),
    "commodity": ("Gold is considered a valuable commodity.", "금은 가치 있는 상품으로 간주됩니다."),
    "quote": ("The contractor gave us a quote for the kitchen renovation.", "계약업체가 부엌 개조에 대한 견적을 우리에게 주었습니다."),
    "consignment": ("The store sells second-hand designer clothes on consignment.", "그 가게는 중고 디자이너 옷을 위탁 판매합니다."),
}

day17_examples = {
    "fragile": ("Please handle this package with care, as it contains fragile items.", "이 소포에는 부서지기 쉬운 물건이 들어있으므로 조심해서 다뤄주세요."),
    "perishable": ("Dairy products are highly perishable and must be refrigerated.", "유제품은 매우 부패하기 쉬우므로 반드시 냉장 보관해야 합니다."),
    "deliver": ("The courier will deliver the package to your office by noon.", "배달원이 정오까지 당신의 사무실로 소포를 배달할 것입니다."),
    "ensure": ("We use strict quality control to ensure our products are safe.", "우리는 우리 제품이 안전하다는 것을 보장하기 위해 엄격한 품질 관리를 사용합니다."),
    "courier": ("Important documents should be sent via a reliable courier service.", "중요한 문서는 신뢰할 수 있는 택배 서비스를 통해 발송되어야 합니다."),
    "carton": ("He bought a large carton of milk from the grocery store.", "그는 식료품점에서 큰 우유 판지 상자를 샀습니다."),
    "address": ("Please make sure you have typed the correct shipping address.", "올바른 배송지 주소를 입력했는지 확인해 주세요."),
    "shipment": ("The first shipment of our new winter coats arrives today.", "우리의 새 겨울 코트 첫 선적이 오늘 도착합니다."),
    "particularly": ("The traffic is particularly bad on Monday mornings.", "월요일 아침에는 교통이 특히 혼잡합니다."),
    "adequately": ("Make sure the items are adequately protected with bubble wrap.", "물품들이 뽁뽁이로 적절히 보호되어 있는지 확인하십시오."),
    "article": ("I read an interesting article about climate change today.", "나는 오늘 기후 변화에 대한 흥미로운 기사를 읽었습니다."),
    "efficient": ("Our new filing system is much more efficient than the old one.", "우리의 새로운 파일 정리 시스템은 예전 것보다 훨씬 효율적입니다."),
    "agency": ("The travel agency helped us book our flights and hotels.", "여행 대행사가 우리의 항공편과 호텔 예약을 도와주었습니다."),
    "enclose": ("Please enclose a copy of your ID with the application form.", "지원서와 함께 신분증 사본을 동봉해 주십시오."),
    "careful": ("You must be careful when carrying those hot coffees.", "그 뜨거운 커피들을 나를 때 조심해야 합니다."),
    "pick up": ("I need to go to the post office to pick up a package.", "소포를 찾으러 우체국에 가야 합니다."),
    "carry": ("The airline allows passengers to carry one small bag on board.", "항공사는 승객들이 비행기에 작은 가방 하나를 가지고 타는 것을 허용합니다."),
    "attach": ("Don't forget to attach your resume to the email before sending it.", "이메일을 보내기 전에 이력서를 첨부하는 것을 잊지 마세요."),
    "formerly": ("The building was formerly used as a bank.", "그 건물은 이전에 은행으로 사용되었습니다."),
    "package": ("Your package will be delivered within three business days.", "귀하의 소포는 영업일 기준 3일 이내에 배달될 것입니다."),
    "react": ("The stock market tends to react strongly to political news.", "주식 시장은 정치 뉴스에 강하게 반응하는 경향이 있습니다."),
    "content": ("We are checking the content of the boxes before shipping them.", "우리는 상자들을 배송하기 전에 내용물을 확인하고 있습니다."),
    "convenience": ("Our store is open 24 hours a day for your convenience.", "저희 매장은 고객의 편의를 위해 하루 24시간 문을 엽니다."),
    "acknowledge": ("Please acknowledge receipt of this letter by signing below.", "아래에 서명하여 이 편지의 수령을 인정해 주십시오."),
    "caution": ("Drivers should proceed with extreme caution in heavy fog.", "운전자들은 짙은 안개 속에서 극도의 주의를 기울여 진행해야 합니다."),
    "correspondence": ("All business correspondence should be polite and professional.", "모든 비즈니스 통신문은 예의 바르고 전문적이어야 합니다."),
    "separate": ("We need to separate the recyclable materials from the garbage.", "우리는 쓰레기에서 재활용 가능한 재료들을 분리해야 합니다."),
    "remarkable": ("The team achieved a remarkable victory against the defending champions.", "팀은 디펜딩 챔피언을 상대로 놀라운 승리를 거두었습니다."),
    "handle": ("Only authorized personnel are allowed to handle the hazardous chemicals.", "허가된 인원만이 유해 화학물질을 다루도록 허용됩니다."),
    "warehouse": ("The goods are currently stored in a warehouse outside the city.", "그 상품들은 현재 도시 외곽의 창고에 보관되어 있습니다."),
    "impose": ("The government decided to impose an extra tax on luxury items.", "정부는 사치품에 추가 세금을 부과하기로 결정했습니다."),
    "storage": ("We rented a unit for the storage of our extra furniture.", "우리는 남는 가구의 보관을 위해 창고 하나를 빌렸습니다."),
    "detach": ("Please detach the bottom portion of the form and return it to us.", "양식의 아랫부분을 분리하여 저희에게 돌려주십시오."),
    "envelope": ("Put the sealed envelope in the mail before 5 PM.", "오후 5시 전에 봉인된 봉투를 우편으로 보내십시오."),
    "exclusion": ("The policy guarantees full coverage with the exclusion of deliberate damage.", "그 정책은 고의적 손상의 제외를 조건으로 전면 보장을 보장합니다."),
    "recipient": ("The recipient must present a valid ID to claim the package.", "수령인은 소포를 찾기 위해 유효한 신분증을 제시해야 합니다."),
    "affix": ("Please affix a postage stamp to the upper right corner of the envelope.", "봉투의 오른쪽 위 모서리에 우표를 붙여 주십시오."),
    "incorrect": ("If the shipping address is incorrect, your delivery will be delayed.", "배송 주소가 부정확하면 귀하의 배달이 지연될 것입니다."),
    "oblige": ("I would be much obliged if you could help me with this project.", "이 프로젝트를 도와주신다면 대단히 감사하겠습니다."),
    "step": ("Taking a deep breath is the first step to calming down.", "심호흡을 하는 것은 진정하기 위한 첫 번째 단계입니다."),
}

day18_examples = {
    "check in": ("We need to check in at the hotel by 3 PM.", "우리는 오후 3시까지 호텔에 체크인해야 합니다."),
    "compensate": ("The airline will compensate passengers for the delayed flight.", "항공사는 지연된 항공편에 대해 승객들에게 보상할 것입니다."),
    "complimentary": ("Guests receive a complimentary breakfast every morning.", "투숙객들은 매일 아침 무료 아침 식사를 제공받습니다."),
    "chef": ("The head chef created a special menu for the holiday.", "수석 주방장은 명절을 위한 특별 메뉴를 만들었습니다."),
    "container": ("Please transfer the leftover food into a plastic container.", "남은 음식은 플라스틱 용기에 옮겨 담으십시오."),
    "elegant": ("The couple dined at an elegant restaurant to celebrate their anniversary.", "부부는 기념일을 축하하기 위해 우아한 식당에서 식사했습니다."),
    "flavor": ("This ice cream uses real strawberries for artificial flavor.", "이 아이스크림은 인공 향료 대신 진짜 딸기를 사용합니다."),
    "accommodate": ("The newly built hotel can accommodate up to 500 guests.", "새로 지은 호텔은 최대 500명의 손님을 수용할 수 있습니다."),
    "available": ("There are currently no rooms available for this weekend.", "이번 주말에는 현재 이용할 수 있는 객실이 없습니다."),
    "reception": ("The wedding reception will be held in the grand ballroom.", "결혼 피로연은 대연회장에서 열릴 것입니다."),
    "in advance": ("It is highly recommended to book your tickets in advance.", "티켓을 사전에 예약하는 것이 강력히 권장됩니다."),
    "refreshments": ("Light refreshments will be served during the intermission.", "휴식 시간 동안 가벼운 다과가 제공될 것입니다."),
    "make": ("I would like to make a reservation for two people at 7 PM.", "저녁 7시에 두 명 예약을 하고 싶습니다."),
    "cater": ("The local business will cater the food for our company picnic.", "지역 업체가 우리 회사 야유회를 위해 음식을 공급할 것입니다."),
    "reservation": ("I called the hotel to confirm my reservation for next week.", "나는 다음 주 나의 예약을 확인하기 위해 호텔에 전화했습니다."),
    "beverage": ("Alcoholic beverages are not served to anyone under the age of 21.", "알코올성 음료는 21세 미만에게 제공되지 않습니다."),
    "confirm": ("Please confirm your attendance by Friday.", "금요일까지 참석 여부를 확인해 주십시오."),
    "cancel": ("She had to cancel her hair appointment due to an unexpected meeting.", "그녀는 예상치 못한 회의 때문에 미용실 예약을 취소해야 했습니다."),
    "rate": ("The hotel offers a discounted rate for corporate clients.", "호텔은 기업 고객들에게 할인된 요금을 제공합니다."),
    "conviniently": ("The hotel is conveniently located near the subway station.", "그 호텔은 지하철역 근처에 편리하게 위치해 있습니다."),
    "decorate": ("They will decorate the room with balloons and flowers for the party.", "그들은 파티를 위해 방을 풍선과 꽃으로 장식할 것입니다."),
    "information": ("For more information, please visit our official website.", "더 많은 정보를 원하시면 저희 공식 웹사이트를 방문해 주십시오."),
    "retain": ("Please retain your receipt as proof of purchase.", "구매 증명으로 영수증을 보관해 주십시오."),
    "atmosphere": ("The cafe has a cozy and relaxing atmosphere.", "이 카페는 아늑하고 편안한 분위기를 가지고 있습니다."),
    "cuisine": ("The restaurant specializes in authentic Italian cuisine.", "그 식당은 정통 이탈리아 요리를 전문으로 합니다."),
    "sequence": ("He explained the events in chronological sequence.", "그는 사건들을 시간적 순서로 설명했습니다."),
    "extensive": ("The library has an extensive collection of historical documents.", "그 도서관은 역사 문서의 광범위한 모음을 가지고 있습니다."),
    "prior": ("Prior experience is required for this management position.", "이 관리직에는 이전의 경험이 요구됩니다."),
    "book": ("I managed to book a flight to London at a great price.", "나는 운 좋게 런던행 비행기를 저렴한 가격에 예약했습니다."),
    "amenity": ("The luxury apartment complex offers a pool and a gym as an amenity.", "그 고급 아파트 단지는 수영장과 체육관을 편의 시설로 제공합니다."),
    "belongings": ("Please ensure you have all your personal belongings before leaving the train.", "기차에서 내리기 전에 모든 개인 소지품을 챙겼는지 확인해 주십시오."),
    "entirely": ("The success of the project is entirely due to the team's hard work.", "프로젝트의 성공은 전적으로 팀의 노고 덕분입니다."),
    "ease": ("Modern technology allows us to communicate with ease globally.", "현대 기술은 우리가 전 세계적으로 쉽게 소통할 수 있게 해줍니다."),
    "ingredient": ("Fresh basil is a key ingredient in authentic pesto sauce.", "신선한 바질은 정통 페스토 소스의 주요 재료입니다."),
    "sip": ("He took a slow sip of his hot coffee.", "그는 그의 뜨거운 커피를 천천히 한 모금 마셨습니다."),
    "stir": ("Stir the soup constantly to prevent it from burning.", "수프가 타는 것을 막기 위해 계속 저어 주세요."),
    "choice": ("The menu offers a wide choice of vegetarian dishes.", "이 메뉴는 매우 다양한 채식 요리의 선택을 제공합니다."),
    "complication": ("The surgery was successful and without any serious complication.", "수술은 성공적이었고 어떤 심각한 복잡한 문제도 없었습니다."),
    "freshness": ("We guarantee the freshness of all our organic vegetables.", "우리는 모든 유기농 채소의 신선함을 보장합니다."),
    "occupancy": ("The hotel reached 100% occupancy during the festival week.", "호텔은 축제 주간 동안 100%의 이용률(객실 사용률)에 도달했습니다."),
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
add_examples_to_day(filepath, 'day16', day16_examples)
add_examples_to_day(filepath, 'day17', day17_examples)
add_examples_to_day(filepath, 'day18', day18_examples)
