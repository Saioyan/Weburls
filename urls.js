var url = "..."
function getRandom(min,max){
    return Math.floor(Math.random()*(max-min+1))+min;
};
a=getRandom(0,1);

function ABC(a){
  if (a==0){
  url="https://reurl.cc/ao7XZ"
  }
  if (a==1){
  url="http://www.codedata.com.tw/javascript/essential-javascript-variable/"
  }
  alert(url);
};
ABC(a);
