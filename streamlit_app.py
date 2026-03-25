import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# ─────────────────────────────────────────────
# 페이지 설정
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="🧬 MBTI 성격유형 테스트",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# CSS 스타일링
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap');

/* 전체 앱 스타일 */
.stApp {
    background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    font-family: 'Noto Sans KR', sans-serif;
}

/* 헤더 숨기기 */
header[data-testid="stHeader"] {
    background: transparent;
}

/* 글래스모피즘 카드 */
.glass-card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    padding: 2rem;
    margin: 1rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

/* 타이틀 스타일 */
.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 900;
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 50%, #ffd200 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
    animation: glow 3s ease-in-out infinite alternate;
}

@keyframes glow {
    from { filter: brightness(1); }
    to { filter: brightness(1.3); }
}

.sub-title {
    text-align: center;
    color: rgba(255, 255, 255, 0.7);
    font-size: 1.1rem;
    font-weight: 300;
    margin-bottom: 2rem;
}

/* 시작 버튼 */
.start-btn-wrapper .stButton > button {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    color: white;
    border: none;
    padding: 1rem 3rem;
    font-size: 1.3rem;
    font-weight: 700;
    border-radius: 50px;
    width: 100%;
    transition: all 0.3s ease;
    box-shadow: 0 4px 20px rgba(245, 87, 108, 0.4);
}
.start-btn-wrapper .stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 30px rgba(245, 87, 108, 0.6);
}

/* 질문 카드 */
.question-card {
    background: rgba(255, 255, 255, 0.06);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 2.5rem;
    margin: 1.5rem 0;
    text-align: center;
}

.question-number {
    color: rgba(255, 255, 255, 0.4);
    font-size: 0.9rem;
    font-weight: 500;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 1rem;
}

.question-text {
    color: white;
    font-size: 1.4rem;
    font-weight: 700;
    line-height: 1.6;
    margin-bottom: 2rem;
}

/* 선택지 버튼 */
.option-btn {
    display: block;
    width: 100%;
    padding: 1.2rem 1.5rem;
    margin: 0.6rem 0;
    background: rgba(255, 255, 255, 0.06);
    border: 2px solid rgba(255, 255, 255, 0.15);
    border-radius: 16px;
    color: white;
    font-size: 1.05rem;
    cursor: pointer;
    transition: all 0.3s ease;
    text-align: left;
}
.option-btn:hover {
    background: rgba(245, 87, 108, 0.2);
    border-color: #f5576c;
    transform: translateX(8px);
}

/* 결과 카드 */
.result-header {
    text-align: center;
    padding: 2rem;
}

.mbti-type {
    font-size: 4.5rem;
    font-weight: 900;
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 50%, #ffd200 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    letter-spacing: 8px;
}

.mbti-nickname {
    color: rgba(255, 255, 255, 0.8);
    font-size: 1.5rem;
    font-weight: 500;
    margin-top: 0.5rem;
}

/* 스펙트럼 바 */
.spectrum-container {
    margin: 1.5rem 0;
}

.spectrum-labels {
    display: flex;
    justify-content: space-between;
    color: rgba(255, 255, 255, 0.7);
    font-size: 0.85rem;
    font-weight: 500;
    margin-bottom: 6px;
}

.spectrum-bar {
    height: 12px;
    border-radius: 6px;
    background: rgba(255, 255, 255, 0.1);
    overflow: hidden;
    position: relative;
}

.spectrum-fill {
    height: 100%;
    border-radius: 6px;
    transition: width 1s ease;
}

.spectrum-value {
    text-align: center;
    color: rgba(255, 255, 255, 0.5);
    font-size: 0.8rem;
    margin-top: 4px;
}

/* 섹션 타이틀 */
.section-title {
    color: white;
    font-size: 1.2rem;
    font-weight: 700;
    margin: 1.5rem 0 1rem 0;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

/* 태그 */
.tag {
    display: inline-block;
    padding: 0.4rem 1rem;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 500;
    margin: 0.2rem;
}
.tag-strength {
    background: rgba(99, 230, 190, 0.15);
    color: #63e6be;
    border: 1px solid rgba(99, 230, 190, 0.3);
}
.tag-weakness {
    background: rgba(255, 107, 129, 0.15);
    color: #ff6b81;
    border: 1px solid rgba(255, 107, 129, 0.3);
}
.tag-job {
    background: rgba(116, 143, 252, 0.15);
    color: #748ffc;
    border: 1px solid rgba(116, 143, 252, 0.3);
}
.tag-celeb {
    background: rgba(255, 210, 0, 0.15);
    color: #ffd200;
    border: 1px solid rgba(255, 210, 0, 0.3);
}

/* 설명 텍스트 */
.desc-text {
    color: rgba(255, 255, 255, 0.75);
    font-size: 1rem;
    line-height: 1.8;
}

/* 궁합 카드 */
.match-card {
    background: rgba(245, 87, 108, 0.1);
    border: 1px solid rgba(245, 87, 108, 0.3);
    border-radius: 16px;
    padding: 1.2rem;
    text-align: center;
}
.match-type {
    font-size: 2rem;
    font-weight: 900;
    color: #f5576c;
}
.match-label {
    color: rgba(255, 255, 255, 0.6);
    font-size: 0.85rem;
}

/* 프로그레스 바 커스텀 */
.stProgress > div > div {
    background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%);
    border-radius: 10px;
}

/* 통계 하이라이트 */
.stat-highlight {
    text-align: center;
    padding: 1.5rem;
    background: linear-gradient(135deg, rgba(240, 147, 251, 0.15), rgba(245, 87, 108, 0.15));
    border-radius: 16px;
    border: 1px solid rgba(245, 87, 108, 0.2);
}
.stat-number {
    font-size: 2.5rem;
    font-weight: 900;
    color: #f5576c;
}
.stat-label {
    color: rgba(255, 255, 255, 0.6);
    font-size: 0.9rem;
}

/* Plotly 차트 배경 투명 */
.js-plotly-plot .plotly .main-svg {
    background: transparent !important;
}

/* 다시하기 버튼 */
div[data-testid="stButton"] > button {
    border-radius: 50px;
    font-weight: 600;
    transition: all 0.3s ease;
}

/* 라디오 버튼 커스텀 */
div[data-testid="stRadio"] > label {
    color: white !important;
    font-weight: 500;
}
div[data-testid="stRadio"] > div {
    gap: 0.5rem;
}
div[data-testid="stRadio"] > div > label {
    background: rgba(255, 255, 255, 0.06) !important;
    border: 2px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 14px !important;
    padding: 1rem 1.2rem !important;
    color: rgba(255, 255, 255, 0.9) !important;
    transition: all 0.3s ease !important;
    font-size: 1rem !important;
}
div[data-testid="stRadio"] > div > label:hover {
    background: rgba(245, 87, 108, 0.15) !important;
    border-color: rgba(245, 87, 108, 0.5) !important;
}
div[data-testid="stRadio"] > div > label[data-checked="true"] {
    background: rgba(245, 87, 108, 0.2) !important;
    border-color: #f5576c !important;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# MBTI 질문 데이터
# ─────────────────────────────────────────────
QUESTIONS = [
    # E/I (0: E, 1: I)
    {
        "axis": "EI",
        "question": "주말에 에너지를 충전하는 방법은?",
        "options": [
            "친구들과 만나서 수다 떨기 🎉",
            "집에서 혼자만의 시간 보내기 🏠"
        ],
    },
    {
        "axis": "EI",
        "question": "새로운 모임에 갔을 때 나는?",
        "options": [
            "먼저 다가가서 말을 건다 👋",
            "누군가 말을 걸어주길 기다린다 🤫"
        ],
    },
    {
        "axis": "EI",
        "question": "생각을 정리할 때 나는?",
        "options": [
            "누군가와 대화하면서 정리한다 🗣️",
            "혼자 조용히 생각을 정리한다 📝"
        ],
    },
    # S/N (0: S, 1: N)
    {
        "axis": "SN",
        "question": "여행 계획을 세울 때 나는?",
        "options": [
            "구체적인 일정과 맛집 리스트를 준비한다 📋",
            "대략적인 방향만 정하고 즉흥적으로 즐긴다 🌈"
        ],
    },
    {
        "axis": "SN",
        "question": "어떤 영화가 더 끌리는가?",
        "options": [
            "실화를 바탕으로 한 감동 영화 🎬",
            "상상력이 넘치는 SF/판타지 영화 🚀"
        ],
    },
    {
        "axis": "SN",
        "question": "대화할 때 주로?",
        "options": [
            "실제 경험이나 사실 위주로 이야기한다 📌",
            "가능성이나 아이디어 위주로 이야기한다 💡"
        ],
    },
    # T/F (0: T, 1: F)
    {
        "axis": "TF",
        "question": "친구가 고민을 털어놓았을 때 나는?",
        "options": [
            "현실적인 해결책을 제시한다 🔧",
            "먼저 공감하고 감정을 들어준다 🤗"
        ],
    },
    {
        "axis": "TF",
        "question": "중요한 결정을 내릴 때 기준은?",
        "options": [
            "논리와 효율성을 우선시한다 📊",
            "관계된 사람들의 감정을 먼저 고려한다 💝"
        ],
    },
    {
        "axis": "TF",
        "question": "팀 프로젝트에서 갈등이 생겼을 때?",
        "options": [
            "객관적 사실을 기반으로 해결한다 ⚖️",
            "서로의 입장을 이해하며 조율한다 🤝"
        ],
    },
    # J/P (0: J, 1: P)
    {
        "axis": "JP",
        "question": "약속 시간에 대한 나의 태도는?",
        "options": [
            "항상 10분 전에 도착한다 ⏰",
            "시간 맞춰 가거나 살짝 늦을 때도 있다 😅"
        ],
    },
    {
        "axis": "JP",
        "question": "방 정리 스타일은?",
        "options": [
            "정해진 자리에 늘 정돈해 둔다 🗄️",
            "나만의 '창의적 혼돈' 속에서 편안하다 🎨"
        ],
    },
    {
        "axis": "JP",
        "question": "과제나 업무 마감일이 다가올 때?",
        "options": [
            "이미 미리미리 해놓은 상태다 ✅",
            "마감 직전 집중력이 폭발한다 🔥"
        ],
    },
]

# ─────────────────────────────────────────────
# MBTI 상세 데이터
# ─────────────────────────────────────────────
MBTI_DATA = {
    "INTJ": {
        "nickname": "전략가 🏰",
        "emoji": "🏰",
        "description": "독립적이고 분석적인 전략가. 높은 기준과 원대한 비전을 가지고 체계적으로 목표를 달성합니다. 논리적 사고와 창의적 통찰력을 겸비한 타입입니다.",
        "strengths": ["전략적 사고", "독립적", "높은 기준", "지식 탐구", "결단력"],
        "weaknesses": ["완벽주의", "감정 표현 서툼", "타인에게 엄격", "고집"],
        "love_style": "지적 교감을 중시하며, 깊고 의미 있는 관계를 추구합니다.",
        "best_match": "ENFP",
        "careers": ["데이터 과학자", "전략 컨설턴트", "소프트웨어 아키텍트", "연구원", "투자 분석가"],
        "celebrities": ["일론 머스크", "크리스토퍼 놀란", "미셸 오바마"],
        "traits": {"분석력": 95, "창의성": 85, "리더십": 80, "공감력": 45, "실행력": 88, "사교성": 35},
        "color": "#6c5ce7",
    },
    "INTP": {
        "nickname": "논리술사 🔬",
        "emoji": "🔬",
        "description": "끝없는 호기심으로 세상의 원리를 탐구하는 사색가. 복잡한 문제를 논리적으로 풀어내는 것을 즐기며, 혁신적인 아이디어를 만들어냅니다.",
        "strengths": ["분석적 사고", "창의적", "객관적", "지적 호기심", "적응력"],
        "weaknesses": ["우유부단", "현실 감각 부족", "감정 표현 어려움", "규칙 무시"],
        "love_style": "지적 대화를 통해 유대감을 형성하며, 자유롭고 독립적인 관계를 선호합니다.",
        "best_match": "ENTJ",
        "careers": ["프로그래머", "물리학자", "철학자", "게임 개발자", "수학자"],
        "celebrities": ["아인슈타인", "빌 게이츠", "래리 페이지"],
        "traits": {"분석력": 98, "창의성": 92, "리더십": 40, "공감력": 38, "실행력": 55, "사교성": 30},
        "color": "#0984e3",
    },
    "ENTJ": {
        "nickname": "통솔자 👑",
        "emoji": "👑",
        "description": "타고난 리더십으로 사람들을 이끄는 카리스마 있는 지도자. 목표를 향해 효율적으로 조직을 이끌며, 도전을 즐기는 타입입니다.",
        "strengths": ["강한 리더십", "전략적", "자신감", "효율적", "결단력"],
        "weaknesses": ["지배적", "감정 무시", "참을성 부족", "지나친 자신감"],
        "love_style": "성장을 함께할 동반자를 찾으며, 서로를 발전시키는 관계를 추구합니다.",
        "best_match": "INFP",
        "careers": ["CEO", "변호사", "경영 컨설턴트", "정치인", "기업가"],
        "celebrities": ["스티브 잡스", "마거릿 대처", "고든 램지"],
        "traits": {"분석력": 85, "창의성": 70, "리더십": 98, "공감력": 42, "실행력": 95, "사교성": 72},
        "color": "#d63031",
    },
    "ENTP": {
        "nickname": "변론가 ⚡",
        "emoji": "⚡",
        "description": "재치 있고 논쟁을 즐기는 혁신가. 기존의 틀을 깨고 새로운 가능성을 탐색하는 것을 좋아하며, 다양한 분야에 관심을 가집니다.",
        "strengths": ["창의적", "재치 있음", "논리적", "적응력", "도전 정신"],
        "weaknesses": ["논쟁적", "끈기 부족", "규칙 싫어함", "감정 무시"],
        "love_style": "지적 자극을 주는 파트너를 선호하며, 유머와 토론이 넘치는 관계를 즐깁니다.",
        "best_match": "INFJ",
        "careers": ["기업가", "변호사", "크리에이티브 디렉터", "저널리스트", "발명가"],
        "celebrities": ["로버트 다우니 주니어", "마크 트웨인", "토마스 에디슨"],
        "traits": {"분석력": 88, "창의성": 95, "리더십": 70, "공감력": 50, "실행력": 60, "사교성": 82},
        "color": "#e17055",
    },
    "INFJ": {
        "nickname": "옹호자 🌙",
        "emoji": "🌙",
        "description": "깊은 통찰력과 이상주의를 가진 조용한 영향력자. 다른 사람의 감정을 깊이 이해하며, 세상을 더 나은 곳으로 만들고자 합니다.",
        "strengths": ["통찰력", "이상주의", "헌신적", "창의적", "공감 능력"],
        "weaknesses": ["완벽주의", "번아웃 위험", "갈등 회피", "비현실적"],
        "love_style": "영혼의 교감을 나눌 수 있는 깊은 관계를 추구하며, 진정성을 중요시합니다.",
        "best_match": "ENTP",
        "careers": ["상담사", "작가", "심리학자", "교사", "비영리 활동가"],
        "celebrities": ["마틴 루터 킹", "니콜 키드먼", "간디"],
        "traits": {"분석력": 75, "창의성": 90, "리더십": 65, "공감력": 97, "실행력": 70, "사교성": 45},
        "color": "#a29bfe",
    },
    "INFP": {
        "nickname": "중재자 🦋",
        "emoji": "🦋",
        "description": "상상력이 풍부하고 감수성이 뛰어난 이상주의자. 내면의 가치를 중시하며, 자신만의 독특한 세계를 가지고 있습니다.",
        "strengths": ["창의적", "공감 능력", "열정적", "이상주의", "진정성"],
        "weaknesses": ["현실 감각 부족", "자기비판적", "우유부단", "상처받기 쉬움"],
        "love_style": "로맨틱하고 깊은 감정적 교류를 원하며, 진실된 사랑을 꿈꿉니다.",
        "best_match": "ENTJ",
        "careers": ["작가", "예술가", "상담사", "디자이너", "음악가"],
        "celebrities": ["셰익스피어", "윌리엄 워즈워스", "오드리 헵번"],
        "traits": {"분석력": 60, "창의성": 97, "리더십": 35, "공감력": 95, "실행력": 45, "사교성": 42},
        "color": "#fd79a8",
    },
    "ENFJ": {
        "nickname": "선도자 🌟",
        "emoji": "🌟",
        "description": "따뜻한 카리스마로 사람들에게 영감을 주는 타고난 리더. 다른 사람의 성장을 돕는 것에서 기쁨을 느끼며, 긍정적 변화를 이끕니다.",
        "strengths": ["카리스마", "공감 능력", "이타적", "소통력", "리더십"],
        "weaknesses": ["자기 희생", "지나친 이상주의", "갈등에 민감", "과도한 책임감"],
        "love_style": "따뜻하고 헌신적인 관계를 추구하며, 파트너의 성장을 적극 지원합니다.",
        "best_match": "ISTP",
        "careers": ["교사", "HR 매니저", "사회복지사", "코치", "외교관"],
        "celebrities": ["오바마", "오프라 윈프리", "마틴 루터 킹"],
        "traits": {"분석력": 65, "창의성": 75, "리더십": 92, "공감력": 95, "실행력": 82, "사교성": 95},
        "color": "#00b894",
    },
    "ENFP": {
        "nickname": "활동가 🎪",
        "emoji": "🎪",
        "description": "열정적이고 자유로운 영혼의 소유자. 어디서든 즐거움을 찾고, 사람들에게 영감을 주며, 무한한 가능성을 탐험합니다.",
        "strengths": ["열정적", "창의적", "사교적", "낙관적", "적응력"],
        "weaknesses": ["산만함", "과도한 감정", "계획성 부족", "끈기 부족"],
        "love_style": "자유롭고 재미있는 관계를 원하며, 감정적 유대를 매우 중시합니다.",
        "best_match": "INTJ",
        "careers": ["크리에이터", "마케터", "배우", "기자", "이벤트 플래너"],
        "celebrities": ["로빈 윌리엄스", "월트 디즈니", "로버트 다우니 주니어"],
        "traits": {"분석력": 55, "창의성": 95, "리더십": 60, "공감력": 88, "실행력": 50, "사교성": 98},
        "color": "#fdcb6e",
    },
    "ISTJ": {
        "nickname": "현실주의자 📚",
        "emoji": "📚",
        "description": "신뢰할 수 있고 책임감 강한 현실주의자. 체계적이고 꼼꼼하며, 맡은 일을 끝까지 완수하는 든든한 존재입니다.",
        "strengths": ["책임감", "꼼꼼함", "신뢰성", "인내력", "체계적"],
        "weaknesses": ["융통성 부족", "변화 거부", "감정 표현 어려움", "고집"],
        "love_style": "안정적이고 헌신적인 관계를 추구하며, 행동으로 사랑을 표현합니다.",
        "best_match": "ESFP",
        "careers": ["회계사", "공무원", "법률가", "은행원", "군인"],
        "celebrities": ["조지 워싱턴", "앤젤라 메르켈", "워렌 버핏"],
        "traits": {"분석력": 80, "창의성": 40, "리더십": 70, "공감력": 50, "실행력": 98, "사교성": 38},
        "color": "#2d3436",
    },
    "ISFJ": {
        "nickname": "수호자 🛡️",
        "emoji": "🛡️",
        "description": "따뜻하고 헌신적인 수호자. 조용하지만 깊은 관심과 배려로 주변을 돌보며, 전통과 안정을 소중히 여깁니다.",
        "strengths": ["헌신적", "세심함", "인내심", "신뢰성", "관찰력"],
        "weaknesses": ["자기 희생", "변화 두려움", "거절 어려움", "과부하"],
        "love_style": "세심한 배려와 헌신으로 사랑하며, 안정적인 가정을 꿈꿉니다.",
        "best_match": "ESTP",
        "careers": ["간호사", "교사", "사서", "사회복지사", "행정직"],
        "celebrities": ["비욘세", "케이트 미들턴", "앤 해서웨이"],
        "traits": {"분석력": 65, "창의성": 45, "리더십": 50, "공감력": 92, "실행력": 90, "사교성": 48},
        "color": "#00cec9",
    },
    "ESTJ": {
        "nickname": "경영자 📊",
        "emoji": "📊",
        "description": "질서와 효율을 중시하는 타고난 관리자. 명확한 규칙과 체계를 세우고, 책임감 있게 조직을 이끄는 실행형 리더입니다.",
        "strengths": ["조직력", "결단력", "책임감", "효율적", "리더십"],
        "weaknesses": ["강압적", "감정 무시", "융통성 부족", "과도한 통제"],
        "love_style": "안정적이고 전통적인 관계를 중시하며, 실질적인 방식으로 사랑을 표현합니다.",
        "best_match": "ISFP",
        "careers": ["프로젝트 매니저", "판사", "경영자", "군 장교", "은행 지점장"],
        "celebrities": ["헨리 포드", "미셸 오바마", "주디 덴치"],
        "traits": {"분석력": 78, "창의성": 38, "리더십": 95, "공감력": 45, "실행력": 97, "사교성": 70},
        "color": "#e84393",
    },
    "ESFJ": {
        "nickname": "집정관 🤝",
        "emoji": "🤝",
        "description": "사교적이고 배려심 깊은 세상의 연결자. 조화로운 관계를 만들고, 다른 사람을 돕는 것에서 보람을 느끼는 따뜻한 사람입니다.",
        "strengths": ["배려심", "사교성", "협동심", "충성심", "실용적"],
        "weaknesses": ["인정 욕구", "갈등 회피", "지나친 걱정", "변화 거부"],
        "love_style": "따뜻하고 사랑 넘치는 관계를 만들며, 가족과 친구를 최우선으로 챙깁니다.",
        "best_match": "ISTP",
        "careers": ["이벤트 플래너", "간호사", "교사", "영업직", "호텔리어"],
        "celebrities": ["테일러 스위프트", "제니퍼 가너", "휴 잭맨"],
        "traits": {"분석력": 55, "창의성": 48, "리더십": 65, "공감력": 92, "실행력": 85, "사교성": 98},
        "color": "#e17055",
    },
    "ISTP": {
        "nickname": "장인 🔧",
        "emoji": "🔧",
        "description": "냉철하고 실용적인 문제 해결사. 손으로 직접 만들고 분석하며, 위기 상황에서 침착하게 대응하는 능력자입니다.",
        "strengths": ["실용적", "냉철함", "적응력", "문제해결", "독립적"],
        "weaknesses": ["감정 표현 어려움", "약속 불이행", "위험 추구", "무관심"],
        "love_style": "자유롭고 독립적인 관계를 선호하며, 말보다 행동으로 사랑을 보여줍니다.",
        "best_match": "ENFJ",
        "careers": ["엔지니어", "파일럿", "요리사", "응급구조사", "메카닉"],
        "celebrities": ["톰 크루즈", "클린트 이스트우드", "마이클 조던"],
        "traits": {"분석력": 85, "창의성": 60, "리더십": 45, "공감력": 35, "실행력": 90, "사교성": 32},
        "color": "#636e72",
    },
    "ISFP": {
        "nickname": "모험가 🎨",
        "emoji": "🎨",
        "description": "감성적이고 자유로운 예술가 영혼. 현재를 즐기며, 자신만의 미적 감각으로 세상을 아름답게 만드는 조용한 모험가입니다.",
        "strengths": ["예술적 감각", "유연함", "공감력", "관찰력", "겸손함"],
        "weaknesses": ["자기표현 어려움", "계획성 부족", "갈등 회피", "예민함"],
        "love_style": "조용하지만 깊은 사랑을 하며, 소소한 일상 속 로맨스를 즐깁니다.",
        "best_match": "ESTJ",
        "careers": ["디자이너", "사진작가", "플로리스트", "수의사", "요리사"],
        "celebrities": ["밥 로스", "마이클 잭슨", "라나 델 레이"],
        "traits": {"분석력": 50, "창의성": 92, "리더십": 30, "공감력": 88, "실행력": 55, "사교성": 45},
        "color": "#55efc4",
    },
    "ESTP": {
        "nickname": "사업가 🎯",
        "emoji": "🎯",
        "description": "대담하고 에너지 넘치는 행동파. 위험을 두려워하지 않고, 순간의 기회를 포착하는 능력이 뛰어난 현실주의자입니다.",
        "strengths": ["대담함", "사교성", "관찰력", "실용적", "적응력"],
        "weaknesses": ["충동적", "참을성 부족", "규칙 무시", "감정 무시"],
        "love_style": "즉흥적이고 재미있는 연애를 즐기며, 파트너와 함께 모험을 떠나길 좋아합니다.",
        "best_match": "ISFJ",
        "careers": ["세일즈", "응급구조사", "스포츠 선수", "기업가", "형사"],
        "celebrities": ["도널드 트럼프", "마돈나", "어니스트 헤밍웨이"],
        "traits": {"분석력": 65, "창의성": 55, "리더십": 72, "공감력": 40, "실행력": 95, "사교성": 92},
        "color": "#ff7675",
    },
    "ESFP": {
        "nickname": "연예인 🎭",
        "emoji": "🎭",
        "description": "무대 위의 주인공처럼 빛나는 엔터테이너. 주변에 활기를 불어넣고, 지금 이 순간을 최대한 즐기는 긍정 에너지의 원천입니다.",
        "strengths": ["사교성", "낙관적", "실용적", "유머 감각", "관대함"],
        "weaknesses": ["산만함", "계획성 부족", "갈등 회피", "장기 목표 약함"],
        "love_style": "즐겁고 열정적인 연애를 하며, 파트너에게 아낌없이 사랑을 표현합니다.",
        "best_match": "ISTJ",
        "careers": ["연예인", "이벤트 플래너", "여행 가이드", "인테리어 디자이너", "영업직"],
        "celebrities": ["마릴린 먼로", "엘튼 존", "제이미 올리버"],
        "traits": {"분석력": 42, "창의성": 68, "리더십": 50, "공감력": 78, "실행력": 72, "사교성": 99},
        "color": "#fab1a0",
    },
}

# MBTI 인구 비율 (%)
MBTI_POPULATION = {
    "ISTJ": 11.6, "ISFJ": 13.8, "INFJ": 1.5, "INTJ": 2.1,
    "ISTP": 5.4, "ISFP": 8.8, "INFP": 4.4, "INTP": 3.3,
    "ESTP": 4.3, "ESFP": 8.5, "ENFP": 8.1, "ENTP": 3.2,
    "ESTJ": 8.7, "ESFJ": 12.3, "ENFJ": 2.5, "ENTJ": 1.8,
}


# ─────────────────────────────────────────────
# 유틸리티 함수
# ─────────────────────────────────────────────
def calculate_mbti(answers):
    """답변을 분석하여 MBTI 유형과 각 축 비율을 반환"""
    axes = {"EI": [0, 0], "SN": [0, 0], "TF": [0, 0], "JP": [0, 0]}

    for i, answer in enumerate(answers):
        axis = QUESTIONS[i]["axis"]
        axes[axis][answer] += 1

    mbti = ""
    percentages = {}
    axis_pairs = [("E", "I", "EI"), ("S", "N", "SN"), ("T", "F", "TF"), ("J", "P", "JP")]

    for first, second, key in axis_pairs:
        total = axes[key][0] + axes[key][1]
        first_pct = (axes[key][0] / total) * 100
        second_pct = (axes[key][1] / total) * 100

        if axes[key][0] >= axes[key][1]:
            mbti += first
        else:
            mbti += second

        percentages[key] = {"first": first_pct, "second": second_pct,
                           "first_label": first, "second_label": second}

    return mbti, percentages


def render_spectrum_bar(label_left, label_right, pct_left, gradient_colors):
    """스펙트럼 바 렌더링"""
    pct_right = 100 - pct_left
    st.markdown(f"""
    <div class="spectrum-container">
        <div class="spectrum-labels">
            <span><b>{label_left}</b> {pct_left:.0f}%</span>
            <span>{pct_right:.0f}% <b>{label_right}</b></span>
        </div>
        <div class="spectrum-bar">
            <div class="spectrum-fill" style="width: {pct_left}%;
                background: linear-gradient(90deg, {gradient_colors[0]}, {gradient_colors[1]});">
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def create_radar_chart(traits, color):
    """Plotly 레이더 차트 생성"""
    categories = list(traits.keys())
    values = list(traits.values())
    values.append(values[0])
    categories.append(categories[0])

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        fillcolor=f'rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.25)',
        line=dict(color=color, width=2),
        marker=dict(size=8, color=color),
    ))

    fig.update_layout(
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            radialaxis=dict(visible=True, range=[0, 100],
                          gridcolor='rgba(255,255,255,0.1)',
                          tickfont=dict(color='rgba(255,255,255,0.4)', size=10)),
            angularaxis=dict(gridcolor='rgba(255,255,255,0.1)',
                           tickfont=dict(color='rgba(255,255,255,0.8)', size=13)),
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=60, r=60, t=40, b=40),
        height=380,
    )
    return fig


def create_population_chart(my_type):
    """MBTI 인구 비율 차트 생성"""
    types = list(MBTI_POPULATION.keys())
    values = list(MBTI_POPULATION.values())
    colors = ['#f5576c' if t == my_type else 'rgba(255,255,255,0.2)' for t in types]

    fig = go.Figure(go.Bar(
        x=types,
        y=values,
        marker=dict(color=colors, line=dict(width=0)),
        text=[f'{v}%' for v in values],
        textposition='outside',
        textfont=dict(color='rgba(255,255,255,0.7)', size=10),
    ))

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            tickfont=dict(color='rgba(255,255,255,0.7)', size=11),
            gridcolor='rgba(255,255,255,0.05)',
        ),
        yaxis=dict(
            tickfont=dict(color='rgba(255,255,255,0.5)', size=10),
            gridcolor='rgba(255,255,255,0.05)',
            title=dict(text='인구 비율 (%)', font=dict(color='rgba(255,255,255,0.5)')),
        ),
        margin=dict(l=40, r=20, t=20, b=40),
        height=320,
    )
    return fig


# ─────────────────────────────────────────────
# 세션 상태 초기화
# ─────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "home"
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "mbti_result" not in st.session_state:
    st.session_state.mbti_result = None


def go_home():
    st.session_state.page = "home"
    st.session_state.current_q = 0
    st.session_state.answers = {}
    st.session_state.mbti_result = None


def start_test():
    st.session_state.page = "test"
    st.session_state.current_q = 0
    st.session_state.answers = {}


def next_question(answer):
    st.session_state.answers[st.session_state.current_q] = answer
    if st.session_state.current_q < len(QUESTIONS) - 1:
        st.session_state.current_q += 1
    else:
        st.session_state.page = "result"
        answers_list = [st.session_state.answers[i] for i in range(len(QUESTIONS))]
        mbti, pcts = calculate_mbti(answers_list)
        st.session_state.mbti_result = mbti
        st.session_state.mbti_percentages = pcts


def prev_question():
    if st.session_state.current_q > 0:
        st.session_state.current_q -= 1


# ─────────────────────────────────────────────
# 페이지: 홈
# ─────────────────────────────────────────────
if st.session_state.page == "home":
    st.markdown("")
    st.markdown("")

    st.markdown('<div class="main-title">🧬 MBTI 성격유형 테스트</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">12개 질문으로 알아보는 나의 성격유형</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; color: rgba(255,255,255,0.8); line-height: 2;">
        <div style="font-size: 3rem; margin-bottom: 1rem;">🧠 💜 🎯 ✨</div>
        <p style="font-size: 1.05rem;">
            간단한 <b>12개의 질문</b>에 답하면<br>
            당신의 MBTI 성격유형을 분석해 드립니다!
        </p>
        <div style="margin: 1.5rem 0; padding: 1rem; background: rgba(255,255,255,0.05); border-radius: 12px;">
            <p style="font-size: 0.9rem; color: rgba(255,255,255,0.6);">
                📊 성격 특성 레이더 차트 &nbsp;|&nbsp;
                💕 연애 궁합 분석 &nbsp;|&nbsp;
                💼 추천 직업 &nbsp;|&nbsp;
                ⭐ 같은 유형 유명인
            </p>
        </div>
        <p style="font-size: 0.85rem; color: rgba(255,255,255,0.4);">
            ⏱️ 소요시간: 약 2~3분
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("")
    st.markdown('<div class="start-btn-wrapper">', unsafe_allow_html=True)
    st.button("🚀 테스트 시작하기", on_click=start_test, use_container_width=True, key="start_btn")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; margin-top: 3rem; color: rgba(255,255,255,0.25); font-size: 0.8rem;">
        본 테스트는 재미를 위한 간이 테스트이며, 공식적인 MBTI 검사와는 다릅니다.
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# 페이지: 테스트
# ─────────────────────────────────────────────
elif st.session_state.page == "test":
    q_idx = st.session_state.current_q
    q = QUESTIONS[q_idx]
    progress = (q_idx) / len(QUESTIONS)

    # 프로그레스 바
    st.progress(progress, text=f"질문 {q_idx + 1} / {len(QUESTIONS)}")

    # 질문 카드
    st.markdown(f"""
    <div class="question-card">
        <div class="question-number">QUESTION {q_idx + 1} OF {len(QUESTIONS)}</div>
        <div class="question-text">{q["question"]}</div>
    </div>
    """, unsafe_allow_html=True)

    # 선택지 버튼
    st.markdown("")
    col1, col2 = st.columns(2)

    with col1:
        if st.button(q["options"][0], key=f"opt_a_{q_idx}", use_container_width=True):
            next_question(0)
            st.rerun()

    with col2:
        if st.button(q["options"][1], key=f"opt_b_{q_idx}", use_container_width=True):
            next_question(1)
            st.rerun()

    # 이전 버튼
    if q_idx > 0:
        st.markdown("")
        if st.button("← 이전 질문", key="prev_btn", on_click=prev_question):
            st.rerun()


# ─────────────────────────────────────────────
# 페이지: 결과
# ─────────────────────────────────────────────
elif st.session_state.page == "result":
    mbti = st.session_state.mbti_result
    data = MBTI_DATA[mbti]
    pcts = st.session_state.mbti_percentages

    # ─── 결과 헤더 ───
    st.markdown(f"""
    <div class="glass-card">
        <div class="result-header">
            <p style="color: rgba(255,255,255,0.5); font-size: 0.9rem; letter-spacing: 3px;">YOUR MBTI TYPE</p>
            <div class="mbti-type">{mbti}</div>
            <div class="mbti-nickname">{data['nickname']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ─── 4축 스펙트럼 ───
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📊 성격 유형 스펙트럼</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    gradient_pairs = [
        ("#fdcb6e", "#e17055"),
        ("#55efc4", "#00b894"),
        ("#fd79a8", "#e84393"),
        ("#a29bfe", "#6c5ce7"),
    ]
    axis_labels = [("외향 (E)", "내향 (I)"), ("감각 (S)", "직관 (N)"),
                   ("사고 (T)", "감정 (F)"), ("판단 (J)", "인식 (P)")]
    axis_keys = ["EI", "SN", "TF", "JP"]

    for i, key in enumerate(axis_keys):
        render_spectrum_bar(
            axis_labels[i][0], axis_labels[i][1],
            pcts[key]["first"], gradient_pairs[i]
        )

    # ─── 성격 설명 ───
    st.markdown(f"""
    <div class="glass-card">
        <div class="section-title">🪶 성격 설명</div>
        <div class="desc-text">{data['description']}</div>
    </div>
    """, unsafe_allow_html=True)

    # ─── 레이더 차트 ───
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 성격 특성 분석</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    radar_fig = create_radar_chart(data["traits"], data["color"])
    st.plotly_chart(radar_fig, use_container_width=True, config={"displayModeBar": False})

    # ─── 강점 & 약점 ───
    col_s, col_w = st.columns(2)
    with col_s:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">💪 강점</div>', unsafe_allow_html=True)
        tags = "".join([f'<span class="tag tag-strength">{s}</span>' for s in data["strengths"]])
        st.markdown(tags, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_w:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">⚡ 약점</div>', unsafe_allow_html=True)
        tags = "".join([f'<span class="tag tag-weakness">{w}</span>' for w in data["weaknesses"]])
        st.markdown(tags, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ─── 연애 스타일 & 궁합 ───
    st.markdown(f"""
    <div class="glass-card">
        <div class="section-title">💕 연애 스타일</div>
        <div class="desc-text">{data['love_style']}</div>
        <div style="margin-top: 1.2rem;">
            <div class="match-card">
                <div class="match-label">💘 베스트 궁합</div>
                <div class="match-type">{data['best_match']}</div>
                <div class="match-label">{MBTI_DATA[data['best_match']]['nickname']}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ─── 추천 직업 ───
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">💼 추천 직업 TOP 5</div>', unsafe_allow_html=True)
    tags = "".join([f'<span class="tag tag-job">{j}</span>' for j in data["careers"]])
    st.markdown(tags, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ─── 같은 유형 유명인 ───
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">⭐ 같은 유형 유명인</div>', unsafe_allow_html=True)
    tags = "".join([f'<span class="tag tag-celeb">{c}</span>' for c in data["celebrities"]])
    st.markdown(tags, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ─── 인구 비율 통계 ───
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🌍 MBTI 유형별 인구 비율</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    my_pct = MBTI_POPULATION[mbti]
    rarer_count = sum(1 for v in MBTI_POPULATION.values() if v < my_pct)
    rarity_pct = (rarer_count / 16) * 100

    st.markdown(f"""
    <div class="stat-highlight">
        <div class="stat-number">{my_pct}%</div>
        <div class="stat-label">
            전체 인구 중 <b>{mbti}</b> 유형의 비율<br>
            {'🌟 상위 ' + f'{100-rarity_pct:.0f}%의 희귀한 유형!' if my_pct < 5 else '많은 사람들이 공감할 수 있는 유형이에요!'}
        </div>
    </div>
    """, unsafe_allow_html=True)

    pop_fig = create_population_chart(mbti)
    st.plotly_chart(pop_fig, use_container_width=True, config={"displayModeBar": False})

    # ─── 다시하기 버튼 ───
    st.markdown("")
    st.markdown("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.button("🔄 다시 테스트하기", on_click=go_home, use_container_width=True, key="retry_btn")

    st.markdown("""
    <div style="text-align: center; margin-top: 2rem; color: rgba(255,255,255,0.25); font-size: 0.8rem;">
        본 테스트는 재미를 위한 간이 테스트이며, 공식적인 MBTI 검사와는 다릅니다.<br>
        © 2026 MBTI 성격유형 테스트
    </div>
    """, unsafe_allow_html=True)
