curl http://rt.molit.go.kr/new/gis/simpleCaptcha.do --output captcha.png

ANSWER=`curl -XPOST -F 'image=@/image/path/captcha.png;filename=captcha.png' https://get-cha.herokuapp.com/predict`

curl 'http://rt.molit.go.kr/new/gis/CaptchaSubmit.do' \
  -H 'Connection: keep-alive' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Origin: http://rt.molit.go.kr' \
  -H 'Referer: http://rt.molit.go.kr/new/pop/captcha_Popup.do' \
  --data-raw "answer=$ANSWER" 
