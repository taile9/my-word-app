import sys

def fix_day1():
    filepath = 'public/data2.csv'
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        parts = line.strip().split('\t')
        
        # Format corrections for bad examples and insertion of missing words
        if len(parts) >= 3 and parts[1] == 'apprehensive':
            new_lines.append(line)
            new_lines.append('\tMany employees are apprehensive about the changes.\t많은 직원들이 변화에 대해 우려하고 있습니다.\n')
        elif len(parts) >= 3 and 'apprehensive' in parts[1] and 'changes' in parts[1]:
            pass # Skip bad format line
        elif len(parts) >= 3 and parts[1] == 'entitle':
            new_lines.append(line)
            new_lines.append('\tAll members are entitled to a 10% discount.\t모든 회원은 10% 할인을 받을 권리가 있습니다.\n')
        elif len(parts) >= 3 and 'entitled' in parts[1]:
            pass # Skip bad format line
        elif len(parts) >= 3 and parts[1] == 'payroll':
            new_lines.append(line)
            new_lines.append('\tThe company has over 500 employees on its payroll.\t그 회사는 급여 명부에 500명이 넘는 직원을 두고 있습니다.\n')
        elif len(parts) >= 3 and 'payroll' in parts[1] and 'company' in parts[1]:
            pass # Skip bad format line
        elif len(parts) >= 3 and parts[1] == 'certification':
            new_lines.append(line)
            new_lines.append('\tProfessional certification can help your career.\t전문 자격증은 당신의 경력에 도움이 될 수 있습니다.\n')
        elif len(parts) >= 3 and 'certification' in parts[1] and 'career' in parts[1]:
            pass # Skip bad format line
        elif len(parts) >= 3 and parts[1] == 'wage':
            # Insert the 4 missing words before "wage"
            new_lines.append('day1\tconsultant\t고문, 컨설턴트\n')
            new_lines.append('\tThe company hired a security consultant to review its systems.\t회사는 시스템을 검토하기 위해 보안 컨설턴트를 고용했습니다.\n')
            new_lines.append('day1\tdegree\t학위\n')
            new_lines.append('\tA master\'s degree is required for this senior position.\t이 고위 직책에는 석사 학위가 필요합니다.\n')
            new_lines.append('day1\trecruit\t(신입사원등을)모집하다\n')
            new_lines.append('\tWe plan to recruit 50 new engineers this year.\t우리는 올해 50명의 새 엔지니어를 모집할 계획입니다.\n')
            new_lines.append('day1\toccupation\t직업\n')
            new_lines.append('\tPlease state your name, age, and occupation on the form.\t양식에 이름, 나이, 직업을 기재해 주세요.\n')
            # Add "wage" and its correct example
            new_lines.append(line)
            new_lines.append('\tThe minimum wage will increase next year.\t최저 임금이 내년에 인상될 예정입니다.\n')
        elif len(parts) >= 3 and 'wage' in parts[1] and 'minimum' in parts[1]:
            pass # Skip the badly formatted day2 wage example
        else:
            new_lines.append(line)
        i += 1

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Fixed day1 formatting and inserted 4 missing words")

if __name__ == '__main__':
    fix_day1()
