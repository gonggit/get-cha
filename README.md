# 정부 Captcha 우회하기.


| 본 프로젝트는 [이 프로젝트](https://github.com/ferriswym/solving_captchas_code_examples)를 기반으로 만들어졌습니다. 어떤 프로젝트를 fork 하셔서 사용하셔도 관계 없습니다.

# 요청하기

```

# 한 번 요청 해보기
curl -XPOST -F 'image=@/image/path/2.png;filename=captcha.png' https://get-cha.herokuapp.com/predict

# 성공 할 때까지 요청해보기
sh solve_captcha.sh

```

