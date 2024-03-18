- 단계 작성
	- txt 파일로 필요한 url들이 있다고 가정함
	  logseq.order-list-type:: number
	- depth는 50으로 한정함
	  logseq.order-list-type:: number
	- img만 받아옴
	  logseq.order-list-type:: number
	- 그 외에 제목과 태그로 나눌 예정
	  logseq.order-list-type:: number
- 큰 구조
	- SQL 직접 때려박을 생각
	- Request와 re로 빠르게 수집할 수 있도록
	- bs4까지 사용하여 수집 (이건 여부 파악 후 생각)
- DB 구조
	- IMG
		- PK - primary
		- Fk - URL PK
	- URL
		- PK - primary
		- Visited - 0,1