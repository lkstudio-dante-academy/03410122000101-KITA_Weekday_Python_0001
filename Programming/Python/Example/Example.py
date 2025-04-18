"""
import 키워드란?
- 특정 모듈을 가져오는 역할을 수행하는 키워드를 의미한다. (+ 즉, import 키워드를 활용하면 Python 이 지원하는
다양한 모듈을 가져와서 활용하는 것이 가능하다.)

Python 은 다양한 모듈을 지원하며 이러한 모듈을 활용하면 프로그램을 좀 더 수월하게 제작하는 것이 가능하다. (+ 즉,
이미 완성 된 기능을 재활용함으로서 작성해야되는 명령문을 줄이는 것이 가능하다.)

모듈 (Module) 이란?
- 재사용 가능한 명령문을 기능적으로 분리한 단위를 의미한다. (+ 즉, 모듈을 활용하면 명령문을 재사용해서
특정 프로그램을 빠르게 제작하는 것이 가능하다.)

모듈은 프로그래밍 언어에 따라 범위가 다양하며 Python 은 명령문이 작성 된 소스 파일을 모듈이라고 지칭한다. (+ 즉,
Python 은 소스 파일 단위로 연관 된 기능을 모듈화해서 명령문을 재사용한다는 것을 알 수 있다.)
"""
import os
import sys

"""
from ~ import 키워드란?
- import 키워드와 마찬가지로 특정 모듈을 가져오는 역할을 수행하는 키워드를 의미한다.

단, from ~ import 키워드는 import 키워드와 달리 특정 모듈에 하위에 있는 기능 (+ Ex. 함수 등등...) 수준까지
명시하는 것이 가능하다. (+ 즉, import 키워드는 모듈 수준까지만 명시하는 것이 가능하다.)
"""
from Example.Example_01 import E01Example_01
from Example.Example_02 import E01Example_02
from Example.Example_03 import E01Example_03
from Example.Example_04 import E01Example_04
from Example.Example_05 import E01Example_05
from Example.Example_06 import E01Example_06
from Example.Example_07 import E01Example_07
from Example.Example_08 import E01Example_08
from Example.Example_09 import E01Example_09
from Example.Example_10 import E01Example_10

from Practice.Practice_01 import P01Practice_01
from Practice.Practice_02 import P01Practice_02
from Practice.Practice_03 import P01Practice_03

from Training.Training_01 import T01Training_01
from Training.Training_02 import T01Training_02
from Training.Training_03 import T01Training_03
from Training.Training_04 import T01Training_04
from Training.Training_05 import T01Training_05

"""
메인 (Main) 모듈이란?
- Python 인터프리터가 가장 먼저 실행한 모듈을 의미한다. (+ 즉, 메인 모듈은 다른 프로그래밍 언어에서 존재하는
메인 함수와 유사한 개념이라는 것을 알 수 있다.)

들여쓰기란?
- Python 에서 특정 문법의 하위 여부를 지정하는 방법을 의미한다. (+ 즉, 들여쓰기도 Python 문법 중 하나라는
것을 알 수 있다.)

따라서 다른 프로그래밍 언어와 Python 에서 들여쓰기는 무분별하게 사용하는 것이 불가능하다.

주석이란?
- 사용자 (프로그래머) 를 위한 기능으로서 메모를 작성 할 수 있는 기능을 의미한다. (+ 즉, 주석은
Python 인터프리터에 의해서 기계어로 변환되지 않는다는 것을 알 수 있다.)

Python 은 다른 프로그래밍 언어와 달리 단일 행 주석만을 제공하며 # 기호를 통해 특정 행을 주석 처리하는 것이
가능하다.
"""
# 메인 모듈 일 경우
if __name__ == "__main__":
	# E01Example_01.start(sys.argv)
	# E01Example_02.start(sys.argv)
	# E01Example_03.start(sys.argv)
	# E01Example_04.start(sys.argv)
	# E01Example_05.start(sys.argv)
	# E01Example_06.start(sys.argv)
	# E01Example_07.start(sys.argv)
	# E01Example_08.start(sys.argv)
	# E01Example_09.start(sys.argv)
	# E01Example_10.start(sys.argv)
	
	# P01Practice_01.start(sys.argv)
	P01Practice_02.start(sys.argv)
	# P01Practice_03.start(sys.argv)
	
	# T01Training_01.start(sys.argv)
	# T01Training_02.start(sys.argv)
	# T01Training_03.start(sys.argv)
	# T01Training_04.start(sys.argv)
	# T01Training_05.start(sys.argv)
