<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>


<script>
document.getElementById("btn").click();
var urls = "..."
function getRandom(min,max){
    return Math.floor(Math.random()*(max-min+1))+min;
};
a=getRandom(0,1);

function ABC(a){
  if (a==0){
  urls="https://reurl.cc/ao7XZ"
  }
  if (a==1){
  urls="https://kk665403.pixnet.net/blog"
  }
};
ABC(a);
function changeSrc(a){
  if (a==0){
  document.getElementById("iframe").src="https://reurl.cc/ao7XZ";
  }
    if (a==1){
  document.getElementById("iframe").src="https://kk665403.pixnet.net/blog";
  }

document.getElementById("button").click();
}

</script>
<input type="button" onclick="changeSrc(a)" value="Change Source">
<br>


<iframe src="https://reurl.cc/ao7XZ" id="iframe" width="250" height="1000"></iframe>

</body>
</html>
