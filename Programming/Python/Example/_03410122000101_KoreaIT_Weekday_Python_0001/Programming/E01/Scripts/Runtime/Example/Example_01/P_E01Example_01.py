import os
import sys

"""
Python 이란?
- 인터프리터 방식으로 동작하는 고수준 프로그래밍 언어를 의미한다. (+ 즉, Python 을 활용하면 프로그램을
제작하는 것이 가능하다.)

Python 데이터 분석을 비롯한 다양한 분야에서 활용되는 범용성이 뛰어난 언어이며 비교적 단순한 문법을
지니고 있기 때문에 프로그래밍 언어를 처음 공부 할 때 주로 추천되는 언어 중 하나이다.

프로그래밍 언어 (Programming Language) 란?
- 컴퓨터에게 작업을 지시하기 위한 프로그램을 제작 할 수 있는 언어를 의미한다. (+ 즉, 프로그래밍 언어를 활용하면
특정 목적을 지니는 프로그램을 제작하는 것이 가능하다.)

프로그래밍 언어는 크게 저수준 언어와 고수준 언어로 구분된다.

저수준 언어는 컴퓨터가 이해하기 쉬운 언어를 의미하며 고수준 언어는 사용자 (프로그래머) 가 이해하기 쉬운 언어를
의미한다. (+ 즉, 고수준 언어는 컴퓨터가 이해 할 수 없다는 것을 의미한다.)

따라서 고수준 언어를 통해 컴퓨터에게 작업을 지시하기 위해서는 고수준 언어를 컴퓨터가 이해 할 수 있는 언어로
변환 할 필요가 있으며 이를 처리해주는 프로그램을 컴파일러 or 인터프리터라고 한다.

컴파일러 (Compiler) vs 인터프리터 (Interpreter)
- 컴파일러와 인터프리터 모두 고수준 언어를 컴퓨터가 이해 할 수 있는 기계어로 변환하는 역할을 수행한다.

컴파일러는 사전에 고수준 언어로 된 명령문을 모두 기계어로 변환해서 프로그램의 형태로 제작하기 때문에 컴퓨터에
의해서 빠르게 처리된다는 장점이 존재한다. (+ 즉, 미리 기계어로 변환되기 때문에 컴퓨터 입장에서는 단순히 명령문을
읽어들여서 처리하기 때문에 속도가 빠르다는 것을 알 수 있다.)

단, 컴파일러는 사전에 고수준 언어로 된 명령문을 모두 기계어로 변환하기 때문에 고수준 언어로 된 명령문에 오류가
존재 할 경우 다시 해당 명령문을 모두 기계어로 변환하는 과정이 필요하다. (+ 즉, 컴파일러는 명령문의 변화가
빈번 할 경우 작업 효율이 떨어지는 단점이 존재한다.)

반면 인터프리터는 컴파일러와 달리 프로그램이 실행 중에 실시간으로 고수준 언어로 된 명령문을 기계어로 변환하기
때문에 컴파일러에 비해서 명령문의 변화에 좀 더 유연하게 대처하는 것이 가능하다. (+ 즉, 고수준 언어로 된 명령문을
수정해도 명령문 전체를 다시 기계어로 변환 할 필요가 없다.)

단, 인터프리터는 고수준 언어로 된 명령문을 기계어로 변환하는 과정이 프로그램이 실행 중에 실시간으로
처리되기 때문에 속도가 떨어지는 단점이 존재한다. (+ 즉, 고수준 언어로 된 명령문을 기계어로 변환하는 과정에서
성능 저하가 발생한다는 것을 알 수 있다.)
"""

# Example 1 (기초)
def start(args):
	"""
	print 함수란?
	- 콘솔 창에 문장을 출력하는 역할을 수행하는 함수를 의미한다. (+ 즉, print 함수를 활용하면 콘솔 창에
	다양한 문장을 출력하는 것이 가능하다.)
	
	함수 (Function) 란?
	- 특정 명령문을 포함하고 있는 기능을 의미한다. (+ 즉, 메서드를 실행하면 메서드 내부에 존재하는 명령문이
	동작한다는 것을 알 수 있다.)
	
	따라서 메서드를 활용하면 여러 기능들을 미리 만들어서 재사용하는 것이 가능하다.
	"""
	print("Hello, World!")
