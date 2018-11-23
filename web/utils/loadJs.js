/*
动态加载js方法
*/
function loadJs(url,callback){
  var script=document.createElement('script');
  script.type="text/javascript";
  if(typeof(callback)!="undefined"){
    if(script.readyState){
      script.onreadystatechange=function(){
        if(script.readyState == "loaded" || script.readyState == "complete"){
          script.onreadystatechange=null;
          callback();
        }
      }
    }
    else{
      script.onload=function(){
      callback();
      }
    } 
  } 
  script.src=url;
  document.body.appendChild(script);
}

/*
适用方法
loadJs("./../js/parorstu/planninghome.js?v="+Math.random(),function(){
  alert('done');
});
*/