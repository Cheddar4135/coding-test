# [level 0] 최빈값 구하기 - 120812 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120812) 

## 공부요약
### 📗 딕셔너리(dictionary)
[위키독스](https://wikidocs.net/16) 
[코딩도장](https://dojang.io/mod/page/view.php?id=2213) 참고

#### 빈 딕셔너리 만들기
a = {}
a = dict()

#### dict()로 {1: 'a', 2:'b'}딕셔너리 만들기
```
a = dict(1 = 'a', 2 = 'b') #키=값, 오류남
a = dict(apple='a',banana='b') #오류안남. 키 자동 문자열로 변환
```
사실 이 방법은 오류난다. 이건 숫자가 아닌 문자열이 키일때 따옴표없이 입력하는 방법이다.<br>
이때는 키에 ' '(작은따옴표)나 " "(큰따옴표)를 사용하지 않아야 한다. <br>
딕셔너리를 만들고 나면 문자열로 바뀐다.
```
a = dict(zip([1,2],['a','b']) #리스트
a = dict((1,'a'),(2,'b')) #튜플
```
**zip()내장함수:**
반복 가능한 객체 여러 개를 넣으면 요소 순서대로 튜플로 묶어서 zip 객체를 반환. 
`list(zip([1, 2, 3], [97, 98, 99]))`는 `[(1, 97), (2, 98), (3, 99)] `
> 딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고 Key를 통해 Value를 얻는다.

> 딕셔너리에는 동일한 Key가 중복으로 존재할 수 없다. 동일한 Key가 2개 존재할 경우, 이전의 쌍이 무시된다

> Key에 리스트는 쓸 수 없다.
하지만 문자열, 정수, 실수, 불, 튜플은 사용할 수 있으며 자료형을 섞어서 사용해도 된다.  딕셔너리의 Key로 쓸 수 있느냐, 없느냐는 Key가 변하는(mutable) 값인지, 변하지 않는(immutable) 값인지에 달려 있다. 리스트는 그 값이 변할 수 있기 때문에 Key로 쓸 수 없다. 
단, Value에는 변하는 값이든, 변하지 않는 값이든 아무 값이나 넣을 수 있다.

`a.values()` : values 함수를 호출하면 dict_values 객체를 리턴한다.

`a.items()` : items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 리턴한다.

#### `a.get('phone')`과 `a['phone']`의 차이점:
딕셔너리에 존재하지 않는 키로 값을 가져오려고 할 경우, a['nokey'] 방식은 오류를 발생시키고 a.get('nokey') 방식은 None을 리턴한다<br>

만약 None 대신 미리 정해 준 디폴트 값을 가져오게 하고 싶을 때는
`a.get('nokey','바보야 이런 키는 없어.')` 이렇게 디폴트값을 설정하면 된다.

#### 특정 키의 값을 갱신할 수도 있다.
```
a = ['apple':1,'banana':2]
a['apple']+=1
```

#### 🎈[중요] 키 유무 조사, key는 iterate하다.

`'phone' in a` <br>
: a 딕셔너리에 'phone'이라는 key가 있다면 True 리턴, 없다면 False 리턴 <br>
`for key in a` <br>
: a 딕셔너리 안에 있는 key를 iterator로 쓸 수 있다.

## 🎨 리스트의 모든 최댓값의 인덱스 구하기 - enumerate()
```
max = max(list)
answer = [index for index, val in enumerate(list_num) if val == m]
```
enumerate()로 자동으로 생성되는 인덱스는 디폴트가 0부터 시작이다. 만약 특정 수부터 시작하게 하고 싶다면, <br> `enumerate(list,start=101)` 이런식으로 변경해주면 된다.

---
### 성능 요약

메모리: 10.2 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 09일 15:29:08

### 문제 설명

<p>최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 <code>array</code>가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 &lt; <code>array</code>의 길이 &lt; 100</li>
<li>0&nbsp;≤&nbsp;<code>array</code>의 원소 &lt; 1000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>array</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 3, 3, 4]</td>
<td>3</td>
</tr>
<tr>
<td>[1, 1, 2, 2]</td>
<td>-1</td>
</tr>
<tr>
<td>[1]</td>
<td>1</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>[1, 2, 3, 3, 3, 4]에서 1은 1개 2는 1개 3은 3개 4는 1개로 최빈값은 3입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>[1, 1, 2, 2]에서 1은 2개 2는 2개로 최빈값이 1, 2입니다. 최빈값이 여러 개이므로 -1을 return 합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>[1]에는 1만 있으므로 최빈값은 1입니다.</li>
</ul>

<hr>

<p>※ 공지 - 2022년 10월 17일 제한 사항 및 테스트케이스가 수정되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
