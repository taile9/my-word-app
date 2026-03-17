# snapvoca 프로젝트 지시사항 정리

## 프로젝트 개요
- 앱 이름: **snapvoca**
- 기술 스택: React (Create React App), [public/data2.csv](file:///c:/Users/USER/my-word-app/public/data2.csv) 기반 단어장 앱
- 주요 파일: [src/App.js](file:///c:/Users/USER/my-word-app/src/App.js), [src/App.css](file:///c:/Users/USER/my-word-app/src/App.css), [public/data2.csv](file:///c:/Users/USER/my-word-app/public/data2.csv), [public/index.html](file:///c:/Users/USER/my-word-app/public/index.html), [public/manifest.json](file:///c:/Users/USER/my-word-app/public/manifest.json)

---

## 완료된 작업

### 1. 앱 이름 및 설명 변경
- 이름을 `VocaZip` → `snapvoca` 로 변경
- 변경 위치: [public/index.html](file:///c:/Users/USER/my-word-app/public/index.html) (title, description), [public/manifest.json](file:///c:/Users/USER/my-word-app/public/manifest.json), [src/App.js](file:///c:/Users/USER/my-word-app/src/App.js) (헤더 h1)
- 설명 문구: **"가장 가볍고 빠른 단어 암기. 복잡한 설정 없이 바로 시작하세요."**

### 2. UI 전면 리디자인 + 다크 모드 추가
- [src/App.css](file:///c:/Users/USER/my-word-app/src/App.css): CSS 변수(`:root`, `body.dark-mode`) 기반 라이트/다크 테마 전환
- [src/App.js](file:///c:/Users/USER/my-word-app/src/App.js): `isDarkMode` state 추가, `localStorage` 저장 (앱 재접속 시 기억)
- 다크 모드 토글 버튼: 홈 화면 상단 컨트롤 바에 `🌙 다크 모드 ON/OFF` 버튼 추가
- 디자인 방향: 글래스모피즘, 보라색 포인트 컬러, 부드러운 애니메이션

### 3. UI 세부 조정 (사용자 직접 피드백 반영)
- **글자 줄바꿈(엔터) 금지**: 단어 글자가 카드 너비에 맞게 자동으로 작아지도록 `clamp(2rem, 8cqw, 4rem)` 방식으로 변경 (`cqw` = 컨테이너 너비 기준)
- **스크롤바 제거**: 카드 내부 `overflow-y: auto` 제거, `overflow: hidden` 적용
- **카드 크기 완전 통일**: `card-wrapper` 및 `quiz-panel` 모두 고정 높이 `580px`로 통일
- **예문 글씨 크기**: 사용자가 직접 [App.css](file:///c:/Users/USER/my-word-app/src/App.css)에서 `.ex-eng`, `.ex-kor` 수정 (약 0.9rem, 0.8rem 수준)
- **단어 글자 크기**: 사용자가 직접 `.large-text` 수정 (2rem ~ 4rem)

### 4. 데이터 파싱 수정 (App.js)
- [data2.csv](file:///c:/Users/USER/my-word-app/public/data2.csv)에서 예문이 단어 뜻으로 잘못 들어가던 버그 수정
- 영어 단어가 4개 이상이거나 마침표로 끝나면 '예문'으로 판단하는 로직 추가
- 유의어([( )](file:///c:/Users/USER/my-word-app/src/App.js#61-693) 괄호 안 내용) 분리 로직 복원

---

## 남은 요청 (미완료)

### 5. data2.csv 전체 단어에 예문 추가
- 현재 예문이 없는 단어들이 다수 존재
- 요청: 모든 단어에 영어 예문 + 한국어 번역 추가
- **Day 범위를 지정해서 새 대화에서 요청할 것** (예: "Day 1~5 예문 추가해줘")

---

## 핵심 규칙 (반드시 지켜야 할 사항)
- ❌ 명령을 허락 없이 터미널에서 실행하지 말 것
- ❌ 단어 카드에 스크롤바 만들지 말 것
- ❌ 단어가 긴 경우 줄바꿈(엔터)로 카드 크기를 키우지 말 것 → 글자 크기로 해결
- ✅ 카드 크기는 항상 고정 (580px), 내용이 넘치면 글자를 작게
- ✅ 예문 글씨는 단어보다 훨씬 작게 유지
- ✅ 변경 전 설명 먼저 하고 허락받을 것
