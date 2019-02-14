/*
两个方法：
1.loadJs：加载js文件使用，顺序加载
2.页面缩放代码
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

(function (doc, win) {
    var docEl = doc.documentElement,
      isIOS = navigator.userAgent.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/),
      dpr = isIOS? Math.min(win.devicePixelRatio, 3) : 1,
      dpr = window.top === window.self? dpr : 1, //被iframe引用时，禁止缩放
      dpr = 1,
      scale = 1 / dpr,
      resizeEvt = 'orientationchange' in window ? 'orientationchange' : 'resize';
    docEl.dataset.dpr = dpr;
    var metaEl = doc.createElement('meta');
    metaEl.name = 'viewport';
    metaEl.content = 'initial-scale=' + scale + ',maximum-scale=' + scale + ', minimum-scale=' + scale;
    docEl.firstElementChild.appendChild(metaEl);
    var recalc = function () {
        var width = docEl.clientWidth;
        if (width / dpr > 640) {
            width = 640 * dpr;
        }
        docEl.style.fontSize = 64 * (width / 640) + 'px';
      };
    recalc()
    if (!doc.addEventListener) return;
    win.addEventListener(resizeEvt, recalc, false);
  })(document, window);
