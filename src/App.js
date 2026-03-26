import React, { useState, useEffect, useRef } from 'react';
import './App.css';

// Sound Helper
const playSound = (type) => {
  try {
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    const oscillator = audioContext.createOscillator();
    const gainNode = audioContext.createGain();

    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);

    if (type === 'flip') {
      oscillator.type = 'sine';
      oscillator.frequency.setValueAtTime(400, audioContext.currentTime);
      oscillator.frequency.exponentialRampToValueAtTime(600, audioContext.currentTime + 0.1);
      gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
      gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.1);
      oscillator.start();
      oscillator.stop(audioContext.currentTime + 0.1);
    } else if (type === 'next') {
      oscillator.type = 'triangle';
      oscillator.frequency.setValueAtTime(300, audioContext.currentTime);
      oscillator.frequency.linearRampToValueAtTime(400, audioContext.currentTime + 0.05);
      gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
      gainNode.gain.linearRampToValueAtTime(0.01, audioContext.currentTime + 0.05);
      oscillator.start();
      oscillator.stop(audioContext.currentTime + 0.05);
    } else if (type === 'correct') {
      oscillator.type = 'square';
      oscillator.frequency.setValueAtTime(400, audioContext.currentTime);
      oscillator.frequency.setValueAtTime(600, audioContext.currentTime + 0.1);
      gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
      gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.2);
      oscillator.start();
      oscillator.stop(audioContext.currentTime + 0.2);
    } else if (type === 'wrong') {
      oscillator.type = 'sawtooth';
      oscillator.frequency.setValueAtTime(200, audioContext.currentTime);
      oscillator.frequency.exponentialRampToValueAtTime(100, audioContext.currentTime + 0.2);
      gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
      gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.2);
      oscillator.start();
      oscillator.stop(audioContext.currentTime + 0.2);
    }
  } catch (e) { /* ignore audio error */ }
};

// TTS Helper
const speakText = (text, lang = 'en-US') => {
  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel(); // cancel pending

    // Force the correct voice by selecting a voice that matches the requested language.
    // (Some devices default to a local voice even if utterance.lang is set.)
    const getBestVoice = () => {
      try {
        const voices = window.speechSynthesis.getVoices?.() || [];
        if (!voices.length) return null;

        const langLower = String(lang || '').toLowerCase();
        const base = langLower.split('-')[0];

        // Prefer exact prefix match (e.g., "en-US" -> "en-US", "ko-KR" -> "ko-KR")
        let voice = voices.find(v => String(v.lang || '').toLowerCase().startsWith(langLower));
        if (voice) return voice;

        // Fallback to base language (e.g., "en-US" -> any "en-*" voice)
        voice = voices.find(v => String(v.lang || '').toLowerCase().startsWith(base));
        if (voice) return voice;

        // Last fallback: first voice
        return voices[0] || null;
      } catch {
        return null;
      }
    };

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = lang;
    const chosenVoice = getBestVoice();
    if (chosenVoice) utterance.voice = chosenVoice;
    utterance.rate = 0.9;
    window.speechSynthesis.speak(utterance);
  }
};

function App() {
  const [vocabData, setVocabData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  // App Navigation: 'home', 'learning', 'quiz-menu', 'quiz-active'
  const [appMode, setAppMode] = useState('home');

  // Learning States
  const [selectedGroup, setSelectedGroup] = useState(null); // Day number OR 'favorites'
  const [learningWords, setLearningWords] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);

  // Feature Toggles (with defaults)
  const [soundEnabled, setSoundEnabled] = useState(true);
  const [ttsEnabled, setTtsEnabled] = useState(true);

  // Favorites (Sync with LocalStorage)
  const [favorites, setFavorites] = useState(() => {
    try {
      const saved = localStorage.getItem('vocabAppFavorites');
      return saved ? JSON.parse(saved) : [];
    } catch { return []; }
  });

  // Dark Mode
  const [isDarkMode, setIsDarkMode] = useState(() => {
    try {
      const saved = localStorage.getItem('vocabAppDarkMode');
      return saved ? JSON.parse(saved) : false;
    } catch { return false; }
  });

  // Quiz States
  // quizType: 'all', 'day', 'favorites'
  // format: 'mc-en2ko', 'mc-ko2en', 'tx-en2ko', 'tx-ko2en'
  const [quizConfig, setQuizConfig] = useState({ type: 'all', day: 1, format: 'mc-en2ko' });
  const [quizQueue, setQuizQueue] = useState([]);
  const [options, setOptions] = useState([]);
  const [inputText, setInputText] = useState('');
  const [quizResult, setQuizResult] = useState(null);
  const [wrongWords, setWrongWords] = useState([]);
  const inputRef = useRef(null);

  // 1. Initial Data Fetching
  useEffect(() => {
    fetch('/data2.csv')
      .then(res => {
        if (!res.ok) throw new Error('파일 없음');
        return res.text();
      })
      .then(text => {
        // data2.csv is normalized as:
        // - word line:   dayN \t word \t meaning
        // - example line: \t exEng \t exKor
        const lines = text.replace(/\r/g, '').split('\n');
        const result = [];
        let currentEntry = null;

        const parseSynonymsRaw = (raw) => {
          const s = (raw || '').replace(/"/g, '').trim();
          if (!s) return '';
          // Support common encodings:
          // - literal "\n" sequences
          // - "||" separators
          // - actual newlines (just in case)
          const normalized = s
            .replace(/\\n/g, '\n')
            .replace(/\|\|/g, '\n');
          const lines = normalized.split('\n').map(v => v.trim()).filter(Boolean);

          const out = [];
          for (const ln of lines) {
            // Expect: "eng meaning" (or "eng - meaning", "eng: meaning")
            const m = ln.match(/^([A-Za-z][A-Za-z\s'’-]*[A-Za-z])\s*(?:[-–—:]|\s{2,}|\s+)\s*(.+)$/);
            if (!m) continue;
            const synEng = (m[1] || '').trim();
            const synKor = (m[2] || '').trim();
            if (synEng && synKor) out.push(`${synEng} - ${synKor}`);
          }
          return out.join('\n');
        };

        const finalizeAndPush = (entry) => {
          if (!entry) return;
          // 괄호( ... )는 뜻의 일부일 수 있으므로 그대로 둔다.
          entry.kor = (entry.kor || '').trim();
          entry.synonyms = parseSynonymsRaw(entry.synonyms || '');
          result.push(entry);
        };

        for (const rawLine of lines) {
          const line = rawLine;
          if (!line.trim()) continue;

          const parts = line.split('\t');
          const dayCol = (parts[0] || '').trim();

          if (/^day\s*\d+$/i.test(dayCol)) {
            // new word row
            finalizeAndPush(currentEntry);

            const d = dayCol.replace(/[^0-9]/g, '');
            const e = (parts[1] || '').replace(/"/g, '').trim();
            const k = (parts[2] || '').replace(/"/g, '').trim();
            const syn = (parts[3] || '').trim();

            if (!d || !e || !k) {
              currentEntry = null;
              continue;
            }

            currentEntry = {
              id: `${parseInt(d, 10)}-${e}`,
              day: parseInt(d, 10),
              eng: e,
              kor: k,
              synonyms: syn,
              exEng: '',
              exKor: ''
            };
          } else if (currentEntry && dayCol === '') {
            // example row
            const exEng = (parts[1] || '').replace(/"/g, '').trim();
            const exKor = (parts[2] || '').replace(/"/g, '').trim();
            if (exEng && !currentEntry.exEng) currentEntry.exEng = exEng;
            if (exKor && !currentEntry.exKor) currentEntry.exKor = exKor;
          }
        }

        finalizeAndPush(currentEntry);

        setVocabData(result);
        setIsLoading(false);
      })
      .catch(e => {
        setError(e.message);
        setIsLoading(false);
      });
  }, []);

  // Sync Favorites to LocalStorage
  useEffect(() => {
    localStorage.setItem('vocabAppFavorites', JSON.stringify(favorites));
  }, [favorites]);

  // Sync Dark Mode
  useEffect(() => {
    localStorage.setItem('vocabAppDarkMode', JSON.stringify(isDarkMode));
    if (isDarkMode) {
      document.body.classList.add('dark-mode');
    } else {
      document.body.classList.remove('dark-mode');
    }
  }, [isDarkMode]);

  const toggleFavorite = (wordId, e) => {
    e.stopPropagation(); // prevent card flip
    setFavorites(prev =>
      prev.includes(wordId) ? prev.filter(id => id !== wordId) : [...prev, wordId]
    );
  };

  // Memoized unique days list
  const days = React.useMemo(() => {
    return [...new Set(vocabData.map(d => d.day))].sort((a, b) => a - b);
  }, [vocabData]);


  /* --- LEARNING LOGIC --- */
  const startLearning = (group) => {
    let words = [];
    if (group === 'favorites') {
      words = vocabData.filter(w => favorites.includes(w.id));
    } else {
      words = vocabData.filter(w => w.day === group);
    }

    setSelectedGroup(group);
    setLearningWords(words);
    setCurrentIndex(0);
    setIsFlipped(false);
    setAppMode('learning');

    if (words.length > 0 && ttsEnabled) {
      speakText(words[0].eng, 'en-US');
    }
  };

  const handleLearnNext = () => {
    if (soundEnabled) playSound('next');
    if (currentIndex < learningWords.length - 1) {
      const nextIdx = currentIndex + 1;
      setCurrentIndex(nextIdx);
      setIsFlipped(false);
      if (ttsEnabled) speakText(learningWords[nextIdx].eng, 'en-US');
    }
  };

  const handleLearnPrev = () => {
    if (soundEnabled) playSound('next');
    if (currentIndex > 0) {
      const prevIdx = currentIndex - 1;
      setCurrentIndex(prevIdx);
      setIsFlipped(false);
      if (ttsEnabled) speakText(learningWords[prevIdx].eng, 'en-US');
    }
  };

  const handleLearnFlip = () => {
    if (soundEnabled) playSound('flip');
    const nextFlippedState = !isFlipped;
    setIsFlipped(nextFlippedState);

    // Add TTS for the corresponding side
    if (ttsEnabled && learningWords.length > 0) {
      const currentWord = learningWords[currentIndex];
      if (nextFlippedState) {
        // Flipped to Back -> Read Korean translation
        speakText(currentWord.kor, 'ko-KR');
      } else {
        // Flipped to Front -> Read English word
        speakText(currentWord.eng, 'en-US');
      }
    }
  };


  /* --- QUIZ LOGIC --- */
  const startQuiz = () => {
    let sourceWords = [];
    if (quizConfig.type === 'favorites') {
      sourceWords = vocabData.filter(w => favorites.includes(w.id));
    } else if (quizConfig.type === 'day') {
      sourceWords = vocabData.filter(w => w.day === parseInt(quizConfig.day, 10));
    } else {
      sourceWords = [...vocabData];
    }

    if (sourceWords.length === 0) {
      alert("단어가 없습니다!");
      return;
    }

    // Shuffle the selected words for the quiz queue
    const queue = [...sourceWords].sort(() => Math.random() - 0.5);

    setQuizQueue(queue);
    setCurrentIndex(0);
    setQuizResult(null);
    setInputText('');
    setWrongWords([]);
    setAppMode('quiz-active');
  };

  // Generate Multiple Choice Options
  useEffect(() => {
    if (appMode === 'quiz-active' && quizConfig.format.includes('mc') && quizQueue.length > 0) {
      const currentWord = quizQueue[currentIndex];
      let wrongOptions = [];
      while (wrongOptions.length < 4) {
        const randomWord = vocabData[Math.floor(Math.random() * vocabData.length)];
        const isDuplicate = wrongOptions.some(w => w.eng === randomWord.eng) || randomWord.eng === currentWord.eng;
        if (!isDuplicate) wrongOptions.push(randomWord);
      }
      let combined = [...wrongOptions, currentWord];
      combined.sort(() => Math.random() - 0.5);
      setOptions(combined);

      if (ttsEnabled && quizConfig.format === 'mc-en2ko') {
        speakText(currentWord.eng, 'en-US');
      }
    }
  }, [appMode, currentIndex, quizQueue, quizConfig.format, vocabData, ttsEnabled]);

  // Handle auto-focus for text quiz input
  useEffect(() => {
    if (appMode === 'quiz-active' && quizConfig.format.includes('tx') && inputRef.current) {
      inputRef.current.focus();
      if (ttsEnabled && quizConfig.format === 'tx-en2ko') {
        speakText(quizQueue[currentIndex].eng, 'en-US');
      }
    }
  }, [appMode, currentIndex, quizConfig.format, ttsEnabled, quizQueue]);


  const checkMultipleChoice = (selectedOption) => {
    if (quizResult !== null) return;
    const currentWord = quizQueue[currentIndex];
    if (selectedOption.eng === currentWord.eng) {
      if (soundEnabled) playSound('correct');
      setQuizResult('correct');
    } else {
      if (soundEnabled) playSound('wrong');
      setQuizResult('wrong');
      setWrongWords(prev => prev.some(w => w.id === currentWord.id) ? prev : [...prev, currentWord]);
    }
    // Auto-advance after 1.2s regardless of correct/wrong
    setTimeout(() => { moveToNextQuiz(); }, 1200);
  };

  const checkTextInput = (e) => {
    e.preventDefault();
    if (quizResult !== null) return;

    const currentWord = quizQueue[currentIndex];
    const isEnToKo = quizConfig.format === 'tx-en2ko';
    const targetAnswer = isEnToKo ? currentWord.kor : currentWord.eng;

    const userAns = inputText.trim().toLowerCase();
    const trueAns = targetAnswer.trim().toLowerCase();

    const correct = isEnToKo ? (trueAns.includes(userAns) && userAns.length > 0) : (userAns === trueAns);

    if (correct) {
      if (soundEnabled) playSound('correct');
      setQuizResult('correct');
    } else {
      if (soundEnabled) playSound('wrong');
      setQuizResult('wrong');
      setWrongWords(prev => prev.some(w => w.id === currentWord.id) ? prev : [...prev, currentWord]);
    }
    // Auto-advance after 1.2s regardless of correct/wrong
    setTimeout(() => { moveToNextQuiz(); }, 1200);
  };

  const moveToNextQuiz = () => {
    if (currentIndex < quizQueue.length - 1) {
      setCurrentIndex(currentIndex + 1);
      setQuizResult(null);
      setInputText('');
    } else {
      setAppMode('quiz-result');
    }
  };


  /* --- RENDERERS --- */
  if (error) {
    return (
      <div className="app-container">
        <div className="error-container">
          <h2 style={{ color: '#ef4444', marginTop: 0 }}>⚠️ 오류 발생</h2>
          <p>public 폴더에 <strong>data.csv</strong> 파일이 있는지 확인해주세요.</p>
          <p style={{ color: '#64748b', fontSize: '0.9rem' }}>{error}</p>
        </div>
      </div>
    );
  }

  if (isLoading) {
    return (
      <div className="loading-container">
        <svg className="loading-spinner" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20" />
        </svg>
        <h2>단어장 준비중...</h2>
      </div>
    );
  }

  return (
    <div className={`app-container ${appMode !== 'home' ? 'app-container-wide' : ''}`}>
      <header>
        <h1>snapvoca</h1>

        {appMode === 'home' && (
          <div className="top-controls">
            <button className={`toggle-btn ${soundEnabled ? 'active' : ''}`} onClick={() => setSoundEnabled(!soundEnabled)}>
              {soundEnabled ? '🔊 효과음 ON' : '🔇 효과음 OFF'}
            </button>
            <button className={`toggle-btn ${ttsEnabled ? 'active' : ''}`} onClick={() => setTtsEnabled(!ttsEnabled)}>
              {ttsEnabled ? '🗣️ 발음 ON' : '🙅 발음 OFF'}
            </button>
            <button className={`toggle-btn ${isDarkMode ? 'active' : ''}`} onClick={() => setIsDarkMode(!isDarkMode)}>
              {isDarkMode ? '🌙 다크 모드 ON' : '☀️ 다크 모드 OFF'}
            </button>
          </div>
        )}
      </header>

      {/* 1. HOME SCREEN */}
      {appMode === 'home' && (
        <div className="main-menu">
          <button className="action-btn" onClick={() => setAppMode('quiz-menu')}>
            🎯 단어 시험(퀴즈) 시작하기
          </button>

          <div className="menu-panel">
            <h2>★ 즐겨찾기 학습 ({favorites.length}단어)</h2>
            {favorites.length > 0 ? (
              <button className="action-btn" style={{ background: 'linear-gradient(135deg, #fbbf24, #f59e0b)' }} onClick={() => startLearning('favorites')}>
                즐겨찾기 단어장 열기
              </button>
            ) : (
              <p style={{ textAlign: 'center', color: '#94a3b8', margin: 0 }}>즐겨찾기한 단어가 없습니다.</p>
            )}
          </div>

          <div className="menu-panel">
            <h2>Day별 학습 ({days.length}일)</h2>
            <div className="grid-container">
              {days.map(d => (
                <button key={d} className="day-btn" onClick={() => startLearning(d)}>
                  <span style={{ display: 'block', lineHeight: 1.05 }}>DAY</span>
                  <span style={{ display: 'block', fontWeight: 800, fontSize: '1.1em' }}>
                    {String(d).padStart(2, '0')}
                  </span>
                </button>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* 2. QUIZ MENU */}
      {appMode === 'quiz-menu' && (
        <div className="menu-panel">
          <div className="quiz-header">
            <button className="back-btn" onClick={() => setAppMode('home')}>← 뒤로</button>
            <h2 style={{ margin: 0, color: 'var(--text-main)' }}>퀴즈 설정</h2>
            <div style={{ width: 70 }}></div>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '20px', marginTop: '20px' }}>
            <div>
              <label style={{ display: 'block', marginBottom: '8px', fontWeight: 'bold' }}>1. 시험 범위</label>
              <select className="mode-select" style={{ width: '100%', padding: '12px' }} value={quizConfig.type} onChange={(e) => setQuizConfig({ ...quizConfig, type: e.target.value })}>
                <option value="all">전체 단어</option>
                <option value="day">특정 Day</option>
                <option value="favorites">즐겨찾기 단어</option>
              </select>
            </div>

            {quizConfig.type === 'day' && (
              <div>
                <label style={{ display: 'block', marginBottom: '8px', fontWeight: 'bold' }}>Day 선택</label>
                <select className="mode-select" style={{ width: '100%', padding: '12px' }} value={quizConfig.day} onChange={(e) => setQuizConfig({ ...quizConfig, day: parseInt(e.target.value, 10) })}>
                  {days.map(d => <option key={d} value={d}>Day {d}</option>)}
                </select>
              </div>
            )}

            <div>
              <label style={{ display: 'block', marginBottom: '8px', fontWeight: 'bold' }}>2. 문제 유형</label>
              <select className="mode-select" style={{ width: '100%', padding: '12px' }} value={quizConfig.format} onChange={(e) => setQuizConfig({ ...quizConfig, format: e.target.value })}>
                <option value="mc-en2ko">객관식 (영 ➔ 한)</option>
                <option value="mc-ko2en">객관식 (한 ➔ 영)</option>
                <option value="tx-en2ko">주관식 (영 ➔ 한)</option>
                <option value="tx-ko2en">주관식 (한 ➔ 영)</option>
              </select>
            </div>

            <button className="action-btn" style={{ marginTop: '20px' }} onClick={startQuiz}>시험 시작!</button>
          </div>
        </div>
      )}

      {/* 3. LEARNING MODE */}
      {appMode === 'learning' && (
        <div className="quiz-container">
          <div className="quiz-header">
            <button className="back-btn" onClick={() => setAppMode('home')}>← 종료</button>
            <div className="progress-bar">{selectedGroup === 'favorites' ? '즐겨찾기' : `Day ${selectedGroup}`} ({currentIndex + 1} / {learningWords.length})</div>
          </div>

          {learningWords.length > 0 ? (
            <div className="card-wrapper">
              <div className={`card ${isFlipped ? 'flipped' : ''}`} onClick={handleLearnFlip}>
                <div className="card-content front">
                  <button
                    className={`star-btn ${favorites.includes(learningWords[currentIndex].id) ? 'active' : 'inactive'}`}
                    onClick={(e) => toggleFavorite(learningWords[currentIndex].id, e)}>
                    <svg width="28" height="28" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                  </button>
                  <h3 className="large-text">{learningWords[currentIndex]?.eng || ''}</h3>
                  <div className="click-hint">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M15 3h6v6" /><path d="M9 21H3v-6" /><path d="M21 3l-7 7" /><path d="M3 21l7-7" /></svg>
                    클릭하여 뜻 확인
                  </div>
                </div>
                <div className="card-content back">
                  <button
                    className={`star-btn ${favorites.includes(learningWords[currentIndex].id) ? 'active' : 'inactive'}`}
                    onClick={(e) => toggleFavorite(learningWords[currentIndex].id, e)}>
                    <svg width="28" height="28" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                  </button>
                  <h3 className="large-text">{learningWords[currentIndex]?.kor || ''}</h3>

                  {learningWords[currentIndex]?.synonyms && (
                    <div className="synonyms-text">{learningWords[currentIndex].synonyms}</div>
                  )}

                  {/* Example Sentences */}
                  {(learningWords[currentIndex]?.exEng || learningWords[currentIndex]?.exKor) && (
                    <div className="example-box">
                      {learningWords[currentIndex]?.exEng && <p className="ex-eng">"{learningWords[currentIndex].exEng}"</p>}
                      {learningWords[currentIndex]?.exKor && <p className="ex-kor">{learningWords[currentIndex].exKor}</p>}
                    </div>
                  )}
                </div>
              </div>
            </div>
          ) : (
            <div className="empty-state"><h3>단어가 없습니다.</h3></div>
          )}

          {learningWords.length > 0 && (
            <div className="controls mt-4">
              <button className="btn-prev" disabled={currentIndex === 0} onClick={handleLearnPrev}>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M19 12H5" /><path d="M12 19l-7-7 7-7" /></svg> 이전
              </button>
              <button className="btn-next" disabled={currentIndex === learningWords.length - 1} onClick={handleLearnNext}>
                다음 <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M5 12h14" /><path d="M12 5l7 7-7 7" /></svg>
              </button>
            </div>
          )}
        </div>
      )}

      {/* 4. ACTIVE QUIZ MODE */}
      {appMode === 'quiz-active' && (
        <div className="quiz-container">
          <div className="quiz-header">
            <button className="back-btn" onClick={() => setAppMode('quiz-menu')}>← 나가기</button>
            <div className="progress-bar">Q {currentIndex + 1} / {quizQueue.length}</div>
          </div>

          {quizQueue.length > 0 && quizConfig.format.includes('mc') && (
            <div className={`quiz-panel ${quizResult}`}>
              <button
                className={`star-btn ${favorites.includes(quizQueue[currentIndex].id) ? 'active' : 'inactive'}`}
                onClick={(e) => toggleFavorite(quizQueue[currentIndex].id, e)}>
                <svg width="28" height="28" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
              </button>
              <div className="question-box">
                
                <h2>
                  {quizConfig.format === 'mc-en2ko' ? quizQueue[currentIndex].eng : quizQueue[currentIndex].kor}
                </h2>
              </div>
              <div className="options-grid">
                {options.map((opt, idx) => (
                  <button key={idx} className="option-btn" disabled={quizResult !== null} onClick={() => checkMultipleChoice(opt)}>
                  
                    <div className="option-val">
                      {quizConfig.format === 'mc-en2ko' ? opt.kor : opt.eng}
                    </div>
                  </button>
                ))}
              </div>
              {quizResult === 'correct' && <div className="result-msg correct">정답입니다!</div>}
              {quizResult === 'wrong' && <div className="result-msg wrong">틀렸습니다. 정답: {quizConfig.format === 'mc-en2ko' ? quizQueue[currentIndex].kor : quizQueue[currentIndex].eng}</div>}
            </div>
          )}

          {quizQueue.length > 0 && quizConfig.format.includes('tx') && (
            <div className={`quiz-panel ${quizResult}`}>
              <button
                className={`star-btn ${favorites.includes(quizQueue[currentIndex].id) ? 'active' : 'inactive'}`}
                onClick={(e) => toggleFavorite(quizQueue[currentIndex].id, e)}>
                <svg width="28" height="28" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
              </button>
              <div className="question-box">
                <h2>{quizConfig.format === 'tx-en2ko' ? quizQueue[currentIndex].eng : quizQueue[currentIndex].kor}</h2>
                <p className="sub-hint">
                  {quizConfig.format === 'tx-en2ko' ? '뜻을 적어주세요' : '단어를 적어주세요'}
                </p>
              </div>

              <form onSubmit={checkTextInput} className="text-input-form">
                <input
                  ref={inputRef} type="text" value={inputText}
                  onChange={e => setInputText(e.target.value)}
                  placeholder="정답 입력..."
                  disabled={quizResult !== null}
                />
                <button type="submit" disabled={quizResult !== null || !inputText.trim()}>제출</button>
              </form>

              {quizResult === 'correct' && <div className="result-msg correct">정답입니다!</div>}
              {quizResult === 'wrong' && <div className="result-msg wrong">틀렸습니다. 정답: {quizConfig.format === 'tx-en2ko' ? quizQueue[currentIndex].kor : quizQueue[currentIndex].eng}</div>}
            </div>
          )}
        </div>
      )}

      {/* 5. QUIZ RESULT MODE */}
      {appMode === 'quiz-result' && (
        <div className="menu-panel" style={{ textAlign: 'center' }}>
          <h2>🎉 퀴즈 완료!</h2>
          <p style={{ fontSize: '1.2rem', marginBottom: '20px' }}>
            총 {quizQueue.length}문제 중 {quizQueue.length - wrongWords.length}문제를 맞췄습니다!
          </p>

          {wrongWords.length > 0 ? (
            <div style={{ marginBottom: '30px' }}>
              <p style={{ color: '#ef4444', fontWeight: 'bold' }}>틀린 단어가 {wrongWords.length}개 있습니다.</p>
              <button className="action-btn" style={{ background: 'linear-gradient(135deg, #ef4444, #b91c1c)', marginTop: '16px' }}
                onClick={() => {
                  setQuizQueue([...wrongWords].sort(() => Math.random() - 0.5));
                  setCurrentIndex(0);
                  setQuizResult(null);
                  setInputText('');
                  setWrongWords([]);
                  setAppMode('quiz-active');
                }}>
                🔄 틀린 단어 다시 풀기
              </button>
              <button className="action-btn" style={{ background: 'linear-gradient(135deg, #fbbf24, #f59e0b)', marginTop: '16px', color: 'white' }}
                onClick={() => {
                  setFavorites(prev => {
                    const nextFavs = [...prev];
                    wrongWords.forEach(w => {
                      if (!nextFavs.includes(w.id)) nextFavs.push(w.id);
                    });
                    return nextFavs;
                  });
                  alert('틀린 단어가 모두 즐겨찾기에 추가되었습니다! ⭐');
                }}>
                ⭐ 틀린 단어 모두 즐겨찾기
              </button>
            </div>
          ) : (
            <div style={{ marginBottom: '30px' }}>
              <p style={{ color: '#22c55e', fontWeight: 'bold' }}>모두 맞췄습니다! 완벽해요!</p>
            </div>
          )}

          <button className="back-btn" style={{ width: '100%', padding: '16px', borderRadius: '16px', background: 'rgba(255, 255, 255, 0.8)' }} onClick={() => setAppMode('home')}>
            🏠 홈으로 돌아가기
          </button>
        </div>
      )}

    </div>
  );
}

export default App;