- ![NumPy.pdf](../assets/NumPy_1710745948747_0.pdf)
- 수학적 연산을 기본으로 만든 것이 아님
- Array보다 빠르지만 hardware 성능 활용
- vectorized - vector처럼 연산한다
	- CPU 기반 병렬 계산
- 본래의 Python list의 문제점
	- C와 다르게 연속으로 값을 배치시키지 않았음
	- 오히려 linked-list 타입이다
- tensor와 똑같이 만들어진
- list to numpy 가능하
- **np.ndarray**
	- nd - n dimension
	- 3차원 이상을 tensor라고 한다
	- array = data type / vector = 수학적 의미
	- \_\_array\_\_ 있으면 numpy랑 연동이 가능하다
- **np.array()**
	- couorse로 인해 element 개수가 다르거나, type이 달라도 알아서 만들어준다
- **np.arange()**
	- range와 같은 기능이다
	- 만약 4를 넣게 되면 [0,1,2,3]의 array가 생성된다
- **np.zeros()**
	- 0으로 채우는 함수
	- ``np.zeros((4,4), dtype=float)``
	- 결과로는 4x4의 matrix이며 모든 값은 0이 된다
- **np.ones()**
	- zeros와 비슷하게 1로 채우는 함수를 의미함
	- ``np.ones((4,4), dtype=float)``
- **np.random**
	- np.ranom.randint()
		- 1st arg - start point
		- 2nd arg - end point
		- 3rd arg - matrix size
		- ``np.random.randint(0, 19, (3,3))``
		- \[[2 3 8] [7 0 7] [7 5 6]]
	- np.random.normal()
		- 1st arg - 평균
		- 2nd arg - 표준편차
		- 3rd arg - matrix size
		- ``np.random.normal(0, 1, (3,3))``
		- 3x3인 평균과 표준편차 값을 가지는 array가 나옴
- **np.concatenate()**
	- 두 개의 array를 일렬로 합친다
	- [1,2,3] + [3,4,5] = [1,2,3,3,4,5]
	- ``np.concatenate([array1, array2])``
	- axis option = 차원을 만들어줌
	- ```
	  array1 = np.arange(4).reshape(1,4)
	  array2 = np.arange(8).reshape(2,4)
	  array3 = np.concatenate([array1, array2], axis=0)
	  >>>
	  [[0 1 2 3]
	   [0 1 2 3]
	   [4 5 6 7]]
	  ```
- **np.split()**
	- params: matrix, (nxm), axis
		- axis = 1 수평으로 분할
		- axis = 0 수직으로 분할
		- (nxm) = 위치의 원소를 가지는 배열로 분할
			- ex) (2,4) -> x[:0:2], x[:2:4], x[:4:6]
			- ![image.png](../assets/image_1710862169486_0.png)
	- params: matrix, num, axis
		- axis는 동일
		- num = 몇개로 분할할지 정함
		- ![image.png](../assets/image_1710862232012_0.png)
	- params: matrix, [num], axis
		- axis는 동일
		- [num] = num 만큼 slicing 함 ([:num])
		- ![image.png](../assets/image_1710862351061_0.png)
- **a.reshape()**
	- 형태를 바꾼다
	- ```
	  array1 = np.array([1,2,3,4])
	  array2 = array1.reshape((2,2))
	  ```
	- \[[1,2][3,4]]
- **shape**
	- matrix의 크기를 return 한다
- **ndim**
	- matrix의 차원을 알려준다
- **dtype**
	- data type을 알려줌
- tensorflow 에서 unpacking
	- len으로 몇개 있는지 확인 후 unpack
	- x,y = tf.~
- **size**
	- 원소의 개수
	- shape에서 나오는 값들로도 충분히 알 수 있음
- **itemsize**
	- bit를 byte로 표현하는 것
- **data**
	- numpy에서는 일렬로 저장하기 때문에 memory 값이 나옴
	- stride 라는 개념이 나옴
	- stride tree 개념
- **꼼수**
	- 세상의 모든 것을 2차원으로 생각해라
	- shape를 3,2,4로 하면 중간의 빈 선으로 나누고 2차원으로 해석한다
- code: [numpy_1.ipynb](../assets/numpy_1_1710752124614_0.ipynb)