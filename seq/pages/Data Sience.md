- 강재우 교수님
	- 빅데이터의 성질
		- volume = 데이터의 사이즈
		  logseq.order-list-type:: number
		- variety = 다양한 데이터
		  logseq.order-list-type:: number
		- velocity = 생산 속도
		  logseq.order-list-type:: number
		- veracity = 불확실성
		  logseq.order-list-type:: number
			- 불확실성? 다양한 해석이 나올 수 있다
			  logseq.order-list-type:: number
	- Challenge
		- 어떻게 저장하고 접근할 것인가 (solved) / 가치 창출 (어떻게?)
	- Effect
		- 기존의 top-down 방식으로 가설을 세우는 것을
		- big data를 통해 역으로 복잡한 가설을 세울 수 있게 된다
	- Data Science란?
		- ML과 Statistics
		- High-Performance Computing이 필요하다
		- CS + Statistics = ML
		- ML + Domain Science (적용할 과학 분야)
		- 이 세개의 영역이 만나는 곳이 DS다
	- 전형적인 DS pipeline
		- 흥미로운 질문
		  logseq.order-list-type:: number
		- Data를 가져옴
		  logseq.order-list-type:: number
		- Data 관측
		  logseq.order-list-type:: number
		- Data 정제 - insight를 얻을 수 있음 (꼭 필요한 단계)
		  logseq.order-list-type:: number
		- 결과에 대한 토론 및 visulization
		  logseq.order-list-type:: number
		- 1~5 반복
		- 다양한 언어를 다룰줄 알면 pipeline의 전체에 관여 가능하다
	- Data Cleaning
		- 정제
		- 하는데 80%의 시간이 소모됨
	- 과학자와 CS의 차이점
		- 과학자
			- data driven
			- 실제 데이터에서 info를 찾아내는 것
			- 의미 중시
		- CS
			- algorithm driven
			- 실제 데이터가 꼭 필요하지 않음
			- 정확도 중시
	- Data Scientist
		- 그 중간에 있으면 됨
	- Data Munging (= data wrangling)
		- Data를 가져오는 작업
		- Cleaning하는 작업
		- Acquiring and preparing
		- Data source에 따라서 다양하게 가져올 수 있음
		- API로 정보를 푸는 경우도 존재
		- Error vs Artifact
			- Error - 어떤 이유로 복구 불가능한 케이스
			- Artifact - 데이터의 이상이 systematically issue가 있을 때
		- Z-Score
			- 원래의 x를 모x로 뺀다음 / standard div로 나누면 된다
			- 평균이 0, sigma가 1인 정규화가 된 값이 나옴
			- 1.96sigma 안에 95%의 값이 들어감
			- 이 Z-score를 통해서 데이터의 무결성을 검증 가능하다
			- 정규분포를 따르는 것은 **자연적인 데이터를 의미**
		- Outlier Detection
			- 고칠 수 있는지?
			- Error인지 artifact인지 분류
			- Low dimension에서는 Visually 본다