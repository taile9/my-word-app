import sys

day26_examples = {
    "delinquent": ("The bank sent a notice about the delinquent account.", "은행은 연체된 계좌에 대한 통지서를 보냈습니다."),
    "overdue": ("Your payment is now three weeks overdue.", "귀하의 결제가 이제 3주 연체되었습니다."),
    "regrettably": ("Regrettably, we must announce the closure of our local branch.", "유감스럽게도, 저희는 지역 지점의 폐쇄를 발표해야 합니다."),
    "balance": ("Please check your account balance regularly.", "잔고를 정기적으로 확인해 주십시오."),
    "deposit": ("I need to go to the bank to deposit this check.", "이 수표를 입금하러 은행에 가야 합니다."),
    "investigation": ("The police conducted a thorough investigation of the crime scene.", "경찰은 범죄 현장에 대한 철저한 조사를 수행했습니다."),
    "account": ("She opened a new savings account last week.", "그녀는 지난주에 새 저축 계좌를 열었습니다."),
    "statement": ("The bank sends a monthly statement of all transactions.", "은행은 모든 거래의 월별 명세서를 보냅니다."),
    "amount": ("The total amount due is written at the bottom of the bill.", "지불해야 할 총액은 청구서 하단에 적혀 있습니다."),
    "withdrawal": ("There is a daily limit for cash withdrawal from the ATM.", "현금자동입출금기에서 현금을 인출하는 데는 일일 한도가 있습니다."),
    "previously": ("He previously worked as an accountant for five years.", "그는 이전에 5년 동안 회계사로 일했습니다."),
    "due": ("The report is due by the end of the day.", "그 보고서는 오늘 끝까지 마감되어야 합니다."),
    "receive": ("You will receive a confirmation email shortly.", "당신은 곧 확인 이메일을 받게 될 것입니다."),
    "expect": ("We expect the new equipment to arrive tomorrow.", "우리는 새 장비가 내일 도착할 것으로 기대합니다."),
    "certificate": ("She received a certificate for completing the training program.", "그녀는 교육 프로그램을 마친 것에 대한 증명서를 받았습니다."),
    "document": ("Please sign this document at the bottom.", "이 문서의 밑부분에 서명해 주십시오."),
    "spending": ("The government plans to reduce public spending this year.", "정부는 올해 공공 지출을 줄일 계획입니다."),
    "successfully": ("They successfully completed the ambitious project on time.", "그들은 기한 내에 성공적으로 야심 찬 프로젝트를 완료했습니다."),
    "bill": ("I need to pay the electricity bill before Friday.", "나는 금요일 전에 전기 요금을 내야 합니다."),
    "pleasure": ("It is my pleasure to introduce our guest speaker tonight.", "오늘 밤 우리의 초청 연사를 소개하게 되어 기쁩니다."),
    "study": ("A recent study shows that more people are working from home.", "최근의 한 연구는 더 많은 사람들이 집에서 일하고 있다는 것을 보여줍니다."),
    "summary": ("Here is a brief summary of what we discussed today.", "여기에 우리가 오늘 논의한 내용에 대한 간략한 요약이 있습니다."),
    "temporary": ("This is only a temporary solution to the problem.", "이것은 그 문제에 대한 일시적인 해결책일 뿐입니다."),
    "lower": ("The store decided to lower its prices to attract more customers.", "그 가게는 더 많은 고객을 유치하기 위해 가격을 낮추기로 결정했습니다."),
    "transaction": ("The online bank transaction took only a few seconds.", "온라인 은행 거래는 불과 몇 초밖에 걸리지 않았습니다."),
    "double": ("The company expects to double its profits next year.", "그 회사는 내년에 이익이 두 배가 될 것으로 기대합니다."),
    "identification": ("Please bring a valid form of identification to the exam.", "시험에 유효한 형태의 신분증을 가져오십시오."),
    "dissatisfaction": ("Customer dissatisfaction can lead to a loss of business.", "고객의 불만은 사업의 손실로 이어질 수 있습니다."),
    "in common": ("The two brothers have very little in common.", "두 형제는 공통점이 거의 없습니다."),
    "interest": ("The bank charges a high interest rate on its loans.", "은행은 대출에 높은 이자율을 부과합니다."),
    "reject": ("The committee will reject any proposals that fail to meet the criteria.", "위원회는 기준을 충족하지 못하는 어떠한 제안도 거절할 것입니다."),
    "relation": ("There is a close relation between diet and health.", "식단과 건강 사이에는 밀접한 관련이 있습니다."),
    "tentatively": ("The meeting has been tentatively scheduled for next Monday.", "회의는 다음 주 월요일로 임시로 예정되어 있습니다."),
    "alternatively": ("You can pay in cash; alternatively, you can use a credit card.", "당신은 현금으로 지불할 수 있습니다; 그렇지 않으면 신용카드를 사용할 수도 있습니다."),
    "attentive": ("The hotel staff is very attentive to the needs of the guests.", "그 호텔 직원은 손님들의 필요에 매우 주의를 기울입니다."),
    "convert": ("They plan to convert the old warehouse into modern apartments.", "그들은 오래된 창고를 현대적인 아파트로 개조할 계획입니다."),
    "heavily": ("The region relies heavily on agricultural exports.", "그 지역은 농산물 수출에 크게 의존합니다."),
    "loan": ("He took out a bank loan to start his new business.", "그는 새 사업을 시작하기 위해 은행 대출을 받았습니다."),
    "unexpected": ("The sudden storm caused unexpected delays at the airport.", "갑작스러운 폭풍이 공항에서 예상치 못한 지연을 발생시켰습니다."),
    "cash": ("We will offer a discount for cash payments.", "우리는 현금 결제에 대해 할인을 제공할 것입니다."),
    "mortgage": ("They are struggling to pay off their monthly mortgage.", "그들은 매월 주택 융자를 갚느라 고군분투하고 있습니다."),
    "payable": ("The invoice is payable within 30 days of the issue date.", "그 송장은 발행일로부터 30일 이내에 지불 가능합니다."),
    "personal": ("Please keep your personal belongings with you at all times.", "항상 귀하의 개인 소지품을 소지하고 계십시오."),
}

day27_examples = {
    "investment": ("Buying this property was a very sound investment.", "이 부동산을 사는 것은 매우 건실한 투자였습니다."),
    "incrative": ("The new contract proved to be a highly lucrative deal.", "그 새 계약은 매우 수익성 있는 거래로 판명되었습니다."),
    "inherently": ("There is an inherently risky nature to stock market trading.", "주식 시장 거래에는 본질적으로 위험한 특성이 있습니다."),
    "secure": ("We need to secure our computer network against hackers.", "우리는 컴퓨터 네트워크를 해커들로부터 안전하게 지켜야 합니다."),
    "foreseeable": ("In the foreseeable future, electric cars will replace gas vehicles.", "가까운/예견할 수 있는 미래에 전기 자동차가 가솔린 차량을 대체할 것입니다."),
    "innate": ("He has an innate talent for playing the piano.", "그는 피아노 연주에 천부적인(타고난) 재능이 있습니다."),
    "property": ("The value of this property has doubled in five years.", "이 재산(부동산)의 가치는 5년 만에 두 배가 되었습니다."),
    "on behalf of": ("I am speaking today on behalf of all the employees.", "나는 오늘 모든 직원들을 대신하여 말씀드립니다."),
    "lease": ("We signed a two-year lease for the new office space.", "우리는 새 사무실 공간에 대해 2년 임대 계약에 서명했습니다."),
    "sponsor": ("A local bank agreed to sponsor the city marathon.", "지역 은행이 도시 마라톤을 후원하기로 동의했습니다."),
    "propose": ("I would like to propose a new strategy to increase sales.", "나는 판매를 증가시키기 위한 새로운 전략을 제안하고 싶습니다."),
    "support": ("We need the full support of the community to succeed.", "우리는 성공하기 위해 지역 사회의 완전한 지지가 필요합니다."),
    "distributuion": ("The distribution of wealth is a major political issue.", "부의 분배는 주요한 정치적 문제입니다."),
    "consider": ("Please consider all the options before making a final decision.", "최종 결정을 내리기 전에 모든 선택 사항을 고려해 주십시오."),
    "nearly": ("It is nearly impossible to finish this project without help.", "이 프로젝트를 도움 없이 끝내는 것은 거의 불가능합니다."),
    "consent": ("You must obtain written consent from your parents to participate.", "당신은 참여하기 위해 부모님으로부터 서면 동의를 얻어야 합니다."),
    "gratitude": ("We would like to express our deep gratitude for your support.", "귀하의 지지에 대해 깊은 감사를 표하고 싶습니다."),
    "consult": ("If the pain continues, please consult your doctor immediately.", "통증이 계속되면 즉시 의사와 상의하십시오."),
    "advice": ("Can you give me some advice on how to start a business?", "사업을 시작하는 방법에 대해 내게 조언을 좀 해줄 수 있나요?"),
    "partially": ("The road was partially blocked by a fallen tree.", "그 도로는 쓰러진 나무에 의해 부분적으로 막혔습니다."),
    "evident": ("It is highly evident that the current system is not working.", "현재의 시스템이 작동하지 않는다는 것이 명백합니다."),
    "reliability": ("The reliability of this information is very questionable.", "이 정보의 신뢰성은 매우 의문스럽습니다."),
    "cautious": ("Be cautious when driving on icy roads.", "얼어붙은 도로에서 운전할 때 조심하십시오."),
    "insight": ("The book provides valuable insight into ancient history.", "그 책은 고대 역사에 대한 귀중한 통찰력을 제공합니다."),
    "portfolio": ("The artist presented her portfolio to the gallery owner.", "예술가는 갤러리 주인에게 그녀의 포트폴리오를 제출했습니다."),
    "possible": ("We will try to resolve the issue as quickly as possible.", "우리는 가능한 한 빨리 그 문제를 해결하려고 노력할 것입니다."),
    "speculation": ("There is widespread speculation that the CEO will resign tomorrow.", "내일 CEO가 사임할 것이라는 널리 퍼진 추측이 있습니다."),
    "solely": ("He was held solely responsible for the accident.", "그는 홀로/전적으로 그 사고에 대한 책임이 있다고 여겨졌습니다."),
    "entrepreneur": ("A successful entrepreneur must be willing to take risks.", "성공적인 사업가는 기꺼이 위험을 감수해야 합니다."),
    "eventually": ("She will eventually realize that she made a mistake.", "그녀는 결국 자신이 실수를 했다는 것을 깨달을 것입니다."),
    "shareholder": ("Every shareholder is invited to the annual meeting next month.", "모든 주주들은 다음 달 연례 회의에 초대됩니다."),
    "outlook": ("The economic outlook for the next quarter is very positive.", "다음 분기에 대한 경제 전망은 매우 긍정적입니다."),
    "stability": ("Political stability is essential for a country's economic growth.", "정치적 안정성은 국가의 경제 성장을 위해 필수적입니다."),
    "bond": ("The government issued new savings bonds to the public.", "정부는 대중에게 새로운 저축 채권을 발행했습니다."),
    "depreciation": ("Car buyers must consider the rapid depreciation of new vehicles.", "자동차 구매자들은 새 차의 급격한 가치 하락을 고려해야 합니다."),
    "increasing": ("There is an increasing demand for renewable energy sources.", "재생 에너지원에 대한 수요가 증가하고 있습니다."),
    "prevalent": ("The disease is mostly prevalent in tropical regions.", "그 질병은 대체로 열대 지역에서 널리 퍼져 있습니다."),
    "rapid": ("The patient made a remarkably rapid recovery after the operation.", "그 환자는 수술 후 놀라울 정도로 빠른 회복을 보였습니다."),
    "unprecedented": ("The disaster caused damage on an unprecedented scale.", "이 재난은 전례 없는 규모의 피해를 초래했습니다."),
    "yield": ("The old apple trees still yield plenty of fruit every autumn.", "그 오래된 사과나무들은 매년 가을마다 여전히 많은 과일을 산출합니다."),
}

day28_examples = {
    "furnished": ("The apartment comes fully furnished with modern appliances.", "그 아파트는 현대적인 가전제품들이 완비된 채로 나옵니다."),
    "residence": ("The prime minister's official residence is located in the capital.", "총리의 공식 관저는 수도에 위치해 있습니다."),
    "spacious": ("They moved into a spacious new office in the city center.", "그들은 도심의 넓은 새 사무실로 이사했습니다."),
    "drape": ("She used elegant velvet curtains to drape the large windows.", "그녀는 넓은 창문들을 (휘)장식하기 위해 우아한 벨벳 커튼을 사용했습니다."),
    "unoccupied": ("The seat next to me remained unoccupied for the entire flight.", "내 옆자리는 비행 내내 비어 있는 상태로 있었습니다."),
    "renovation": ("The museum is closed for extensive renovation until next year.", "그 박물관은 내년까지 광범위한 보수 공사를 위해 문을 닫습니다."),
    "appropriate": ("Please wear appropriate clothing to the formal dinner.", "공식 만찬에 적합한 의상을 입고 오십시오."),
    "delay": ("Heavy snow caused a two-hour delay for all outgoing flights.", "폭설이 모든 출발 항공편에 두 시간의 지연을 초래했습니다."),
    "community": ("The new park will be a great benefit to the local community.", "새로운 공원은 지역 사회에 큰 이점이 될 것입니다."),
    "construction": ("The construction of the new high school will begin next month.", "새 고등학교의 건설이 다음 달에 시작될 것입니다."),
    "repair": ("The mechanic strongly suggested taking the car in for immediate repair.", "정비사는 즉각적인 수리를 위해 차를 들여올 것을 강력히 제안했습니다."),
    "currently": ("I am currently working on a high-priority project.", "저는 현재 최우선 순위 프로젝트를 작업 중입니다."),
    "regularly": ("You should wash your hands regularly to prevent infection.", "감염을 예방하기 위해 손을 정기적으로 씻어야 합니다."),
    "arrange": ("Can you arrange a meeting with the marketing director for tomorrow?", "내일 마케팅 이사와의 회의를 주선해 주시겠습니까?"),
    "location": ("The new coffee shop has an excellent location near the university.", "새 커피숍은 대학교 근처에 훌륭한 장소를 가지고 있습니다."),
    "restore": ("The city council plans to restore the historic building.", "시의회는 역사적인 건물을 복원할 계획입니다."),
    "presently": ("The manager is presently in a meeting and cannot take your call.", "매니저님은 현재 회의 중이시라 전화를 받으실 수 없습니다."),
    "numerous": ("There are numerous reasons why this strategy will not work.", "이 전략이 효과가 없을 수많은 이유들이 있습니다."),
    "abandon": ("The captain ordered the crew to abandon ship during the storm.", "폭풍우 동안 선장은 승무원들에게 배를 버리고 떠나라고 지시했습니다."),
    "contractor": ("The general contractor hired fifty workers for the building site.", "종합 도급업자는 건설 현장을 위해 50명의 인부를 고용했습니다."),
    "develop": ("Reading regularly helps to develop your vocabulary and imagination.", "정기적으로 읽는 것은 어휘력과 상상력을 발달시키는 데 도움이 됩니다."),
    "maintain": ("It is easier to maintain good health than to recover it.", "건강을 회복하는 것보다 유지하는 것이 더 쉽습니다."),
    "densely": ("Tokyo is one of the most densely populated cities in the world.", "도쿄는 세계에서 가장 빽빽하게 인구가 밀집된 도시 중 하나입니다."),
    "prepare": ("We must adequately prepare for the upcoming inspection.", "우리는 다가오는 점검을 위해 적절히 준비해야 합니다."),
    "finally": ("After three hours of waiting, the train finally arrived.", "기다린 지 세 시간 만에 기차가 마침내 도착했습니다."),
    "district": ("The financial district is unusually quiet on Sundays.", "금융 구역은 일요일에 유난히 조용합니다."),
    "renewal": ("The lease requires an annual renewal to stay valid.", "그 임대차(임대)는 유효하게 유지되려면 매년의 갱신이 필요합니다."),
    "compulsory": ("Wearing a helmet is compulsory for all motorcycle riders.", "모든 오토바이 운전자에게 헬멧 착용은 의무적입니다."),
    "interfere": ("Please do not interfere while they are trying to fix the machine.", "그들이 기계를 고치려 노력하는 동안 방해하지 마십시오."),
    "relocation": ("The company offered to pay for my relocation expenses to New York.", "회사는 저의 뉴욕으로의 이전 비용을 지불하겠다고 제안했습니다."),
    "totally": ("I totally agree with your assessment of the situation.", "저는 그 상황에 대한 당신의 평가에 전적으로 동의합니다."),
    "actually": ("I actually prefer the older version of the software.", "나는 사실 이 소프트웨어의 이전 버전을 더 선호합니다."),
    "architect": ("The famous architect designed an eco-friendly building for the city.", "그 유명한 건축가는 도시를 위해 친환경 건물을 설계했습니다."),
    "enlarge": ("We plan to enlarge the kitchen and add a new dining area.", "우리는 부엌을 확장하고 새로운 식사 공간을 추가할 계획입니다."),
    "install": ("The technician will arrive tomorrow to install the new air conditioner.", "기술자가 내일 새 에어컨을 설치하기 위해 도착할 것입니다."),
    "permanent": ("After the trial period, she was offered a permanent position.", "수습 기간 후에 그녀는 영구적인(정규직) 자리를 제안받았습니다."),
    "suppose": ("I suppose we could finish this task tomorrow if necessary.", "필요하다면 우리가 내일 이 작업을 끝낼 수 있을 거라고 생각합니다."),
    "adjacent": ("We bought the empty lot adjacent to our house.", "우리는 우리 집과 인접한 빈 땅을 샀습니다."),
    "consist": ("The basic breakfast will consist of toast, eggs, and coffee.", "기본 아침 식사는 토스트, 계란, 커피로 구성될 것입니다."),
    "utility": ("The monthly rent includes water and electricity utility bills.", "월세에는 공공시설(수도 및 전기 요금)이 포함되어 있습니다."),
}

day29_examples = {
    "conserve": ("We must conserve water during the dry summer months.", "우리는 건조한 여름철 동안 물을 아껴야(보존해야) 합니다."),
    "chance": ("This is a once-in-a-lifetime chance to travel around the world.", "이것은 전 세계를 여행할 일생에 단 한 번의 기회입니다."),
    "forecast": ("The weather forecast predicts heavy rain for tomorrow afternoon.", "일기예보는 내일 오후에 폭우가 내릴 것이라고 예측합니다."),
    "waste": ("Leaving the lights on all day is a terrible waste of electricity.", "하루 종일 불을 켜두는 것은 끔찍한 쓰레기/낭비입니다."),
    "dispose": ("Please safely dispose of these old batteries in the recycling bin.", "이 오래된 배터리들을 재활용 쓰레기통에 안전하게 처분해 주십시오."),
    "recycling": ("The city's new recycling program has been highly successful.", "시의 새로운 재활용 프로그램은 매우 성공적이었습니다."),
    "clear": ("The sky is clear and there are no clouds today.", "오늘 하늘이 맑고 구름이 없습니다."),
    "damage": ("The hurricane caused extensive damage to the coastal towns.", "허리케인은 해안 마을들에 막대한 피해를 입혔습니다."),
    "significant": ("There has been a significant change in the company's leadership.", "회사의 리더십에 중요한(중대한) 변화가 있었습니다."),
    "solution": ("We are working hard to find a workable solution to this problem.", "우리는 이 문제에 적용할 수 있는 해결책을 찾기 위해 열심히 일하고 있습니다."),
    "occur": ("Most traffic accidents occur during the heavy rain or snow.", "대부분의 교통사고는 폭우나 폭설 동안 발생합니다."),
    "ideal": ("This quiet neighborhood is the ideal place to raise a family.", "이 조용한 동네는 가정을 꾸리기에 이상적인 장소입니다."),
    "preserve": ("The historical society wants to preserve the oldest house in town.", "역사 협회는 마을에서 가장 오래된 집을 보존하기를 원합니다."),
    "aid": ("The charity provided massive medical aid to the earthquake victims.", "자선단체는 지진 피해자들에게 대규모의 의료 원조를 제공했습니다."),
    "excessive": ("Excessive consumption of sugar can lead to serious health issues.", "설탕의 지나친 섭취는 심각한 건강 문제로 이어질 수 있습니다."),
    "intensively": ("The land was farmed intensively for many years.", "그 땅은 수년간 집중적으로 경작되었습니다."),
    "vary": ("The temperature can vary greatly between daytime and nighttime.", "기온은 낮과 밤 사이에 크게 다를(변할) 수 있습니다."),
    "pleasing": ("The new design has a very pleasing aesthetic to the eye.", "새로운 디자인은 눈에 매우 즐거운(유쾌한) 미적 감각을 지녔습니다."),
    "mark": ("Please place a red mark beside the correct answers.", "정답 옆에 빨간색 표시를 해 주십시오."),
    "inaccessible": ("Because of the heavy snow, the mountain road was totally inaccessible.", "폭설 때문에 그 산길은 완전히 접근할 수 없었습니다."),
    "disturb": ("Please do not disturb the animals while they are resting.", "동물들이 쉬고 있을 때 방해하지 마십시오."),
    "pollutant": ("Carbon monoxide is a dangerous air pollutant.", "일산화탄소는 위험한 공기 오염 물질입니다."),
    "emission": ("The new factory will drastically cut its carbon emission level.", "새 공장은 탄소 배출 수준을 대폭 줄일 것입니다."),
    "dense": ("The travelers got lost in the dense forest.", "여행자들은 빽빽한 숲속에서 길을 잃었습니다."),
    "environmental": ("Pollution is one of the most pressing environmental problems.", "오염은 가장 긴급한 환경적 문제들 중 하나입니다."),
    "consistent": ("You must be consistent in your efforts to achieve your goals.", "목표를 달성하기 위한 노력에 있어서 당신은 일관되어야 합니다."),
    "leak": ("The plumber fixed the water leak in the bathroom pipe.", "배관공이 욕실 파이프의 누출점을 고쳤습니다."),
    "organization": ("The international organization seeks to end poverty worldwide.", "그 국제 단체는 전 세계적인 빈곤 종식을 추구합니다."),
    "continually": ("The software is continually updated to improve security.", "보안을 향상시키기 위해 소프트웨어가 계속해서 업데이트됩니다."),
    "contaminate": ("The oil spill could easily contaminate the local water supply.", "기름 유출이 지역 식수 공급을 쉽게 오염시킬 수 있습니다."),
    "disaster": ("The earthquake was the worst natural disaster in the country's history.", "지진은 그 나라 역사상 최악의 자연재해였습니다."),
    "discharge": ("The factory was heavily fined for attempting to discharge toxic waste into the river.", "그 공장은 유독 폐기물을 강에 배출하려 한 것으로 무거운 벌금을 물었습니다."),
    "resource": ("Water is an essential natural resource that must be conserved.", "물은 반드시 보존되어야 하는 필수적인 천연자원입니다."),
    "prominent": ("He is a very prominent member of the city council.", "그는 시의회의 매우 유명한(저명한) 구성원입니다."),
    "deplete": ("Overfishing will severely deplete the ocean's fish population.", "남획은 바다의 물고기 개체수를 심하게 고갈시킬 것입니다."),
    "purify": ("Boiling water is a simple way to purify it before drinking.", "물을 끓이는 것은 마시기 전에 그것을 정화하는 간단한 방법입니다."),
    "endangered": ("The giant panda is one of the world's most endangered animal species.", "자이언트 판다는 세계에서 가장 멸종 위기에 처한 동물 종 중 하나입니다."),
    "extinction": ("Many rare animals are on the verge of total extinction.", "많은 희귀 동물들이 완전한 멸종 위기에 처해 있습니다."),
    "drought": ("The severe drought caused widespread crop failure this year.", "심각한 가뭄이 올해 광범위한 농작물 실패를 초래했습니다."),
    "inflict": ("The typhoon is expected to heavily inflict damage along the coast.", "그 태풍은 해안을 따라 막대한 피해를 입힐(가할) 것으로 예상됩니다."),
    "migration": ("The annual migration of birds is a beautiful natural phenomenon.", "매년 일어나는 새들의 이동은 아름다운 자연 현상입니다."),
    "ecology": ("Studying the local ecology is crucial for preserving the wetlands.", "지역의 생태계를 연구하는 것은 습지 보존을 위해 매우 중요합니다."),
    "habitat": ("Deforestation is destroying the natural habitat of many animals.", "삼림 벌채가 많은 동물의 자연 서식지를 파괴하고 있습니다."),
}

day30_examples = {
    "fatigue": ("Drivers should take a break if they start feeling fatigue.", "운전자들은 피로를 느끼기 시작하면 휴식을 취해야 합니다."),
    "checkup": ("I have a regular physical checkup scheduled for next Monday.", "나는 다음 주 월요일에 정기 건강 진단이 예정되어 있습니다."),
    "symtom": ("A high fever is a common symptom of the flu.", "고열은 독감의 흔한 증상입니다."),
    "physician": ("Please contact your primary physician if the pain persists.", "통증이 지속되면 주치의(내과의사)에게 연락하십시오."),
    "diagnosis": ("The quick diagnosis allowed them to start treatment early.", "빠른 진단 덕분에 그들은 조기에 치료를 시작할 수 있었습니다."),
    "prescribe": ("The doctor will prescribe painkillers for your severe headache.", "의사는 당신의 심한 두통을 위해 진통제를 처방할 것입니다."),
    "recovery": ("We all wish you a speedy recovery from your illness.", "우리 모두는 당신이 병에서 빨리 회복/쾌유하기를 바랍니다."),
    "recognize": ("I didn't recognize her because she had changed so much.", "그녀가 너무 많이 변해서 나는 그녀를 알아보지 못했습니다."),
    "join": ("He decided to join the local health club to stay fit.", "그는 건강을 유지하기 위해 지역 헬스클럽에 가입하기로 결정했습니다."),
    "comprehensive": ("The textbook offers a highly comprehensive overview of world history.", "그 교과서는 세계사에 대한 매우 종합적인 개요를 제공합니다."),
    "participate": ("All students are strongly encouraged to participate in extracurricular activities.", "모든 학생들은 과외 활동에 참여하도록 강력히 권장됩니다."),
    "recommend": ("I strongly recommend this book to anyone interested in science.", "저는 과학에 관심 있는 누구에게나 이 책을 강력히 추천합니다."),
    "necessary": ("A valid passport is strictly necessary for international travel.", "국제 여행을 위해서는 유효한 여권이 반드시 필요합니다."),
    "ability": ("He has the impressive ability to speak five different languages.", "그는 5개의 다른 언어를 구사하는 인상적인 능력을 가지고 있습니다."),
    "operation": ("The doctors performed emergency operation to save the patient's life.", "의사들은 환자의 생명을 구하기 위해 응급 수술을 수행했습니다."),
    "cleanliness": ("Strict cleanliness is required in restaurant kitchens.", "레스토랑 주방에서는 엄격한 청결이 요구됩니다."),
    "duration": ("You must fasten your seatbelt for the entire duration of the flight.", "비행하는 기간(지속기간) 내내 안전벨트를 매야 합니다."),
    "examination": ("The teacher will hand out the final examination papers soon.", "선생님께서 곧 기말고사(검토, 시험) 시험지를 나누어 주실 것입니다."),
    "eliminate": ("We must strive to totally eliminate poverty from our society.", "우리는 우리 사회에서 가난을 완전히 제거하기 위해 노력해야 합니다."),
    "easily": ("She easily passed the driving test on her first attempt.", "그녀는 첫 번째 시도에서 쉽게 운전면허 시험에 합격했습니다."),
    "dental": ("Regular flossing is essential for good dental health.", "규칙적인 치실 사용은 좋은 치과의(치아) 건강을 위해 필수적입니다."),
    "related": ("All the evidence collected was related to the initial crime scene.", "수집된 모든 증거는 초기의 범죄 현장과 관련된 것이었습니다."),
    "transmit": ("Mosquitoes can easily transmit harmful diseases to humans.", "모기는 사람에게 해로운 질병을 쉽게 전염시킬 수 있습니다."),
    "periodically": ("The company effectively reviews its safety policies periodically.", "그 회사는 자사의 안전 정책을 주기적으로 효과적으로 재검토합니다."),
    "reaction": ("His allergic reaction to the bee sting was severe.", "벌에 쏘인 후 그의 알레르기 반응은 심각했습니다."),
    "simple": ("It is a simple recipe that anyone can easily follow.", "이것은 누구나 쉽게 따라 할 수 있는 단순한 조리법입니다."),
    "coverage": ("The insurance policy provides extensive coverage for medical emergencies.", "그 보험 정책은 의료 응급 상황에 대한 광범위한 보상 범위를 제공합니다."),
    "exposure": ("Prolonged exposure to the sun can severely damage your skin.", "햇빛에 장기간 노출(됨)은 피부를 심하게 손상시킬 수 있습니다."),
    "pharmaceutical": ("The pharmaceutical company announced a major breakthrough in cancer research.", "그 제약 회사는 암 연구에서 주요한 돌파구를 발표했습니다."),
    "premium": ("You are required to pay a monthly premium for your health insurance.", "건강 보험을 위해 당신은 매월 보험료를 지불해야 합니다."),
    "relieve": ("This medication will help relieve the pain in your joints.", "이 약은 당신의 관절 통증을 완화시키는 데 도움이 될 것입니다."),
    "combination": ("The safe requires a four-digit combination code to open.", "금고를 열려면 4자리의 결합(비밀번호) 코드가 필요합니다."),
    "conscious": ("Patients remain fully conscious during the minor surgical procedure.", "환자들은 사소한 외과 수술 동안 완전히 의식 있는 상태를 유지합니다."),
    "deprivation": ("Sleep deprivation can heavily impact your daily performance.", "수면 박탈은 일상 업무 수행에 큰 영향을 미칠 수 있습니다."),
    "health": ("Eating vegetables clearly improves both physical and mental health.", "채소를 먹는 것은 분명히 육체적 정신적 건강 모두를 향상시킵니다."),
    "induce": ("The doctor used a soft medication to induce sleep.", "의사는 수면을 유발하기 위해 가벼운 약물을 사용했습니다."),
    "insurance": ("It is illegal to drive a car without valid insurance.", "유효한 보험 없이 차를 운전하는 것은 불법입니다."),
    "nutrition": ("Good nutrition is absolutely essential for a child's healthy growth.", "좋은 영양은 아이의 건강한 성장에 절대적으로 필수적입니다."),
    "prevention": ("Education firmly plays a key role in the prevention of crime.", "교육은 범죄의 예방에 분명히 중요한 역할을 합니다."),
    "susceptible": ("Older adults are generally more susceptible to the winter flu.", "노년층은 일반적으로 겨울 독감에 더 영향받기 쉽습니다/감염되기 쉽습니다."),
}

def add_examples_to_day(filepath, day, examples_dict):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    i = 0
    added_count = 0
    
    # Pre-process examples keys for partial matching (for bad spellings like symtom vs symptom)
    keys = list(examples_dict.keys())
    
    while i < len(lines):
        line = lines[i]
        parts = line.rstrip('\r\n').split('\t')
        
        if len(parts) >= 3 and parts[0] == day:
            word = parts[1].strip()
            # fuzzy matching just in case of typos in data2.csv
            matched_key = None
            for k in keys:
                if k == word or word.startswith(k) or k.startswith(word):
                    matched_key = k
                    break
                    
            if matched_key:
                new_lines.append(line)
                
                # Check if it already has an example
                has_ex = False
                if i + 1 < len(lines):
                    next_line = lines[i + 1]
                    next_parts = next_line.rstrip('\r\n').split('\t')
                    if next_parts[0] == '':
                        # It has an example line
                        new_lines.append(lines[i + 1])
                        has_ex = True
                        i += 2
                        continue
                
                eng, kor = examples_dict[matched_key]
                new_lines.append(f'\t{eng}\t{kor}\n')
                added_count += 1
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
        
        i += 1
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"Added {added_count} examples for {day}")
    return added_count

filepath = 'public/data2.csv'
add_examples_to_day(filepath, 'day26', day26_examples)
add_examples_to_day(filepath, 'day27', day27_examples)
add_examples_to_day(filepath, 'day28', day28_examples)
add_examples_to_day(filepath, 'day29', day29_examples)
add_examples_to_day(filepath, 'day30', day30_examples)
