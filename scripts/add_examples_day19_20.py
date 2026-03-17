import sys

day19_examples = {
    "decline": ("The company saw a sharp decline in sales last quarter.", "그 회사는 지난 분기 판매에서 급격한 감소를 보였습니다."),
    "markedly": ("The weather has become markedly colder this week.", "이번 주에 날씨가 두드러지게 추워졌습니다."),
    "increase": ("The factory plans to increase its production by 20%.", "그 공장은 그들의 생산을 20% 늘릴 계획입니다."),
    "revenue": ("The new tax policy is expected to generate more revenue.", "새로운 세금 정책이 더 많은 수익을 창출할 것으로 예상됩니다."),
    "projection": ("Our financial projection shows a steady growth next year.", "우리의 재무 예상은 내년에 꾸준한 성장을 보여줍니다."),
    "substantial": ("The foundation received a substantial donation from an anonymous benefactor.", "재단은 익명의 후원자로부터 상당한 금액의 기부금을 받았습니다."),
    "anticipate": ("We anticipate a huge turnout for the outdoor concert.", "우리는 야외 콘서트에 엄청난 참석자가 올 것으로 기대합니다."),
    "significantly": ("Profits have increased significantly since the new CEO arrived.", "눈에 띄게 큰 이익이 새로운 CEO 부임 이후 증가했습니다."),
    "estimate": ("It is hard to estimate the total cost of the damages.", "손해의 총비용을 추정하는 것은 어렵습니다."),
    "shift": ("There has been a noticeable shift in public opinion recently.", "최근에 대중 의견에서 눈에 띄는 변화가 있었습니다."),
    "fee": ("You must pay a late fee if you return the book after the due date.", "만기일 이후 책을 반납하면 지각 요금을 내야 합니다."),
    "production": ("The halt in production caused a shortage in the market.", "생산의 중단은 시장에 부족을 야기했습니다."),
    "sale": ("The holiday sale attracted thousands of shoppers.", "연휴 할인은 수천 명의 쇼핑객을 끌어들였습니다."),
    "impressive": ("Her resume features an impressive list of academic achievements.", "그녀의 이력서에는 인상적인 학업 성취 목록이 있습니다."),
    "representative": ("A customer service representative will be with you shortly.", "고객 서비스 대표자가 곧 연결될 것입니다."),
    "recent": ("Recent studies show that dark chocolate has health benefits.", "최근의 연구는 다크 초콜릿이 건강에 이점이 있다는 것을 보여줍니다."),
    "exceed": ("Do not exceed the speed limit on this road.", "이 도로에서는 제한 속도를 초과하지 마십시오."),
    "improvement": ("There has been a vast improvement in his test scores.", "그의 시험 점수에서 큰 향상이 있었습니다."),
    "employer": ("Her previous employer wrote a glowing recommendation letter.", "그녀의 이전 고용주는 극찬하는 추천서를 써주었습니다."),
    "regular": ("Regular exercise is essential for maintaining good health.", "규칙적인 운동은 좋은 건강을 유지하는 데 필수적입니다."),
    "summarize": ("Please summarize the main points of the chapter in one page.", "그 장의 주요 요점들을 한 페이지로 요약해 주십시오."),
    "typically": ("This breed of dog typically weighs around 20 pounds.", "이 품종의 개는 일반적으로 약 20파운드 나갑니다."),
    "whole": ("I stayed up the whole night finishing my project.", "나는 프로젝트를 끝내기 위해 밤 전체를 꼬박 새웠습니다."),
    "growth": ("The government hopes to stimulate economic growth with new policies.", "정부는 새로운 정책들로 경제 성장을 자극하기를 희망합니다."),
    "figure": ("The sales figure for last month was surprisingly high.", "지난달의 판매 수치는 놀라울 정도로 높았습니다."),
    "steady": ("The country's economy requires a steady supply of energy.", "국가의 경제는 꾸준한 에너지 공급을 요구합니다."),
    "frequent": ("The buses run on a frequent schedule during rush hour.", "버스들은 출퇴근 시간 동안 빈번한 일정으로 운행됩니다."),
    "achieve": ("He worked hard to achieve his dream of becoming a pilot.", "그는 조종사가 되겠다는 자신의 꿈을 달성하기 위해 열심히 일했습니다."),
    "assumption": ("Our business plan is built on the assumption that demand will rise.", "우리의 사업 계획은 수요가 오를 것이라는 가정 위에 세워졌습니다."),
    "share": ("They decided to share the cost of the rental equally.", "그들은 대여 비용을 동등하게 나누기로 결정했습니다."),
    "incur": ("If you miss the deadline, you will incur a penalty charge.", "당신이 기한을 놓치면, 당신은 벌금 요금을 초래할 것입니다."),
    "slightly": ("The chair moved slightly when I leaned against it.", "내가 기대었을 때 의자가 약간 움직였습니다."),
    "profit": ("The company reported a record profit for the third quarter.", "이 회사는 3분기에 기록적인 수익을 보고했습니다."),
    "reliant": ("Many modern industries are heavily reliant on computers.", "많은 현대 산업들은 컴퓨터에 크게 의존합니다."),
    "illustrate": ("Let me use an example to illustrate my point clearly.", "나의 요점을 명확하게 설명하기 위해 한 가지 예를 사용하게 해주세요."),
    "inaccurate": ("The weather forecast was terribly inaccurate yesterday.", "날씨 예보는 어제 터무니없이 부정확했습니다."),
    "percentage": ("A high percentage of the students passed the final exam.", "높은 비율의 학생들이 기말고사를 통과했습니다."),
    "reduce": ("You should try to reduce your intake of sugary drinks.", "당신은 단 음료 섭취를 줄이기 위해 노력해야 합니다."),
    "tend": ("People tend to eat more unhealthy food when they are stressed.", "사람들은 그들이 스트레스를 받을 때 건강하지 않은 음식을 먹는 경향이 있습니다."),
}

day20_examples = {
    "audit": ("The government ordered an independent audit of the bank's records.", "정부는 그 은행의 기록들에 대한 독립적인 회계감사를 명령했습니다."),
    "accounting": ("She has a degree in business administration and accounting.", "그녀는 경영학과 회계학 학위를 가지고 있습니다."),
    "budget": ("We need to finish this project strictly within the given budget.", "우리는 철저히 주어진 예산 안에서 이 프로젝트를 완료해야 합니다."),
    "financial": ("The company is currently facing severe financial difficulties.", "이 회사는 현재 심각한 금전상의 어려움에 직면해 있습니다."),
    "curtail": ("The factory had to curtail its production due to a lack of parts.", "공장은 부품 부족 때문에 생산을 삭감해야 했습니다."),
    "deficit": ("The national budget deficit reached a record high this year.", "국가 예산 적자가 올해 사상 최고치에 도달했습니다."),
    "recently": ("I recently moved to a new apartment in the city center.", "나는 최근에 시내 중심에 있는 새 아파트로 이사했습니다."),
    "substantially": ("Housing prices have substantially increased over the last decade.", "주택 가격은 지난 10년 동안 상당히 증가했습니다."),
    "committee": ("The planning committee meets every Tuesday morning.", "기획 위원회는 매주 화요일 아침에 모입니다."),
    "frequently": ("She travels to Japan frequently for business meetings.", "그녀는 사업 회의를 위해 일본으로 자주 여행합니다."),
    "capability": ("The new missile system has a remarkably precise strike capability.", "이 신형 미사일 시스템은 놀랍도록 정밀한 타격 능력을 가지고 있습니다."),
    "proceeds": ("All the proceeds from the concert will go to a local charity.", "콘서트에서 나온 모든 수익금은 지역 자선 단체로 갈 것입니다."),
    "reimburse": ("The company will reimburse your travel expenses next week.", "이 회사는 귀하의 출장비를 다음 주에 변제할 것입니다."),
    "considerably": ("The temperature dropped considerably after sunset.", "기온은 일몰 후에 상당히 떨어졌습니다."),
    "adequate": ("Please make sure you have adequate drinking water for the hike.", "하이킹을 위한 적절한 양의 식수를 가지고 있는지 확인하십시오."),
    "total": ("The total number of attendees exceeded our expectations.", "총 참석자 수가 우리의 예상을 초과했습니다."),
    "allocate": ("The school decided to allocate more funds for the new sports facility.", "학교는 새 스포츠 시설을 위해 더 많은 기금을 할당하기로 결정했습니다."),
    "inspector": ("The health inspector found several violations in the restaurant's kitchen.", "보건 조사관은 그 식당의 주방에서 여러 위반 사항들을 발견했습니다."),
    "preferred": ("Coffee is my preferred drink in the morning.", "아침에 내가 선호하는 음료는 커피입니다."),
    "quarter": ("The company's profits grew in the fourth quarter of the year.", "이 회사의 이익은 그 해의 4분기에 증가했습니다."),
    "interrupt": ("Please do not interrupt me while I am making a presentation.", "내가 프레젠테이션을 하는 동안 방해하지 말아주세요."),
    "browse": ("Feel free to browse our online catalog at your convenience.", "당신이 편할 때 마음껏 자사의 온라인 카탈로그를 훑어보세요."),
    "prompt": ("The firefighters' prompt response saved the building from burning down.", "소방관들의 즉각적인 대응은 건물이 불타는 것을 막았습니다."),
    "deduct": ("The employer will deduct taxes from your monthly paycheck.", "고용주는 귀하의 매월 급여에서 세금을 공제할 것입니다."),
    "measurement": ("The carpenter took a careful measurement of the door frame.", "목수는 문틀에 대해 신중한 측정을 했습니다."),
    "shorten": ("The tailor agreed to shorten the sleeves of my new jacket.", "그 재단사는 내 새 재킷의 소매를 단축하기로 동의했습니다."),
    "amend": ("The city council voted to amend the zoning laws.", "시의회는 도시 계획 구역 지정법을 수정하기로 투표했습니다."),
    "calculate": ("Please use a calculator to accurately calculate the final amount.", "최종 금액을 정확하게 계산하기 위해 계산기를 사용하십시오."),
    "exempt": ("Certain non-profit organizations are exempt from paying property taxes.", "특정 비영리 단체는 재산세 납부가 면제됩니다."),
    "deficient": ("A diet deficient in iron can lead to severe health problems.", "철분이 부족한 식단은 심각한 건강 문제를 초래할 수 있습니다."),
    "compare": ("Consumers often compare prices before buying an expensive item.", "소비자들은 종종 비싼 물건을 사기 전에 가격을 비교합니다."),
    "fortunate": ("We were fortunate to have perfectly clear weather for our outdoor wedding.", "우리의 야외 결혼식을 위해 완벽하게 화창한 날씨를 갖게 되어 다행스러웠습니다."),
    "expenditure": ("The country needs to reduce its military expenditure during peacetime.", "그 국가는 평화 시에 자국의 군사 지출을 줄일 필요가 있습니다."),
    "accurately": ("The watch keeps time very accurately despite being old.", "그 시계는 오래되었음에도 불구하고 시간을 매우 정확하게 지킵니다."),
    "worth": ("This antique vase is worth thousands of dollars.", "이 골동품 꽃병은 수천 달러의 가치가 있습니다."),
    "excess": ("Avoid eating in excess if you want to lose weight.", "당신이 체중을 줄이고 싶다면 초과로 먹는 것을 피하십시오."),
    "fiscal": ("The government announced its new fiscal policy for the upcoming year.", "정부는 다가오는 해에 대한 새로운 재정 정책을 발표했습니다."),
    "incidental": ("Save all receipts for incidental expenses during your business trip.", "출장 중의 부수적인 지출들에 대한 모든 영수증을 보관하십시오."),
    "inflation": ("High inflation reduces the purchasing power of consumers.", "높은 물가상승은 소비자들의 구매력을 감소시킵니다."),
    "liable": ("The driver who caused the accident is liable for the damages.", "그 사고를 야기한 운전자는 손해들에 대해 책임져야 합니다."),
    "spend": ("Many students spend their weekends studying at the library.", "많은 학생들이 주말을 도서관에서 공부하며 보냅니다."),
    "turnover": ("The fast-food restaurant has a very high employee turnover rate.", "그 패스트푸드점은 직원 이직률이 매우 높습니다."),
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
add_examples_to_day(filepath, 'day19', day19_examples)
add_examples_to_day(filepath, 'day20', day20_examples)
