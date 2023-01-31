# OpenCV with C++

## 주요 함수

### BMP 파일 영상을 화면에 출력하는 HelloCV 소스 코드

```cpp
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main()
{
	cout << "Hello OpenCV " << CV_VERSION << endl;

	Mat img;
	img = imread("lenna.bmp");

	if (img.empty()) {
		cerr << "Image load failed!" << endl;
		return -1;
	}

	namedWindow("image");
	imshow("image", img);

	waitKey();

	return 0;
}
```

### imread()

```cpp
Mat imread(const String& filename, int flags = IMREAD_COLOR);
```

- filename : 불러올 영상 파일 이름
- flags : 영상 파일 불러오기 옵션 플래그. ImreadModes 열거형 상수를 지정합니다.
  - IMREAD_UNCHANGED
  - IMREAD_GRAYSCALE
  - IMREAD_COLOR
  - IMREAD_REDUCE_GRAYSALE_2
  - IMREAD_REDUCE_COLOR_2
  - IMREAD_IGNORE_ORIENTATION

### imwrite()

```cpp
bool imwrite(const String& filename, InputArray img, const std::vector<int>& params = std::vector<int>());
```

- filename : 저장할 영상 파일 이름
- img : 저장할 영상 데이터(Mat 객체)
- params : 저장할 영상 파일 형식에 의존적인 파라미터(플래그 & 값) 쌍

### empty()

```cpp
bool Mat::empty() const
```

### namedWindow()

```cpp
void namedWindow(const String& window, int flags = WINDOW_AUTOSIZE);
```

- winname : 영상 출력 창 상단에 출력되는 창 고유 이름. 이 문자열로 창을 구분합니다.
- flags : 생성되는 창의 속성을 지정하는 플래그. WindowFlags 열거형 상수를 지정합니다.
  - WINDOW_NORMAL
  - WINDOW_AUTOSIZE
  - WINDOW_OPENGL

### destroyWindow()

```cpp
void destroyWindow(const String& winname);
void destroyAllWindow();
```

- winname : 소멸시킬 창 이름

### moveWindow()

```cpp
void moveWindow(const String& window, int x, int y);
```

- winname : 위치를 이동할 창 이름
- x : 창이 이동할 위치의 x 좌표
- y : 창이 이동할 위치의 y 좌표

### resizeWindow()

```cpp
void resizeWindow(const String& winname, int width, int height);
```

- winname : 크기를 변경할 창 이름
- width : 창의 가로 크기
- height : 창의 세로 크기

### imshow()

```cpp
void imshow(const String& winname, InputArray mat);
```

- winname : 영상을 출력할 대상 창 이름
- mat : 출력할 영상 데이터(Mat 객체)

### waitKey()

```cpp
int waitKey(int delay = 0);
```

- delay : 키 입력을 기다릴 시간(밀리초 단위). delay ≤ 0이면 무한히 기다립니다.
