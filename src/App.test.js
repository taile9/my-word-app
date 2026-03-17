import { render, screen } from '@testing-library/react';
import App from './App';

beforeEach(() => {
  // Mock fetch(/data2.csv) used by App
  global.fetch = jest.fn(() =>
    Promise.resolve({
      ok: true,
      text: () =>
        Promise.resolve(
          [
            'day1\tresume\t이력서\tCV 이력서\\ncurriculum vitae 라틴어 표현',
            '\tPlease submit your resume by Friday.\t금요일까지 이력서를 제출해 주세요.',
          ].join('\n')
        ),
    })
  );
});

afterEach(() => {
  jest.resetAllMocks();
});

test('renders snapvoca home UI after loading', async () => {
  render(<App />);

  // Loading state first
  expect(screen.getByText('단어장 준비중...')).toBeInTheDocument();

  // After fetch resolves, home actions appear
  expect(await screen.findByText('🎯 단어 시험(퀴즈) 시작하기')).toBeInTheDocument();
  expect(screen.getByText('DAY')).toBeInTheDocument();
  expect(screen.getByText('01')).toBeInTheDocument();
});
